$(function() {
    $('#vege_all > button').click(function(){
        $('#vege_all > button').attr('disabled',true)
        var vege_chs = this.innerText
        var str="";
          str += "<div id='cm-msg-2' class='chat-msg self'>";
          str += "          <div class='cm-msg-text'>";
          str += "            <div id = 'choose_1'>";
          str += vege_chs + ' 을/를 클릭했습니다.';
          str += '            </div>';
          str += "          </div>";
          str += "        </div>";
          $(".chat-logs").append(str);
          $("#cm-msg-2").hide().fadeIn(500);
        var id = this.id
        if(id==1){
            var str="";
          str += "<div id='cm-msg-3' class='chat-msg user'>";
          str += "          <div class='cm-msg-text'>";
          str += "            <div id = 'find_all_'>";
          str += '                <button id = "find_"  onclick="location.href=\'/predict/product_1\'">가격 예측</button>';
          str += '                <button id = "find_" onclick="location.href=\'statistic/product_1\'">통계 자료</button>';
          str += '                <button id = "find_else" onclick="location.href=\'/about/product_1\'">농사물 바로 알기</button>';
          str += '            </div>';
          str += "          </div>";
          str += "        </div>";
          $(".chat-logs").append(str);
          $("#cm-msg-3").hide().fadeIn(1500);
        }
        else if(id==2){
            var str="";
          str += "<div id='cm-msg-3' class='chat-msg user'>";
          str += "          <div class='cm-msg-text'>";
          str += "            <div id = 'find_all_'>";
          str += '                <button id = "find_"  onclick="location.href=\'/predict/product_2\'">가격 예측</button>';
          str += '                <button id = "find_" onclick="location.href=\'statistic/product_2\'">통계 자료</button>';
          str += '                <button id = "find_else" onclick="location.href=\'/about/product_2\'">농사물 바로 알기</button>';
          str += '            </div>';
          str += "          </div>";
          str += "        </div>";
          $(".chat-logs").append(str);
          $("#cm-msg-3").hide().fadeIn(1500);
        }
        else if(id==3){
            var str="";
          str += "<div id='cm-msg-3' class='chat-msg user'>";
          str += "          <div class='cm-msg-text'>";
          str += "            <div id = 'find_all_'>";
          str += '                <button id = "find_"  onclick="location.href=\'/predict/product_3\'">가격 예측</button>';
          str += '                <button id = "find_" onclick="location.href=\'statistic/product_3\'">통계 자료</button>';
          str += '                <button id = "find_else" onclick="location.href=\'/about/product_3\'">농사물 바로 알기</button>';
          str += '            </div>';
          str += "          </div>";
          str += "        </div>";
          $(".chat-logs").append(str);
          $("#cm-msg-3").hide().fadeIn(1500);
        }
        else if(id==4){
            var str="";
          str += "<div id='cm-msg-3' class='chat-msg user'>";
          str += "          <div class='cm-msg-text'>";
          str += "            <div id = 'find_all_'>";
          str += '                <button id = "find_"  onclick="location.href=\'/predict/product_4\'">가격 예측</button>';
          str += '                <button id = "find_" onclick="location.href=\'statistic/product_4\'">통계 자료</button>';
          str += '                <button id = "find_else" onclick="location.href=\'/about/product_4\'">농사물 바로 알기</button>';
          str += '            </div>';
          str += "          </div>";
          str += "        </div>";
          $(".chat-logs").append(str);
          $("#cm-msg-3").hide().fadeIn(1500);
        }
        else if(id==5){
            var str="";
          str += "<div id='cm-msg-3' class='chat-msg user'>";
          str += "          <div class='cm-msg-text'>";
          str += "            <div id = 'find_all_'>";
          str += '                <button id = "find_"  onclick="location.href=\'/predict/product_5\'">가격 예측</button>';
          str += '                <button id = "find_" onclick="location.href=\'statistic/product_5\'">통계 자료</button>';
          str += '                <button id = "find_else" onclick="location.href=\'/about/product_5\'">농사물 바로 알기</button>';
          str += '            </div>';
          str += "          </div>";
          str += "        </div>";
          $(".chat-logs").append(str);
          $("#cm-msg-3").hide().fadeIn(1500);
        }
        else if(id==6){
            var str="";
          str += "<div id='cm-msg-3' class='chat-msg user'>";
          str += "          <div class='cm-msg-text'>";
          str += "            <div id = 'find_all_'>";
          str += '                <button id = "find_"  onclick="location.href=\'/predict/product_6\'">가격 예측</button>';
          str += '                <button id = "find_" onclick="location.href=\'statistic/product_6\'">통계 자료</button>';
          str += '                <button id = "find_else" onclick="location.href=\'/about/product_6\'">농사물 바로 알기</button>';
          str += '            </div>';
          str += "          </div>";
          str += "        </div>";
          $(".chat-logs").append(str);
          $("#cm-msg-3").hide().fadeIn(1500);
        }
        else if(id==7){
            var str="";
          str += "<div id='cm-msg-3' class='chat-msg user'>";
          str += "          <div class='cm-msg-text'>";
          str += "            <div id = 'find_all_'>";
          str += '                <button id = "find_"  onclick="location.href=\'/predict/product_7\'">가격 예측</button>';
          str += '                <button id = "find_" onclick="location.href=\'statistic/product_7\'">통계 자료</button>';
          str += '                <button id = "find_else" onclick="location.href=\'/about/product_7\'">농사물 바로 알기</button>';
          str += '            </div>';
          str += "          </div>";
          str += "        </div>";
          $(".chat-logs").append(str);
          $("#cm-msg-3").hide().fadeIn(1500);
        }
        else if(id==8){
            var str="";
          str += "<div id='cm-msg-3' class='chat-msg user'>";
          str += "          <div class='cm-msg-text'>";
          str += "            <div id = 'find_all_'>";
          str += '                <button id = "find_"  onclick="location.href=\'/predict/product_8\'">가격 예측</button>';
          str += '                <button id = "find_" onclick="location.href=\'statistic/product_8\'">통계 자료</button>';
          str += '                <button id = "find_else" onclick="location.href=\'/about/product_8\'">농사물 바로 알기</button>';
          str += '            </div>';
          str += "          </div>";
          str += "        </div>";
          $(".chat-logs").append(str);
          $("#cm-msg-3").hide().fadeIn(1500);
        }
        else if(id==9){
            var str="";
          str += "<div id='cm-msg-3' class='chat-msg user'>";
          str += "          <div class='cm-msg-text'>";
          str += "            <div id = 'find_all_'>";
          str += '                <button id = "find_"  onclick="location.href=\'/predict\'">가격 예측</button>';
          str += '                <button id = "find_" onclick="location.href=\'statistic\'">통계 자료</button>';
          str += '                <button id = "find_else" onclick="location.href=\'/about_1\'">농사물 바로 알기</button>';
          str += '            </div>';
          str += "          </div>";
          str += "        </div>";
          $(".chat-logs").append(str);
          $("#cm-msg-3").hide().fadeIn(1500);
        }

         var str="";
          str += "<div id='cm-msg-4' class='chat-msg-user'>";
          str += "          <div class='cm-msg-text'>";
          str += "            <div id = 'choose_1'>";
          str += ' 농산물을 다시 선택하시려면 우측상단의 휴지통을 눌러주세요.';
          str += '            </div>';
          str += "          </div>";
          str += "        </div>";
          $(".chat-logs").append(str);
          $("#cm-msg-4").hide().fadeIn(500);
    })

    var INDEX = 0;
    $("#chat-submit").click(function(e) {
      e.preventDefault();
      var msg = $("#chat-input").val(); 
      if(msg.trim() == ''){
        return false;
      }
      generate_message(msg, 'self');
      setTimeout(function(){
        generate_message(msg, 'user');
      }, 300)
    })

    function generate_message(msg, type) {
      INDEX++;
      if(type == 'user'){
          var str="";
          str += "<div id='cm-msg-"+INDEX+"' class=\"chat-msg "+type+"\">";
          str += "          <span class=\"msg-avatar\">";
          str += "          <img src=\"../../static/images/nong.jpg\">";
          str += "          <\/span>";
          str += "          <div class=\"cm-msg-text\">";
          str += 10;
          str += "          <\/div>";
          str += "        <\/div>";
          $(".chat-logs").append(str);
          $("#cm-msg-"+INDEX).hide().fadeIn(300);
      }
      if(type == 'self'){
          var str="";
          str += "<div id='cm-msg-"+INDEX+"' class=\"chat-msg "+type+"\">";
          str += "          <span class=\"msg-avatar\">";
          str += "            <img src=\"../../static/images/user.png\">";
          str += "          <\/span>";
          str += "          <div class=\"cm-msg-text\">";
          str += msg;
          str += "          <\/div>";
          str += "        <\/div>";
          $(".chat-logs").append(str);
          $("#cm-msg-"+INDEX).hide().fadeIn(300);
          $("#chat-input").val('');
      }    
      $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000);    
    }  
    
    
    $(document).delegate(".chat-btn", "click", function() {
      var value = $(this).attr("chat-value");
      var name = $(this).html();
      $("#chat-input").attr("disabled", false);
      generate_message(name, 'self');
    })
    
    $("#chat-circle").click(function() {    
      $("#chat-circle").toggle('scale');
      $(".chat-box").toggle('scale');
    })
    
    $(".chat-box-toggle").click(function() {
      $("#chat-circle").toggle('scale');
      $(".chat-box").toggle('scale');
    })

    $(".chat-box-reset").click(function() {
      $("div").detach("#cm-msg-2")
      $("div").detach("#cm-msg-3")
      $('#vege_all > button').attr('disabled',false)
    })

  })

 