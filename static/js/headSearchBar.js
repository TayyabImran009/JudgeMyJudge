const sHead1 = document.getElementById("sOpHead1");
const sHead2 = document.getElementById("sOpHead2");

const sHdiv1 = document.getElementById("hsearch-bar1");
const sHdiv2 = document.getElementById("hsearch-bar2");

sHead2.addEventListener("click", function () {
  sHead1.style.display = "block";
  sHdiv1.style.display = "block";

  sHdiv2.style.display = "none";
  sHead2.style.display = "none";
});

sHead1.addEventListener("click", function () {
  sHead1.style.display = "none";
  sHdiv1.style.display = "none";

  sHead2.style.display = "block";
  sHdiv2.style.display = "block";
});
