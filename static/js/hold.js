const name = document.querySelector("#autocomplete");
$(function () {
  $(".autocomplete").autocomplete({
    source: "/autocomplete/",
    select: function (e, ui) {
      document.querySelector("#btn00909").click();
    },
  });
});