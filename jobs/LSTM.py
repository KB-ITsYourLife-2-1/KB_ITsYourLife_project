def func():
    from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
    from sklearn.preprocessing import MinMaxScaler, RobustScaler
    from statsmodels.tsa.seasonal import seasonal_decompose, STL
    from keras.callbacks import ModelCheckpoint, EarlyStopping
    from tensorflow.keras.layers import Dense, LSTM, Dropout
    from tensorflow.keras import Sequential
    from tensorflow.keras import layers
    import matplotlib.pyplot as plt
    import tensorflow as tf
    import pandas as pd
    import numpy as np
    import os
    plt.rc('font', family='NanumBarunGothic')

    class Nong1:

        def __init__(self, df, test):
            self.df = df
            self.test = test
            self.df = pd.concat([self.df, self.test], axis=0)
            self.df.date = pd.to_datetime(self.df.date)
            self.df = pd.concat([self.df, pd.get_dummies(self.df['요일'])], axis=1)
            self.feature = self.df.columns[2:]
            self.df = self.df.reset_index(drop=True)

        def set_feature(self, name):
            self.name = name
            self.name1 = name + "_가격(원/kg)"
            self.name2 = name + "_거래량(kg)"
            self.feature = [self.name1, self.name2, '금요일', '목요일', '수요일', '월요일', '일요일', '토요일', '화요일', 'resid']

        def set_target(self, day):
            self.df['target'] = self.df[self.name1].shift(day)
            self.df['resid'] = 0
            stl = STL(self.df[['date', self.name1]].set_index('date'), period=12)
            res = stl.fit()
            self.df['resid'] = res.resid.values

        def set_model(self):
            self.scaler = MinMaxScaler()
            self.df[self.feature] = self.scaler.fit_transform(self.df[self.feature])
            self.df_learn = self.df[self.df['target'].notnull()]
            self.X = self.df_learn[self.feature].values.reshape(-1, 1, len(self.feature))
            self.y = self.df_learn['target'].values.reshape(-1, 1, 1)
            # self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, shuffle=False)

            with tf.device('/device:GPU:0'):
                self.model = Sequential()
                self.model.add(layers.Activation('relu'))
                self.model.add(
                    tf.compat.v1.keras.layers.CuDNNLSTM(100, input_shape=(21, len(self.feature)), return_sequences=True))
                self.model.add(Dropout(0.1))
                self.model.add(layers.Dense(30))
                self.model.add(Dropout(0.1))
                self.model.add(layers.Dense(1))
                self.model.compile(optimizer='adam', loss='mse')
                self.early_stopping = EarlyStopping(patience=300)
                self.model.fit(self.X, self.y, epochs=1000, batch_size=32, validation_split=0.1,
                               callbacks=[self.early_stopping], verbose=0)

        def get_plot(self):
            self.y_pred = self.model.predict(self.X)
            self.MAE = mean_absolute_error(self.y.reshape(-1, 1), self.y_pred.reshape(-1, 1))

            plt.figure(figsize=(20, 10), dpi=300)
            plt.title(self.name + ' 가격 예측 결과' + '   MAE : ' + str(self.MAE)[:7])
            plt.ylabel(self.name + ' 가격')
            plt.plot(np.array(self.y.reshape(-1, 1)), alpha=0.9, label='Real')
            plt.plot(self.model.predict(self.X).reshape(-1, 1), alpha=0.6, linestyle="--", label='Predict')
            plt.legend()
            plt.show()

        def get_price(self):
            self.price = self.model.predict(
                self.df[self.feature].iloc[len(self.df) - 1].values.reshape(-1, 1, len(self.feature)))
            return self.price[0][0][0]

    today = datetime.now() - timedelta(1)
    today = today.year * 10000 + today.month * 100 + today.day

    last = datetime.now() - timedelta(7)
    last = last.year * 10000 + last.month * 100 + last.day

    data = pd.read_csv(f"./statistic/static/graph/base_data_{today}.csv")
    if 'Unnamed: 0' in data.columns:
        data.drop(['Unnamed: 0'], axis = 1, inplace = True)
    data.iloc[:,2:] = (data.iloc[:,2:].bfill() + data.iloc[:,2:].ffill()) / 2

    my_nong1 = Nong1(data.iloc[:-1], data.iloc[[-1]])

    features = ['배추', '양파', '마늘', '깻잎','대파', '상추', '양상추', '무', '시금치']

    day7=[]

    for feature in features:
      print(feature)
      a = 0
      for i in range(2,8):
        print(i)
        my_nong1 = Nong1(data.iloc[:-1], data.iloc[[-1]])
        my_nong1.set_feature(feature)
        my_nong1.set_target(i)
        my_nong1.set_model()
        a += my_nong1.get_price()
      day7.append(round(a/7, 0).astype(int))

    submmision = pd.DataFrame(day7).T
    submmision.columns = features

    submmision.to_csv(f'./predict/static/images/predict_{today}.csv')

    if os.path.exists(f'./predict/static/images/predict_{last}.csv'):
        os.remove(f'./predict/static/images/predict__{last}.csv')