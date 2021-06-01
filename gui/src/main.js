function startTask () {
    var task = document.getElementById("task").value;
    alert(task);
    eel.call_robot(task);
}