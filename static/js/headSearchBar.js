const headSearchbar1 = document.getElementById("headSearchJudge");
const headDiv1 = document.getElementById("headMatchList1");

const headSearchJudge = async (headsearch1) => {
  const res = await fetch("/judgeWithLocation/" + headsearch1 + "");
  var response = await res.json();
  let matches = response.jugeslist;
  if (matches != []) {
    headSearchbar1.style.borderBottomLeftRadius = "0px";
    headSearchbar1.style.borderBottomRightRadius = "0px";
  }
  if (headsearch1.length <= 1) {
    matches = [];
    headDiv1.innerHTML = "";
    headSearchbar1.style.borderBottomLeftRadius = "25px";
    headSearchbar1.style.borderBottomRightRadius = "25px";
  }
  headoutputHtml1(matches);
};

const headoutputHtml1 = (matches) => {
  if (matches.length > 0) {
    const html = matches
      .map(
        (match) =>
          "<div class='displayHeadNames' id='selectedHeadJudge' onclick='goToJudge(" +
          match.id +
          ")'><div class='row'><div class='align-items-left info'><b><i class='bi bi-person'></i></b><span ><b>" +
          match.name +
          "</b></span></div></div><small class='locationInfo'>Location: <b>" +
          match.location +
          "</b></small></div>"
      )
      .join("");
    headDiv1.innerHTML = html;
  }
};

headSearchbar1.addEventListener("input", () =>
  headSearchJudge(headSearchbar1.value)
);

const headSearchbar2 = document.getElementById("headSearchLocation");
const headDiv2 = document.getElementById("headMatchList2");

const headSearchLocation = async (headsearch2) => {
  const res2 = await fetch("/autocomplete3/" + headsearch2 + "");
  var response2 = await res2.json();
  let matches2 = response2.locationlist;
  if (matches2 != []) {
    headSearchbar2.style.borderBottomLeftRadius = "0px";
    headSearchbar2.style.borderBottomRightRadius = "0px";
  }
  if (headsearch2.length <= 1) {
    matches2 = [];
    headDiv2.innerHTML = "";
    headSearchbar2.style.borderBottomLeftRadius = "25px";
    headSearchbar2.style.borderBottomRightRadius = "25px";
  }
  headOutputHtml2(matches2);
};

const headOutputHtml2 = (matches2) => {
  if (matches2.length > 0) {
    const html = matches2
      .map(
        (match2) =>
          "<div class='displayHeadLocation' id='selectedHeadLocation'  onclick=goToSetLocation('" +
          match2 +
          "')><div class='row'><div class='align-items-left info'><b><i class='bi bi-pin-map-fill'></i></b><span ><b class='lName'>" +
          match2 +
          "</b></span></div></div></div>"
      )
      .join("");
    headDiv2.innerHTML = html;
  }
};

headSearchbar2.addEventListener("input", () =>
  headSearchLocation(headSearchbar2.value)
);

const headLocationDiv = document.getElementById("search-bar2");
const changeHeadLocation = document.getElementById("changeHeadLocation");
const headLocationOptionDiv = document.getElementById("headLocationOption");
const headSearchLocationValue = document.getElementById("headSearchLocation");
const setLocation = document.getElementById("setLocation");

changeHeadLocation.addEventListener("click", function () {
  headLocationDiv.style.display = "block";
  headLocationOptionDiv.style.display = "none";
});

function goToSetLocation(name) {
  console.log(name);
  const res = fetch("/setLocation/" + name + "");
  headDiv2.innerHTML = "";
  headLocationDiv.style.display = "none";
  headLocationOptionDiv.style.display = "block";
  headSearchLocationValue.value = name;
  setLocation.innerHTML =
    "<p id='setLocation'>" +
    name +
    " <i class ='fa fa-pencil' id='changeHeadLocation'></i></p>";
}
