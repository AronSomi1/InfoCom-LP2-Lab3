
function Submit() {
  var from_addr = document.getElementById('faddr').value;
  var to_addr = document.getElementById('taddr').value;
  var data = {
    "faddr": from_addr,
    "taddr": to_addr,
  }
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      try {
        var resp = this.responseText;
        alert(resp);
      }
      catch (err) {
        alert(this.responseText);
      }
    }
  };
  xhttp.open("POST", "http://127.0.0.1:5002/planner", true);
  xhttp.send(JSON.stringify(data));
  //startTimer()
}
