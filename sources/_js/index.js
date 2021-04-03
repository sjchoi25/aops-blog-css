const app = require("express")();
const http = require('http');
const server = http.createServer(app);

app.get("/test.css", (req, res) => {
	console.log("test.css requested");
	res.setHeader('Content-Type', 'text/css');
  	res.send("body {color: blue;}");
});

app.get("/wakeup", (req, res) => {
	console.log("Waking server...\nDone.");
	res.send("Waking up...");
})

app.get("/", (req, res) => {
	console.log("Requested");
	res.send("Hey");
})

server.listen(8000, () => {
	console.log("Server online.");
});
