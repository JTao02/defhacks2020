var slider = document.getElementById("myRange");
var output = document.getElementById("radius-input");
output.innerHTML = slider.value + "m"; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value + "m";
}