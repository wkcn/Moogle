$(document).ready(function() {
  let send_login = function() {
    $.ajax({
      url: "/accounts/login",
      type: "POST",
      dataType: "json",
      contentType: 'application/x-www-form-urlencoded; charset=utf-8',
      cache: false,
      data: {
        "email": $("input.login[name='email']").val(),
        "password": $.md5($("input.login[name='password']").val())
      },
      success: function(data) {
        if (data.code) {
          AjaxMessage(data.ret, "error");
          return false;
        } else {
          AjaxMessage(data.ret, "success");
        }
      },
      error: function() {
        AjaxFail();
      }
    });
  }

  let send_register = function() {
    if($("input.signup[name='password']").val() != $("input.signup[name='password-2']").val()) {
      AjaxMessage("两次密码不相同", "error");
      return false;
    }
    $.ajax({
      url: "/accounts/register",
      type: "POST",
      dataType: "json",
      contentType: 'application/x-www-form-urlencoded; charset=utf-8',
      cache: false,
      data: {
        "email": $("input.signup[name='email']").val(),
        "password": $.md5($("input.signup[name='password']").val()),
        "username": $("input.signup[name='username']").val(),
      },
      success: function(data) {
        if (data.code) {
          AjaxMessage(data.ret, "error");
          return false;
        } else {
          AjaxMessage(data.ret, "success");
        }
      },
      error: function() {
        AjaxFail();
      }
    });
  }

  $("#login-submit").click(send_login);
  $("#signup-submit").click(send_register);
});