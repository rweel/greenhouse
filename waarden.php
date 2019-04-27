<html>
   <head>
      <title>Greenhouse data</title>
   </head>
   <body>
<?php
$servername = "localhost";
$username = "root";
$password = "fcVolend@m24";
$dbname = "greenhouse";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT ts, temperature, humidity FROM enviroment";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "Datum en tijd: " . $row["ts"]. " - Temperatuur: " . $row["temperature"]. " - Vochtigheid " . $row["humidity"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>
   </body>
</html>