const express = require("express");
const ejs = require("ejs");

const config = require("./config");

const { port } = config;

const app = express();

// app("view engine", "ejs");

// app.use(function logger(req, res, next) {
//   console.log(req.method+" "+ req.path +" - "+ req.ip);
//   ejs.renderFile("index.ejs", {}, {}, function(err, template) {
//     if(err) {
//       res.err("err "+err);
//     } else {
//       res.end(template);
//     }
//   });
//   next();
// });

app.get("/", function(req, res) {
  ejs.renderFile("index.ejs", {}, {}, function(err, template) {
    if(err) {
      res.err("err "+err);
    } else {
      res.end(template);
    }
  });
});

app.listen(port, function(error) {
  if(error) {throw error;}
  console.info("express app runs or port "+port);
});