function calc(op) {
    const a = document.getElementById("a").value;
    const b = document.getElementById("b").value;

    fetch("/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ op, a, b })
    })
    .then(res => res.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = data.error;
            return;
        }

        document.getElementById("result").innerText =
            "Result: " + data.result;

        const history = document.getElementById("history");
        history.innerHTML = "";
        data.history.forEach(item => {
            const li = document.createElement("li");
            li.innerText = item;
            history.appendChild(li);
        });
    });
}

