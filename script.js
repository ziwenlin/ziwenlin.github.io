function randomColor(change, selector, saturation=100, lightness=50, alpha=0, range=240, offset=20) {
  var lijst = document.querySelectorAll(selector);
  for (var i = 0; i < lijst.length; i++) {
    var color = hsl(range, offset, saturation, lightness, alpha);
    lijst[i].style[change] = color;
    console.log(color);
  }
}

function hsl(range, offset, saturation, lightness, alpha) {
  var random = Math.floor(Math.random() * range + offset);
  return "hsl(" + random + "," + saturation + "%," + lightness + "%)";
}

/* Begin Initial */

/* Check if there is an scroll-progress-bar */
var progressContainer = document.getElementById("progress-container");
if (progressContainer) {
  addEvent(window, "scroll", onScroll);
  var sticky = progressContainer.offsetTop;
}


var collapses = document.getElementsByClassName("collapse");
for (var i = 0; i < collapses.length; i++) {
  addEvent(collapses[i], "click", togglecollapse);
}

/* End initial ******* Begin functions */

function addEvent(object, type, callback) {
  if (object == null || typeof(object) == 'undefined') return;
  if (object.addEventListener) {
    object.addEventListener(type, callback, false);
  } else if (object.attachEvent) {
    object.attachEvent("on" + type, callback);
  } else {
    object["on"+type] = callback;
  }
}

function onResize() {
  var panels = document.getElementsByClassName("panel");
  if (panels) {
    for (var i = 0; i < panels.length; i++) {
      var panel = panels[i];
      if (panel.style.maxHeight) {
        panel.style.maxHeight = panel.scrollHeight + "px";
      }
    }
  }
}

function togglecollapse() {
  this.classList.toggle("active");
  var panel = this.nextElementSibling;
  if (panel.style.maxHeight) {
    panel.style.maxHeight = null;
  } else {
    // panel.style.transitionDuration = Math.sqrt(panel.scrollHeight/4)/100 + "s";
    panel.style.maxHeight = panel.scrollHeight + "px";
    // panel.style.maxHeight = "none";
  }
}

function onScroll() {
  var docElm = document.documentElement;
  var winScroll = document.body.scrollTop || docElm.scrollTop;
  var height = docElm.scrollHeight - docElm.clientHeight;
  var progress = (winScroll / height) * 100;
  document.getElementById("progress-bar").style.width = progress + "%";
  if (winScroll > sticky) {
    progressContainer.classList.add("sticky");
  } else {
    progressContainer.classList.remove("sticky");
  }
}


/**
 * Main, start of the program
 */
function main() {
  randomColor("borderColor", "h2", 90, 70);
  randomColor("borderColor", "img", 30);
  randomColor("borderColor", "article", 100, 70, 0, 210, 20);

  addEvent(window, "resize", onResize);
}

main()