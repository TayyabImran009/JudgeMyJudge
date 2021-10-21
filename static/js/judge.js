$(function () {
  $(".autocomplete").autocomplete({
    source: "/autocomplete/",
    select: function (e, ui) {
      document.getElementById("autocomplete").value = ui.item.value;
      document.getElementById("btn_ser1").submit();
    },
  });
});

// $(function () {
//   $(".autocompleteLocation").autocomplete({
//     source: "/autocompleteLocation/",
//     select: function (e, ui) {
//       document.getElementById("autocompleteLocation").value = ui.item.value;
//       document.getElementById("btn_ser2").submit();
//     },
//   });
// });

//Add

const star1 = document.getElementById("star1");
const star2 = document.getElementById("star2");
const star3 = document.getElementById("star3");
const star4 = document.getElementById("star4");
const star5 = document.getElementById("star5");

var score = document.getElementById("score");

const arr = [star1, star2, star3, star4, star5];

const setScore = (selection) => {
  switch (selection) {
    case "star1": {
      star1.classList.add("checked");
      star2.classList.remove("checked");
      star3.classList.remove("checked");
      star4.classList.remove("checked");
      star5.classList.remove("checked");
      score.value = 1;
      return;
    }

    case "star2": {
      star1.classList.add("checked");
      star2.classList.add("checked");
      star3.classList.remove("checked");
      star4.classList.remove("checked");
      star5.classList.remove("checked");
      score.value = 2;
      return;
    }
    case "star3": {
      star1.classList.add("checked");
      star2.classList.add("checked");
      star3.classList.add("checked");
      star4.classList.remove("checked");
      star5.classList.remove("checked");
      score.value = 3;
      return;
    }
    case "star4": {
      star1.classList.add("checked");
      star2.classList.add("checked");
      star3.classList.add("checked");
      star4.classList.add("checked");
      star5.classList.remove("checked");
      score.value = 4;
      return;
    }
    case "star5": {
      star1.classList.add("checked");
      star2.classList.add("checked");
      star3.classList.add("checked");
      star4.classList.add("checked");
      star5.classList.add("checked");
      score.value = 5;
      return;
    }
  }
};

arr.forEach((item) =>
  item.addEventListener("click", (event) => {
    setScore(event.target.id);
  })
);

//Edit

const star1_1 = document.getElementById("star1_1");
const star2_1 = document.getElementById("star2_1");
const star3_1 = document.getElementById("star3_1");
const star4_1 = document.getElementById("star4_1");
const star5_1 = document.getElementById("star5_1");

var rating = document.getElementById("rating");

const arr2 = [star1_1, star2_1, star3_1, star4_1, star5_1];

const setScore2 = (selection) => {
  switch (selection) {
    case "star1_1": {
      star1_1.classList.add("checked");
      star2_1.classList.remove("checked");
      star3_1.classList.remove("checked");
      star4_1.classList.remove("checked");
      star5_1.classList.remove("checked");
      rating.value = 1;
      return;
    }

    case "star2_1": {
      star1_1.classList.add("checked");
      star2_1.classList.add("checked");
      star3_1.classList.remove("checked");
      star4_1.classList.remove("checked");
      star5_1.classList.remove("checked");
      rating.value = 2;
      return;
    }
    case "star3_1": {
      star1_1.classList.add("checked");
      star2_1.classList.add("checked");
      star3_1.classList.add("checked");
      star4_1.classList.remove("checked");
      star5_1.classList.remove("checked");
      rating.value = 3;
      return;
    }
    case "star4_1": {
      star1_1.classList.add("checked");
      star2_1.classList.add("checked");
      star3_1.classList.add("checked");
      star4_1.classList.add("checked");
      star5_1.classList.remove("checked");
      rating.value = 4;
      return;
    }
    case "star5_1": {
      star1_1.classList.add("checked");
      star2_1.classList.add("checked");
      star3_1.classList.add("checked");
      star4_1.classList.add("checked");
      star5_1.classList.add("checked");
      rating.value = 5;
      return;
    }
  }
};

arr2.forEach((item) =>
  item.addEventListener("click", (event) => {
    setScore2(event.target.id);
  })
);
