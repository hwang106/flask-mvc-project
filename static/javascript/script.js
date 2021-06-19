let testInput = document.querySelector("#testInputAppend");
let testButton = document.querySelector("#testButton");

testButton.addEventListener("click", (e) => {
    testInput.innerHTML = "Testing 123";
})

