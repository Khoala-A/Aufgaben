
<html> 
<head>
<title>Umfang</title>
</head>
<body>

<?php 
echo "Bitte geben Sie den Durchmesser ein: ";
?>

<form method= "post" name="Umfang">
<input type="text" name="variable1" />
<input type="submit"/>
</form>

<?php 
echo "Der Umfang beträgt: ";
$variable1 = $_POST["variable1"];
$umfang = $variable1*pi();
echo round($umfang,2);
?>


</body>
</html>