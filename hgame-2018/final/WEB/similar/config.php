<?php
error_reporting(E_ERROR | E_WARNING | E_PARSE);
define(BASEDIR, "/var/www/html/");
define(FLAG_SIG, 1);

$DBHOST = "mysql";
$DBUSER = "root";
$DBPASS = "0720";
//$DBPASS = "";
$DBNAME = "hgame";
$mysqli = @new mysqli($DBHOST, $DBUSER, $DBPASS, $DBNAME);
if(mysqli_connect_errno()){
        echo "no sql connection".mysqli_connect_error();
        $mysqli=null;
        die();
}
?>
