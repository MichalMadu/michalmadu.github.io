fetch('https://ghibliapi.herokuapp.com/films')
  .then(response => {
    return response.json();
})
.then(title => {
    console.log(title);
});
