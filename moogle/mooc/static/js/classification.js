$(document).ready(function() {
  $(".title-bg").backstretch("/static/img/home-bg-1.jpg");

  $(".row.classification").css({
    "margin-top": (300 - $(".row.classification").height()) / 2
  });

  $(".ui.shape").shape({
    onChange: function() {
      get_courses_of($(".side.active").text());
    }
  });

  $(".ui.text.shape").click(function() {
    $(".ui.dimmer.loading").dimmer("show");
    $(".ui.shape").shape("flip down");
  });

  let get_courses_of = function(classification) {
    $.ajax({
      url: "/get_classi_courses",
      type: "GET",
      dataType: "json",
      contentType: 'application/x-www-form-urlencoded; charset=utf-8',
      cache: false,
      data: {
        "cl": classification
      },
      success: function(data) {
        if (data.code) {
          AjaxMessage(data.ret, "error");
          $(".ui.dimmer.loading").dimmer("hide");
          return false;
        } else {
          $(".ui.cards.five").remove();
          $(".result.container").append(data.ret.text);
          $(".result.num").html('<i class="find icon orange"></i>共有 '+ data.ret.num +' 门课程。');
          window.footer_margin();
          $(".ui.dimmer.loading").dimmer("hide");
        }
      },
      error: function() {
        AjaxFail();
      }
    });
  }

  
  get_courses_of('全部课程');
});