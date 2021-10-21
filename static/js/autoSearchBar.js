const search = document.getElementById("searchJudge");
const matchList = document.getElementById("match-list");

const searchJudges = async (searchText) => {
  const res = await fetch("/autocomplete2/" + searchText + "");
  var response = await res.json();
  let matches = response.jugeslist;
  if (matches != []) {
    search.style.borderTopLeftRadius = "25px";
    search.style.borderTopRightRadius = "25px";
  }
  if (searchText.length <= 1) {
    matches = [];
    matchList.innerHTML = "";
    search.style.borderTopLeftRadius = "0px";
    search.style.borderTopRightRadius = "0px";
  }
  outputHtml(matches);
};

const outputHtml = (matches) => {
  if (matches.length > 0) {
    const html = matches
      .map(
        (match) =>
          "<div class='displayNames' id='selectedJudge' onclick='goToJudge(" +
          match.id +
          ")'><div class='row'><div class='align-items-left info'><b><i class='bi bi-person'></i></b><span ><b>" +
          match.name +
          "</b></span></div></div><small class='locationInfo'>Location: <b>" +
          match.location +
          "</b></small></div>"
      )
      .join("");
    matchList.innerHTML = html;
  }
};

search.addEventListener("input", () => searchJudges(search.value));

function goToJudge(id) {
  window.location.replace("/getJudge2/" + id);
}
