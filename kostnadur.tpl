<!DOCTYPE html>
<html>
<head>
	<title>Kostnadur</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="static/css.css">
</head>
<body>
<h1>Skráningarform</h1>
<form action="/kostnadur2" method="post" accept-charset="ISO-8859-1">
	Nafnið:<br>
	<input type="text" name="nafn" required><br>
	Heimilisfang:<br>
	<input type="text" name="hf" required><br>
	Netfang:<br>
	<input type="email" name="mail" required><br>
	Símanúmer:<br>
	<input type="tel" name="simi" required><br>
	Password:<br>
	<input type="Password" name="psw" placeholder="minnsta lagi 8" min="8" required><br>
	<br><br>
	<input type="submit" value="notandi">
</body>
</html>