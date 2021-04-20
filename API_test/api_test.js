var request = new XMLHttpRequest()

document.write("
                     <table class="w3-table-all">
                      <tr>
                        <th>Title</th>
                        <th>Rate</th>
                       </tr>
                      <tr>");

request.open('GET', 'https://ghibliapi.herokuapp.com/films', true)


fetch('https://ghibliapi.herokuapp.com/films')
  .then(response => {
    return response.json();
})
.then(title => {
    console.log(title);
});
