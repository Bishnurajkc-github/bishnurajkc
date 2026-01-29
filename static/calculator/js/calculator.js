function calc(op) {
    const a = parseFloat(document.getElementById("a").value);
    const b = parseFloat(document.getElementById("b").value);
    let result;

    if (op === "add") result = a + b;
    else if (op === "subtract") result = a - b;
    else if (op === "multiply") result = a * b;
    else if (op === "divide") result = b !== 0 ? a / b : "Cannot divide by zero!";
    else if (op === "power") result = a ** b;
    else if (op === "sqrt") result = a >= 0 ? Math.sqrt(a) : "Invalid input";

    document.getElementById("result").innerText = "Result: " + result;
}
