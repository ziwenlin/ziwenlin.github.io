function accordion() {
  this.classList.toggle("active");
  var panel = this.nextElementSibling;
  if (panel.style.maxHeight) {
    panel.style.maxHeight = null;
  } else {
    panel.style.maxHeight = panel.scrollHeight + "px";
  }
}

function scrollbar() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  if(document.getElementById("progress-bar")) {
    if (window.pageYOffset > sticky) {
      scrollbar.classList.add("sticky");
    } else {
      scrollbar.classList.remove("sticky");
    }
    document.getElementById("progress-bar").style.width = scrolled + "%";
  }
}

if (document.getElementById("progress-container")) {
  window.onscroll = scrollbar;
  var scrollbar = document.getElementById("progress-container");
  var sticky = scrollbar.offsetTop;
}

var acc = document.getElementsByClassName("accordion");
for (var i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", accordion);
}
