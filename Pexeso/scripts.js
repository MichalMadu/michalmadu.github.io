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
     if (firstCard.dataset.framework === secondCard.dataset.framework) {
      firstCard.removeEventListener('click', flipCard);
      secondCard.removeEventListener('click', flipCard);
     } else {
       //not a match
       firstCard.classList.remove('flip');
       secondCard.classList.remove('flip');
     }
   }
}

cards.forEach(card => card.addEventListener('click', flipCard));
