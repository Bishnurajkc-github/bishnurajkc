// Keep a global history array
let history = [];

// Calculator function
function calc(op) {
    const a = parseFloat(document.getElementById("a").value);
    const b = parseFloat(document.getElementById("b").value);
    let result;

    // Perform operation
    if (op === "add") result = a + b;
    else if (op === "subtract") result = a - b;
    else if (op === "multiply") result = a * b;
    else if (op === "divide") result = b !== 0 ? a / b : "Cannot divide by zero!";
    else if (op === "power") result = a ** b;
    else if (op === "sqrt") result = a >= 0 ? Math.sqrt(a) : "Invalid input";

    // Show result
    document.getElementById("result").innerText = "Result: " + result;

    // ✅ Update history if result is a number
    if (!isNaN(result)) {
        history.push(`${op}(${a}, ${b}) = ${result}`);
        if (history.length > 10) history.shift(); // Keep only last 10 results

        // Render history on page
        const historyList = document.getElementById("history");
        historyList.innerHTML = "";
        history.forEach(item => {
            const li = document.createElement("li");
            li.innerText = item;
            historyList.appendChild(li);
        });
    }
}

// Clear function
function clearCalculator() {
    document.getElementById("a").value = "";
    document.getElementById("b").value = "";
    document.getElementById("result").innerText = "";

    const historyList = document.getElementById("history");
    historyList.innerHTML = "";

    // Clear JS history array
    history = [];
}
