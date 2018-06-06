
var freshTomatoesLongDescription = `Fresh Tomatoes!<br>
                  <span style="font-size:0.7em">
                    A place where you can bookmark your favorite movies!
                  </span>`;

var gitEnvironmentLongDescription = `A Perfect Git Environment<br>
                  <span style="font-size:0.7em">
                    Makes your bash environment beautiful with
                    <em>
                      completions!
                    </em>
                  </span>`

var spaAppLongDescription = `Sadona Salon + Spa App<br>
                  <span style="font-size:0.7em">
                    Helps Sadona's amazing staff stay on top of business!
                  </span>`

function getViewportSize() {
  if ($(window).width() < 450) {
    return "under 451";
  } else {
    return "over 450";
  }
}

function changeFeatureDescriptions() {
  var viewportSize = getViewportSize();
  if (viewportSize == "under 451") {
    makeSmallFeatureDescription();
  }

  if (viewportSize == "over 450") {
    makeLargeFeatureDescription();
  }
}

function makeLargeFeatureDescription() {
  $("#freshTomatoesDescription").html(freshTomatoesLongDescription);
  $("#perfectGitDescription").html(gitEnvironmentLongDescription);
  $("#spaAppDescription").html(spaAppLongDescription);
}

function makeSmallFeatureDescription() {
  $("#freshTomatoesDescription").text("Fresh Tomatoes!");
  $("#perfectGitDescription").text("A Perfect Git Environment");
  $("#spaAppDescription").text("Sadona Salon + Spa App");
}
