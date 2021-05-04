const cards = document.querySelectorAll('.memory-card');

let hasFlippedCard = false;
let firstCard, secondCard;

function flipCard() {
  this.classList.toggle('flip');
  
  if (!hasFlippedCard) {
    // first click
    hasFlippedCard = true;
    firstCard = this; 
   } else {
     // second card
     hasFlippedCard = false;
     secondCard = this;
     
     // Do cards match?
     console.log(firstCard.dataset.framework);
     console.log(secondCard.dataset.framework);
     
   }
}

cards.forEach(card => card.addEventListener('click', flipCard));
