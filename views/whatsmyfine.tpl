<!DOCTYPE html>

<html>
	<head>
		<title>legal.io--Whats My Fine</title>
		<style type="text/css">
			.label {
				text-align: right;
			}

			.error {
				color: red;
			}
		</style>

	</head>
	<body>
		<h2>legal.io--Whats my Fine</h2>

		<form action="/whatsmyfine" method="POST">
			<b>Enter in your Infraction</b><br>
			<input type="text" name="searchTerm" size="60" value="search term"><br>
			<input type="submit" value="Submit">
		</form>
	</body>
</html>
