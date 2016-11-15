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

  window.scroll2 = function(selector, time, offset=0) {
    $(document.body).animate({
      scrollTop: $(selector).offset().top - offset
    }, time);
  }

  window.click2 = function(selector, target, time, offset=0) {
    $(selector).click(function() {
      window.scroll2(target, time, offset);
    })
  }

  // search box events

  $("input.main-search").keyup(function(event) {
    if(event.keyCode == 13) {
      $("#main-search-btn").click();
    }
  });

  $("#main-search-btn").click(function() {
    let keyword = $("input.main-search").val();
    window.location.href = "/search?key=" + keyword ;
  })

});