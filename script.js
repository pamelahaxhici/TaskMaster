document.addEventListener("DOMContentLoaded", function() {
    const taskInput = document.getElementById("task-input");
    const addButton = document.getElementById("add-button");
    const taskList = document.getElementById("task-list");
    const doneButton = document.getElementById("done-button");
    const deleteButton = document.getElementById("delete-button");
    const viewStatsButton = document.getElementById("view-stats-button");

    let taskId = 1; // Initialize task ID counter

    addButton.addEventListener("click", function() {
        const taskText = taskInput.value.trim();
        if (taskText) {
            const li = document.createElement("li");
            li.textContent = `${taskId}. ${taskText}`; // Add task ID to task text
            taskList.appendChild(li);
            taskInput.value = "";
            taskId++; // Increment task ID counter
        }
    });

    taskList.addEventListener("click", function(event) {
        if (event.target.tagName === "LI") {
            event.target.classList.toggle("selected");
        }
    });

    doneButton.addEventListener("click", function() {
        const selectedItems = taskList.querySelectorAll(".selected");
        selectedItems.forEach(item => {
            item.classList.toggle("done");
            item.classList.remove("selected");
        });
    });

    deleteButton.addEventListener("click", function() {
        const selectedItems = taskList.querySelectorAll(".selected");
        selectedItems.forEach(item => item.remove());
    });

    viewStatsButton.addEventListener("click", function() {
        const doneItems = taskList.querySelectorAll(".done");
        const totalTasks = taskList.children.length;
        const completedTasks = doneItems.length;
        const message = `Total tasks: ${totalTasks}\nCompleted tasks: ${completedTasks}`;
        alert(message);
    });
});
