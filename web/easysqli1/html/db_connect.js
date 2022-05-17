const mysql = require('mysql');

const db = {
    "getconnection": function() {
        var connection = mysql.createConnection({
            host: 'localhost',
            user: 'root',
            password: 'pcs1.1.2.3',
            database: 'orderbysql'
        });
        connection.connect(function(err) {
            if (err) throw err;

        });
        return connection;
    }
}

module.exports = db