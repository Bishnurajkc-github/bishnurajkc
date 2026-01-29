// Function to perform calculator operations
function calc(op) {
    const a = document.getElementById("a").value;
    const b = document.getElementById("b").value;

    fetch("/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ operation: op, num1: a, num2: b })
    })
    .then(res => res.json())
    .then(data => {
        const resultDiv = document.getElementById("result");
        const historyList = document.getElementById("history");

        // Clear previous result
        resultDiv.innerText = "";

        // Handle errors
        if (data.error) {
            resultDiv.innerText = "Error: " + data.error;
            return;
        }

        // Show result
        if (data.result !== undefined) {
            resultDiv.innerText = "Result: " + data.result;
        }

        // Update history (last 10 items)
        if (data.history) {
            historyList.innerHTML = "";
            data.history.forEach(item => {
                const li = document.createElement("li");
                li.innerText = item;
                historyList.appendChild(li);
            });
        }
    })
    .catch(err => {
        document.getElementById("result").innerText = "Error: " + err;
    });
}
