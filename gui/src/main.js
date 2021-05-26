function startTask () {
    var task = document.getElementById("task").value;
    eel.call_robot(task);
}