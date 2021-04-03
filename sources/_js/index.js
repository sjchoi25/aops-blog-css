// Code by Nhv24 (github)/player01 (AoPS)/player010 (replit)

const app = require("express")();
const http = require('http');
const server = http.createServer(app);

// Url for testing
app.get("/test.css", (req, res) => {
	console.log("test.css requested");
	res.setHeader('Content-Type', 'text/css');
  	res.send("body {color: blue;}");
});

// Wakeup url
app.get("/wakeup", (req, res) => {
	console.log("Waking server...\nDone.");
	res.send("Waking up...");
})

// Base url
app.get("/", (req, res) => {
	console.log("Requested");
	res.send("Hey");
})

server.listen(8000, () => {
	console.log("Server online.");
});
