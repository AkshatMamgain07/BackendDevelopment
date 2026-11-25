# Lab Experiments 7 and 8 – JavaScript ES6 To-Do App

## Aim
Build an interactive to-do list using JavaScript ES6 features and DOM event handling. Users can add tasks, mark them complete, and delete them.

## Requirements
- A modern web browser (Chrome, Firefox, Edge, or equivalent)
- A text editor for viewing or changing the source files
- The experiment files: `index.html`, `todo.html`, and `app.js`
- No package installation or Node.js is required

## Files
- `index.html` — experiment overview and instructions; this is the GitHub Pages landing page.
- `todo.html` — page structure and styling for the interactive to-do list.
- `app.js` — task model, rendering, and add, complete, and delete behavior.

## How to Run Locally
1. Download or clone the repository, or copy the `lab/Exp7_8` folder to your computer.
2. Open the `lab/Exp7_8` folder.
3. Open `todo.html` directly in a modern browser. The app runs locally without a server.
4. Alternatively, start a local server from the `lab/Exp7_8` folder with `python -m http.server 8000`, then visit `http://localhost:8000/todo.html` in your browser.

## Procedure / Steps to Perform
1. Open `todo.html` and confirm the page contains a task input, an **Add** button, and an empty task list.
2. In `app.js`, inspect the `Task` class, which creates each task with an ID, title, and completion state.
3. Enter a task and select **Add** (or press **Enter**). Confirm the task appears in the list.
4. Select a task's text to toggle its completed state; confirm completed text is crossed out.
5. Select **Delete** beside a task and confirm it is removed.
6. Try adding several tasks and repeat the complete and delete actions to verify they work independently.
7. Refresh the page and observe that tasks reset because they are stored only in memory.

## Concepts Demonstrated
- ES6 classes and `let`
- Arrow functions, destructuring, and the spread operator
- Array methods (`forEach`, `filter`, and `map`)
- DOM creation and event delegation
- Keyboard and click event listeners

## Expected Result
The browser displays a working to-do list. A task can be added, marked complete, and deleted. Tasks reset after a page refresh.
