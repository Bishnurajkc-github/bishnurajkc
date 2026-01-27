from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# Global memory and history
memory = 0
history = []

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Calculator page
@app.route('/calculator')
def calculator_page():
    return render_template('calculator.html', memory=memory, history=history)

# API endpoint for calculations
@app.route('/calculate', methods=['POST'])
def calculate():
    global memory, history

    data = request.json
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')
    result = None

    try:
        # Convert inputs to float if present
        if num1 is not None:
            num1 = float(num1)
        if num2 is not None:
            num2 = float(num2)

        # BASIC OPERATIONS
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Cannot divide by zero!'})
            result = num1 / num2
        elif operation == 'power':
            result = num1 ** num2
        elif operation == 'percentage':
            result = (num1 * num2) / 100
            history.append(f"{num2}% of {num1} = {result}")
            return jsonify({'result': result, 'history': history[-10:]})

        # SCIENTIFIC OPERATIONS
        elif operation == 'sqrt':
            if num1 >= 0:
                result = math.sqrt(num1)
            else:
                return jsonify({'error': 'Cannot calculate square root of negative number!'})
        elif operation == 'sin':
            result = math.sin(math.radians(num1))
        elif operation == 'cos':
            result = math.cos(math.radians(num1))
        elif operation == 'tan':
            result = math.tan(math.radians(num1))
        elif operation == 'log':
            if num1 > 0:
                result = math.log(num1)
            else:
                return jsonify({'error': 'Cannot calculate log of non-positive number!'})
        elif operation == 'exp':
            result = math.exp(num1)
        elif operation == 'factorial':
            if num1 >= 0 and num1.is_integer():
                result = math.factorial(int(num1))
            else:
                return jsonify({'error': 'Factorial requires non-negative integer!'})

        # MEMORY OPERATIONS
        elif operation == 'memory_store':
            memory = num1
            return jsonify({'message': f'Saved {num1} to memory', 'memory': memory})
        elif operation == 'memory_recall':
            return jsonify({'result': memory, 'memory': memory})
        elif operation == 'memory_clear':
            memory = 0
            return jsonify({'message': 'Memory cleared', 'memory': memory})

        # CONVERTERS
        elif operation == 'km_to_miles':
            result = num1 * 0.621371
        elif operation == 'kg_to_pounds':
            result = num1 * 2.20462
        elif operation == 'm_to_feet':
            result = num1 * 3.28084
        elif operation == 'l_to_gallon':
            result = num1 * 0.264172
        elif operation == 'usd_to_inr':
            result = num1 * 83.0
        elif operation == 'eur_to_inr':
            result = num1 * 90.0
        elif operation == 'c_to_f':
            result = (num1 * 9/5) + 32
        elif operation == 'f_to_c':
            result = (num1 - 32) * 5/9

        # FINANCE TOOLS
        elif operation == 'tip':
            tip_percent = float(data.get('tip_percent', 15))
            tip = num1 * (tip_percent / 100)
            total = num1 + tip
            history.append(f"Tip: ₹{num1} + {tip_percent}% = ₹{total}")
            return jsonify({'tip': tip, 'total': total, 'history': history[-10:]})
        elif operation == 'bmi':
            height = float(data.get('height', 1.7))
            if height <= 0:
                return jsonify({'error': 'Height must be positive!'})
            result = num1 / (height ** 2)
            history.append(f"BMI: {num1}kg/{height}m = {result:.2f}")
            return jsonify({'result': result, 'history': history[-10:]})

        # HISTORY
        elif operation == 'get_history':
            return jsonify({'history': history[-10:]})
        elif operation == 'clear_history':
            history.clear()
            return jsonify({'message': 'History cleared', 'history': []})

        else:
            return jsonify({'error': 'Invalid operation!'})

        # Store in history
        if operation in ['add', 'subtract', 'multiply', 'divide', 'power']:
            op_symbol = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/', 'power': '^'}[operation]
            history.append(f"{num1} {op_symbol} {num2} = {result}")
        elif operation == 'sqrt':
            history.append(f"√{num1} = {result}")
        elif operation in ['sin', 'cos', 'tan']:
            history.append(f"{operation}({num1}°) = {result}")
        elif operation == 'log':
            history.append(f"log({num1}) = {result}")
        elif operation == 'exp':
            history.append(f"exp({num1}) = {result}")
        elif operation == 'factorial':
            history.append(f"{int(num1)}! = {result}")
        elif 'to_' in operation:
            conv_name = operation.replace('_to_', ' → ').replace('_', ' ')
            history.append(f"{num1} {conv_name} = {result}")

        return jsonify({'result': result, 'history': history[-10:], 'memory': memory})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()
