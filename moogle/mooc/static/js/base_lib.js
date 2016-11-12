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

  window.scroll2 = function(obj, time) {
    $(document.body).animate({
      scrollTop: $(obj).offset().top
    }, time);
  }

});