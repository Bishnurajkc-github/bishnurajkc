from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

history = []

@app.route("/")
def calculator():
    return render_template("calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    op = data.get("op")
    a = float(data.get("a", 0))
    b = float(data.get("b", 0))

    try:
        if op == "add":
            result = a + b
            text = f"{a} + {b} = {result}"
        elif op == "sub":
            result = a - b
            text = f"{a} - {b} = {result}"
        elif op == "mul":
            result = a * b
            text = f"{a} × {b} = {result}"
        elif op == "div":
            if b == 0:
                return jsonify({"error": "Cannot divide by zero"})
            result = a / b
            text = f"{a} ÷ {b} = {result}"
        elif op == "sqrt":
            result = math.sqrt(a)
            text = f"√{a} = {result}"
        else:
            return jsonify({"error": "Invalid operation"})

        history.append(text)
        return jsonify({"result": result, "history": history[-5:]})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run()
