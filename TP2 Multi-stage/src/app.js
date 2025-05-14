let counter = 0;

document.getElementById("increment-btn").addEventListener("click", () => {
  counter++;
  document.getElementById("counter").textContent = counter;
});
