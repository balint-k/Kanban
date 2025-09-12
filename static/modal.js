// Modal logic
var modal = document.getElementById("addColumnModal");
var btn = document.getElementById("addColumnBtn");
var columnSpan = document.getElementById("closeColumnModal");

var taskModal = document.getElementById("addTaskModal");
var taskSpan = document.getElementById("closeTaskModal");

btn.onclick = function() {
    modal.style.display = "block";
    document.getElementById("columnName").focus();
}
columnSpan.onclick = function() {
    modal.style.display = "none";
    document.getElementById("columnName").value = "";
}
window.onclick = function(event) {
if (event.target == modal) {
    modal.style.display = "none";
}
}


taskSpan.onclick = function() {
    taskModal.style.display = "none";
    document.getElementById("taskTitle").value = "";
    document.getElementById("taskDescription").value = "";
    document.getElementById("taskColumnId").value = "";
}


function addTask(columnId) {
    taskModal.style.display = "block";
    document.getElementById("taskTitle").focus();
    document.getElementById("taskColumnId").value = columnId;
}