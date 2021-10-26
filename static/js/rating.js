const likebtn = document.querySelectorAll("#reviewLikebtn");
const dislikebtn = document.querySelectorAll("#reviewDislikebtn");

const reviewLikesLable = document.querySelectorAll("#reviewLikes");
const reviewDislikesLable = document.querySelectorAll("#reviewDislikes");

const ratingDiv = document.querySelectorAll("#ratingDiv");
const reviewCategory = document.querySelectorAll("#reviewCategory");
const reviewFilter = document.querySelectorAll("#reviewSelectedFilter");

const category = document.getElementById("category");
const selectCategory = document.querySelectorAll("#selectCategory");

const toggleBtnUp = document.querySelectorAll("#toggleRatingDivUp");
const toggleBtnDown = document.querySelectorAll("#toggleRatingDivDown");

for (let i = 0; i < toggleBtnDown.length; i++) {
  toggleBtnDown[i].addEventListener("click", function (event) {
    ratingDiv[i].style.height = "100%";
    toggleBtnUp[i].style.display = "block";
    toggleBtnDown[i].style.display = "none";
  });
}

for (let i = 0; i < toggleBtnUp.length; i++) {
  toggleBtnUp[i].addEventListener("click", function (event) {
    ratingDiv[i].style.height = "350px";
    toggleBtnUp[i].style.display = "none";
    toggleBtnDown[i].style.display = "block";
  });
}

for (let i = 0; i < selectCategory.length; i++) {
  selectCategory[i].addEventListener("click", function (event) {
    var catname = event.target.getAttribute("data-category");
    category.value = catname;
  });
}

for (let i = 0; i < reviewFilter.length; i++) {
  reviewFilter[i].addEventListener("click", function (event) {
    var Rname = event.target.getAttribute("data-Rname");
    applyFilter(Rname);
  });
}

function applyFilter(Rname) {
  for (let rc = 0; rc < reviewCategory.length; rc++) {
    if (reviewCategory[rc].getAttribute("data-RCname") == Rname) {
      ratingDiv[rc].style.display = "block";
    } else {
      ratingDiv[rc].style.display = "none";
    }
  }
}

for (let i = 0; i < likebtn.length; i++) {
  likebtn[i].addEventListener("click", function (event) {
    var Rid = event.target.getAttribute("data-Rid");
    likeReview(Rid, i);
  });
}

function likeReview(Rid, i) {
  var mydata = { id: Rid };
  $.ajax({
    url: "/likereview/",
    method: "POST",
    data: mydata,
    success: function (data) {
      likebtn[i]
        .closest("#ratingArea")
        .querySelector("#reviewLikes").innerHTML = "" + data.totalLikes + ".0";

      likebtn[i]
        .closest("#ratingArea")
        .querySelector("#reviewDislikes").innerHTML =
        "" + data.totalDislikes + ".0";

      likebtn[i]
        .closest("#ratingArea")
        .querySelector("#reviewDislikebtn").style.display = "block";

      likebtn[i].style.display = "none";
    },
  });
}

for (let i = 0; i < dislikebtn.length; i++) {
  dislikebtn[i].addEventListener("click", function (event) {
    var Rid = event.target.getAttribute("data-Rid");
    dislikeReview(Rid, i);
  });
}

function dislikeReview(Rid, i) {
  var mydata = { id: Rid };
  $.ajax({
    url: "/dislikeReview/",
    method: "POST",
    data: mydata,
    success: function (data) {
      dislikebtn[i]
        .closest("#ratingArea")
        .querySelector("#reviewLikes").innerHTML = "" + data.totalLikes + ".0";

      dislikebtn[i]
        .closest("#ratingArea")
        .querySelector("#reviewDislikes").innerHTML =
        "" + data.totalDislikes + ".0";

      dislikebtn[i]
        .closest("#ratingArea")
        .querySelector("#reviewLikebtn").style.display = "block";

      dislikebtn[i].style.display = "none";
    },
  });
}
