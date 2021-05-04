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
      firstCard.removeEvenListener('click', flipCard);
      secondCard.removeEventListener('click', flipCard);
     }
     console.log("Function has been Executed!");
   }
}

cards.forEach(card => card.addEventListener('click', flipCard));
