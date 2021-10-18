$(function () {
  $(".autocomplete").autocomplete({
    source: "/autocomplete/",
    select: function (e, ui) {
      document.getElementById("autocomplete").value = ui.item.value;
      document.getElementById("btn_ser1").submit();
    },
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

var ratebyName = document.getElementsByClassName("rateby");
for (var i = 0; i < ratebyName.length; i++) {
  ratebyName[i].addEventListener("click", function (e) {
    const tar =
      e.target.parentElement.parentElement.querySelectorAll(
        ".rating_details"
      )[0];

    if ((tar.style.display = "none")) {
      tar.style.display = "block";
    } else {
      tar.style.display = "none";
    }
  });
}
