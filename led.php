<?php


//echo exec("whoami");

//$x = $_POST["x"];
//$y = $_POST["y"];

//$data = json_decode($_POST["data"]);;
$data = $_POST["data"];
$brightness = $_POST["brightness"];

var_dump($data);




echo exec ("sudo /var/www/html/led.py '$data' $brightness");
//echo exec ("sudo /var/www/html/led.py $x $y");

//var_dump($_POST);
