// Modal logic
var modal = document.getElementById("addColumnModal");
var btn = document.getElementById("addColumnBtn");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "block";
    document.getElementById("columnName").focus();
}
span.onclick = function() {
    modal.style.display = "none";
}
window.onclick = function(event) {
if (event.target == modal) {
    modal.style.display = "none";
}
}