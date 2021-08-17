<html>

<h1> PHP </h1>

<?php
   try 
   {
       /*** connect to SQLite database ***/
   
       $dbh = new PDO("sqlite:db.sqlite3");
       echo "Handle has been created ......";
   
   }
   catch(PDOException $e)
   {
       echo "Database -- NOT -- loaded successfully .. ";
       die("Query Closed !!! $error");
   }
   
   echo "Database loaded successfully ...."
?>

</html>