/* const startingMinutes = 10;
let time = startingMinutes * 60;

const countDownEl = document.getElementById('timer');

function startTimer() {
  setInterval(updateTimer, 1000);
}

function updateTimer() {
  const min = Math.floor(time / 60);
  let second = time % 60;

  second = second < startingMinutes ? '0' + second : second;

  countDownEl.innerHTML = `${min}:${second}`;
  time--;
} */

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
  startTimer()
}
