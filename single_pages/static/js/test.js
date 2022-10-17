$(function() {
    $('#vege_all > button').click(function(){
        $('#vege_all > button').attr('disabled',true)
        var vege_chs = this.innerText
        var str="";
          str += "<div id='cm-msg-2' class='chat-msg self'>";
          str += "          <div class='cm-msg-text'>";
          str += "            <div id = 'choose_1'>";
          str += vege_chs + '를 클릭했습니다.';
          str += '            </div>';
          str += "          </div>";
          str += "        </div>";
          $(".chat-logs").append(str);
          $("#cm-msg-2").hide().fadeIn(500);
        var str="";
          str += "<div id='cm-msg-3' class='chat-msg user'>";
          str += "          <div class='cm-msg-text'>";
          str += "            <div id = 'find_all_'>";
          str += '                <button id = "find_"  onclick="location.href=\'http://www.naver.com\'">가격 예측</button>';
          str += '                <button id = "find_" onclick="location.href=\'http://www.google.com\'">통계 자료</button>';
          str += '                <button id = "find_else" onclick="location.href=\'http://www.google.com\'">농사물 바로 알기</button>';
          str += '            </div>';
          str += "          </div>";
          str += "        </div>";
          $(".chat-logs").append(str);
          $("#cm-msg-3").hide().fadeIn(1500);
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
          str += "            <img src=\"https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA0MTVfMTgx%2FMDAxNjUwMDE0MDAzNDg5.eryItdOF2i9tpWB6fYUdYtN4qABYmNLGEOz089yN4Xwg.bT6P2unkDBKpqbCvMUZ7Ho9L6fdIne3D6HPhekLB4p0g.JPEG.an3895%2FIMG_5102.jpg&type=a340\">";
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
          str += "            <img src=\"https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA0MTVfMTgx%2FMDAxNjUwMDE0MDAzNDg5.eryItdOF2i9tpWB6fYUdYtN4qABYmNLGEOz089yN4Xwg.bT6P2unkDBKpqbCvMUZ7Ho9L6fdIne3D6HPhekLB4p0g.JPEG.an3895%2FIMG_5102.jpg&type=a340\">";
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

 