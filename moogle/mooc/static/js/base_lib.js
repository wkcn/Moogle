// global
$(document).ready(function() {
  window.AjaxFail = function() {
    swal({
      title: "Oo..",
      text: "There seems to be some problem",
      type: "error",
      confirmButtonText: "Okay..."
    });
  };

  window.AjaxMessage = function(message, type) {
    swal({
      title: message,
      text: "",
      type: type,
      confirmButtonText: "Okay"
    });
  }

  window.scroll2 = function(selector, time, offset = 0) {
    $(document.body).animate({
      scrollTop: $(selector).offset().top - offset
    }, time);
  }

  window.click2 = function(selector, target, time, offset = 0) {
    $(selector).click(function() {
      window.scroll2(target, time, offset);
    })
  }

  // search box events

  $("input.main-search").keyup(function(event) {
    if (event.keyCode == 13) {
      $("#main-search-btn").click();
    }
  });

  $("#main-search-btn").click(function() {
    let keyword = $("input.main-search").val();
    window.location.href = "/search?key=" + keyword;
  })

  // footer style
  $("footer .names").css({
    "margin-top": $("footer").height() / 2 - $("footer .names").height() - $("footer .copyright").height()
  });

  window.footer_margin = function() {
    if ($("footer").offset().top + $("footer").height() < $(window).height()) {
      $("footer").css({
        "margin-top": $(window).height() - $("footer").offset().top - $("footer").height() + 30
      })
    }
  }


  $(window).scroll(function() {
    if ($(this).scrollTop() > 300) {
      $(".scroll-to-top").fadeIn();
    } else {
      $(".scroll-to-top").hide();
    }
  });

  window.click2(".to.top", "#top-menu", 190, 0);
});