const likebtn = document.querySelectorAll("#reviewLikebtn");
const dislikebtn = document.querySelectorAll("#reviewDislikebtn");

const reviewLikesLable = document.querySelectorAll("#reviewLikes");
const reviewDislikesLable = document.querySelectorAll("#reviewDislikes");

const ratingDiv = document.querySelectorAll("#ratingDiv");
const reviewCategory = document.querySelectorAll("#reviewCategory");
const reviewFilter = document.querySelectorAll("#reviewSelectedFilter");

const filterDropdownBtn = document.getElementById("filterDropdownBtn");

const category = document.getElementById("category");
const selectCategory = document.querySelectorAll("#selectCategory");

const toggleBtnUp = document.querySelectorAll("#toggleRatingDivUp");
const toggleBtnDown = document.querySelectorAll("#toggleRatingDivDown");

const judgeRatingTags = document.querySelectorAll("#judgeRatingTags");

const tag1 = document.getElementById("tag1");
const tag2 = document.getElementById("tag2");
const tag3 = document.getElementById("tag3");

let tagCount = 0;
for (let i = 0; i < judgeRatingTags.length; i++) {
  judgeRatingTags[i].addEventListener("click", function (event) {
    if (tagCount < 3) {
      if (judgeRatingTags[i].classList.contains("judgeRatingTags")) {
        judgeRatingTags[i].classList.add("selectedTag", "nothing");
        judgeRatingTags[i].classList.remove("judgeRatingTags", "nothing");
        tagCount++;
        addTag(judgeRatingTags[i].getAttribute("data-tagName"));
      } else {
        judgeRatingTags[i].classList.remove("selectedTag", "nothing");
        judgeRatingTags[i].classList.add("judgeRatingTags", "nothing");
        tagCount--;
        removeTag(judgeRatingTags[i].getAttribute("data-tagName"));
      }
    } else {
      if (judgeRatingTags[i].classList.contains("selectedTag")) {
        judgeRatingTags[i].classList.remove("selectedTag", "nothing");
        judgeRatingTags[i].classList.add("judgeRatingTags", "nothing");
        tagCount--;
        removeTag(judgeRatingTags[i].getAttribute("data-tagName"));
      }
    }
  });
}

function addTag(tag) {
  if (tag1.value == "") {
    tag1.value = tag;
  } else if (tag2.value == "") {
    tag2.value = tag;
  } else {
    tag3.value = tag;
  }
}

function removeTag(tag) {
  if (tag1.value == tag) {
    tag1.value = "";
  } else if (tag2.value == tag) {
    tag2.value = "";
  } else {
    tag3.value = "";
  }
}

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
    filterDropdownBtn.innerHTML = Rname;
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

const updateTag = document.querySelectorAll("#updateTag");

const updateTag1 = document.getElementById("updateTag1");
const updateTag2 = document.getElementById("updateTag2");
const updateTag3 = document.getElementById("updateTag3");

let updateTagsCount = 0;

if (updateTag1.value != "") {
  updateTagsCount++;
}
if (updateTag2.value != "") {
  updateTagsCount++;
}
if (updateTag3.value != "") {
  updateTagsCount++;
}

for (let i = 0; i < updateTag.length; i++) {
  updateTag[i].addEventListener("click", function (event) {
    if (updateTagsCount < 3) {
      if (updateTag[i].classList.contains("updateJudgeRatingTags")) {
        updateTag[i].classList.add("updateSelectedTag", "nothing");
        updateTag[i].classList.remove("updateJudgeRatingTags", "nothing");
        updateTagsCount++;
        updateAddTag(updateTag[i].getAttribute("data-tagName"));
      } else {
        updateTag[i].classList.remove("updateSelectedTag", "nothing");
        updateTag[i].classList.add("updateJudgeRatingTags", "nothing");
        updateTagsCount--;
        updateRemoveTag(updateTag[i].getAttribute("data-tagName"));
      }
    } else {
      if (updateTag[i].classList.contains("updateSelectedTag")) {
        updateTag[i].classList.remove("updateSelectedTag", "nothing");
        updateTag[i].classList.add("updateJudgeRatingTags", "nothing");
        updateTagsCount--;
        updateRemoveTag(updateTag[i].getAttribute("data-tagName"));
      }
    }
  });
}

function updateAddTag(tag) {
  if (updateTag1.value == "") {
    updateTag1.value = tag;
  } else if (updateTag2.value == "") {
    updateTag2.value = tag;
  } else {
    updateTag3.value = tag;
  }
}

function updateRemoveTag(tag) {
  if (updateTag1.value == tag) {
    updateTag1.value = "";
  } else if (updateTag2.value == tag) {
    updateTag2.value = "";
  } else {
    updateTag3.value = "";
  }
}

const updateCategory = document.querySelectorAll("#updateCategory");

const updateCategoryInput = document.getElementById("Editcategory");

const updateCategoryDropdownBtn = document.getElementById(
  "updateCategoryDropdownBtn"
);

for (let i = 0; i < updateCategory.length; i++) {
  updateCategory[i].addEventListener("click", function (event) {
    console.log(updateCategoryInput);
    var catname = event.target.getAttribute("data-category");
    updateCategoryInput.value = catname;
    updateCategoryDropdownBtn.innerHTML = catname;
  });
}
