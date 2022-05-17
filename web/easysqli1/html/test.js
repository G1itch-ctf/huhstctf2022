var express = require("express");
var bodyParser = require("body-parser");
var app = express();

function safe(str) {
    const r = str
        .replace(/[\s,()#;*\-]/g, '')
        .replace(/^.*(?=union|binary).*$/gi, '')
        .toString();
    return r;
}

// 创建 application/x-www-form-urlencoded 编码解析
var urlencodedParser = bodyParser.urlencoded({ extended: false })
    //post请求
app.post("/post", urlencodedParser, function(req, res) {
    var username = req.body.username;
    sql = `SELECT * FROM auth WHERE username='${safe(username)}' LIMIT 1`;
    res.send(sql);
})

var server = app.listen(8000, function() {
    var host = server.address().address
    var port = server.address().port
    console.log("http://%s:%s", host, port);
})