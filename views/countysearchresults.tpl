<!DOCTYPE html>

<html>
  <head>
    <title>legal.io--case law lookup</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>legal.io--Local Attorney Search</h2>

    <form action="/dolocalattorneysearch" method="POST" state={{state['name']}}>
    <input type="hidden" name="state" value="{{state['abbreviation']}}">
      <b>Select Your County</b>
      <br>
      <select name="county">
      %if state:
        %for county in state['counties']:
          <option value="{{county}}">{{county}}</option>
          <hr>
          <br>
        %end
      %else:
        No results found.<br><br>
        %end
      %end
      </select>

      <br><br>

      <input type="submit" value="Submit">

    </form>
  </body>

</html>
