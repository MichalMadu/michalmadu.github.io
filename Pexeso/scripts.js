const cards = document.querySelectorAll('.memory-card');

function flipCard() {
  console.log('I was clicked!');
}

cards.forEach(card => card.addEventListener('click', flipCard));
