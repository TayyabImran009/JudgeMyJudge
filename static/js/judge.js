$(function () {
  $(".autocomplete").autocomplete({
    source: "/autocomplete/",
  });
});

//

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
