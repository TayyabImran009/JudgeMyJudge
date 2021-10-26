const searchOption1 = document.getElementById("sOptions1");
const searchOption2 = document.getElementById("sOptions2");

const searchdiv1 = document.getElementById("sDiv1");
const searchdiv2 = document.getElementById("sDiv2");

searchOption1.addEventListener("click", function () {
  searchdiv1.style.display = "none";
  searchdiv2.style.display = "block";
});

searchOption2.addEventListener("click", function () {
  searchdiv2.style.display = "none";
  searchdiv1.style.display = "block";
});

const search2 = document.getElementById("searchLocation");
const matchList2 = document.getElementById("match-list2");

const searchLocation = async (searchText2) => {
  const res2 = await fetch("/autocomplete3/" + searchText2 + "");
  var response2 = await res2.json();
  let matches2 = response2.locationlist;
  console.log("Here");
  if (matches2 != []) {
    search2.style.borderBottomLeftRadius = "0px";
    search2.style.borderBottomRightRadius = "0px";
  }
  if (searchText2.length <= 1) {
    matches2 = [];
    matchList2.innerHTML = "";
    search2.style.borderBottomLeftRadius = "25px";
    search2.style.borderBottomRightRadius = "25px";
  }
  outputHtml2(matches2);
};

const outputHtml2 = (matches2) => {
  if (matches2.length > 0) {
    const html = matches2
      .map(
        (match2) =>
          "<div class='displayLocation' id='selectedLocation'  onclick=goToLocation2('" +
          match2 +
          "')><div class='row'><div class='align-items-left info'><b><i class='bi bi-pin-map-fill'></i></b><span ><b class='lName'>" +
          match2 +
          "</b></span></div></div></div>"
      )
      .join("");
    matchList2.innerHTML = html;
  }
};

search2.addEventListener("input", () => searchLocation(search2.value));

function goToLocation2(myvalue) {
  window.location.replace("/getJudgeByLocation/" + myvalue);
}
