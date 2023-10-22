const flipButton = document.querySelector("#flip-button");
const resultElement = document.querySelector("#result");

flipButton.addEventListener("click", () => {
  const result = Math.random();
  if (result < 0.5) {
    resultElement.innerHTML = `<img src="heads.jpeg" alt="Heads" />`;
  } else {
    resultElement.innerHTML = `<img src="tails.jpeg" alt="Tails" />`;
  }
});