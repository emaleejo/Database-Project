<?php
$host="softwaredb.cqj4mkbkulv0.us-east-2.rds.amazonaws.com";
$port=3306;
$socket="";
$user="admin";
$password="testpassword";
$dbname="tester";

// Creating connection
$con = new mysqli($host, $user, $password, $dbname, $port, $socket)
    // Checking connection
	or die ('Could not connect to the database server' . mysqli_connect_error());

//$con->close();

$query = "";

if ($stmt = $con->prepare($query)) {
    $stmt->execute();
    $stmt->bind_result($field1, $field2);
    while ($stmt->fetch()) {
        //printf("%s, %s\n", $field1, $field2);
    }
    $stmt->close();
}