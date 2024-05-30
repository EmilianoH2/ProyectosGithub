document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('todo-form');
    const newTaskInput = document.getElementById('new-task');
    const tasksList = document.getElementById('tasks');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const taskText = newTaskInput.value.trim();
        if (taskText) {
            addTask(taskText);
            newTaskInput.value = '';
            newTaskInput.focus();
        }
    });

    function addTask(taskText) {
        const li = document.createElement('li');
        li.textContent = taskText;

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.addEventListener('click', () => {
            tasksList.removeChild(li);
        });

        li.appendChild(deleteButton);
        tasksList.appendChild(li);

        li.addEventListener('click', () => {
            li.classList.toggle('completed');
        });
    }
});
