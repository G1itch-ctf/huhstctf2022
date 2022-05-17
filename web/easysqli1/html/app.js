const fs = require('fs')
const express = require('express')
const bodyParser = require('body-parser')
const lodash = require('lodash')
const path = require('path');
const connection = require("./db_connect.js");
const { response } = require('express');
const { result } = require('lodash');
const { json } = require('body-parser');

const app = express()
    // app.use(bodyParser.urlencoded({ extended: true })).use(bodyParser.json())

function safe(str) {
    const r = str
        .replace(/[\s#;\-]/g, '')
        .replace(/if|\|\||&&/gi, '')
        .toString();
    return r;
}


app.get("/", function(req, res) {
    var test = req.query.id;


    var conn = connection.getconnection();
    var result = { "result": [] };
    var t = safe(test);
    const sql = `SELECT id,username FROM users order by ` + t;
    conn.query(sql, function(error, results, fields) {
        if (results == undefined) {
            res.json(["error"]);
            return;
        }

        for (i = 0; i < results.length; i++) {
            result["result"].push({ "id": results[i].id, "username": results[i].username })
        }
        res.json(result)
    });
    conn.end();
})

app.listen(3000, () => console.log(`Example app listening on port 3000!`))
