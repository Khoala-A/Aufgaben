
<html> 
<head>
<title>Quadratische Gleichung</title>
</head>
<body>

<?php 
echo "<br>";
echo "x² + px + q = 0";
echo "<br>";
echo "<br>";
echo "Lösung: 2x1 = - p/2 ± SQRT (p²/4 - q)";
echo "<br>";
echo "<br>";
echo "Geben Sie bitte p und q ein: ";
?>

<form method= "post" name="Quadratische Gleichung">
<input type="number" step="any" name="p" />
<input type="number" step="any" name="q" />
<input type="submit" value="Berechnen" name='submit'/>
</form>

<?php 
echo "<br>"; 

$p = $_POST["p"];
$q = $_POST["q"];

$wurzel = ($p*$p/4-$q);
$p2 = ($p/2)*(-1);



if($wurzel > 0) {
	echo "Wurzel > 0 => 2 Lösungen";
	echo "<br>";
	echo "x1 = " .$p2. " + " .round(sqrt($wurzel),2). " = " .round((-$p/2)+(sqrt($wurzel)),2);
	echo "<br>";
	echo "x2 = " .$p2. " - " .round(sqrt($wurzel),2). " = " .round((-$p/2)-(sqrt($wurzel)),2);
} elseif($wurzel == 0) {
	echo "Wurzel = 0 => 1 Doppel-Lösung";
	echo "<br>";
	echo "x1 = $p2 + $wurzel = " .round(-$p/2+sqrt($wurzel),2);
	echo "<br>";
	echo "x2 = $p2 - $wurzel = " .round(-$p/2-sqrt($wurzel),2);
} else {
	echo "Wurzel < 0 => 2 komplex konjugierte Lösungen";
	echo "<br>";
	echo "x1 = " .$p2. " +i ".round(sqrt((-1)*$wurzel),2);
	echo "<br>";	
	echo "x2 = " .$p2. " -i ".round(sqrt((-1)*$wurzel),2);
}
echo "<br>";
?>


</body>
</html>