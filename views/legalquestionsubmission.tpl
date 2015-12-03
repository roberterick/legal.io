<!DOCTYPE html>

<html>
	<head>
		<title>legal.io--Legal Question Submission</title>
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
		<h2>legal.io--Legal Question Submission</h2>

		<form action="/dolegalquestionsubmission" method="POST">

				<b>Your state</b><br>
					<select name="state">        
						<option value="CA">California</option>
						<option value="OR">Oregon</option>
					</select><br><br>

				<b>Enter in your Question</b><br>
					<p><input type="text" name="userquestion" cols="75" rows="20"></textarea></p>

				<input type="submit" value="Submit">
		</form>
	</body>
</html>
