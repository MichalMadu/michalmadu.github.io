var request = new XMLHttpRequest()

request.open('GET', 'https://ghibliapi.herokuapp.com/films', true)
request.onload = function () {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response)

  if (request.status >= 200 && request.status < 400) {
    data.forEach((movie) => {
      document.write("
                     <table class="w3-table-all">
                      <tr>
                        <th>Title</th>
                        <th>Rate</th>
                       </tr>
                      <tr>");
                     
      document.write("Title: ");
      document.write(movie.title);
      document.write(", Rate: ");
      document.write(movie.rt_score);
      document.write("%,<br>")
    })
  } else {
    console.log('error')
  }
}

request.send()
