const express = require('express');
// const { createPool } = require('mysql');
const mysql = require('mysql');
const apps = express();

const db = mysql.createPool({
    host: "localhost",
    user: "root",
    // port: 42069,
    password: "Lays)Potato15963",
    database: "videogame",
    connectionLimit: 10
})



apps.get("/", (req, res) => {
    const sqlInsert = " USE users_login; INSERT INTO users(email, password) VALUES ('someemail@email.com', 'password');";
    db.query(sqlInsert, (err, result) => {
        res.send("Hello World");
        console.log(sqlInsert)
        console.log(db)
    });
})

apps.listen(42070, () => {
    console.log("running on port 42070");
})