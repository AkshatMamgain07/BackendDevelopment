# Experiment 12(A) – Express.js Routes and EJS

## Aim
Create an Express.js server that demonstrates text, HTML, and JSON responses; route and query parameters; POST requests; and server-rendered EJS pages.

## Requirements
- Node.js and npm
- A modern web browser
- A terminal and text editor
- Dependencies installed with `npm install` (Express and EJS)

## Run Locally
1. Clone or download this repository.
2. Open a terminal in `lab/Exp12_A`.
3. Run `npm install` to install the required packages.
4. Run `npm start` to start the Express server.
5. Open `http://localhost:3000` in a browser. Keep the terminal open while using the app; press `Ctrl+C` to stop the server.

## Steps to Perform
1. Visit `/text`, `/html`, and `/json` to compare response types.
2. Visit `/user/42` and `/product/books/7` to try route parameters.
3. Visit `/search?q=express&page=1&limit=5` to try query parameters.
4. Visit `/calculate?num1=8&num2=2&operation=multiply` to try the calculator route.
5. Visit `/home`, `/users`, and `/profile/42` to view pages rendered from EJS templates.
6. Send POST requests to `/user`, `/register`, and `/login` with JSON or form data using a REST client such as Postman or the VS Code REST Client.


