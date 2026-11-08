from flask import Flask, request

app = Flask(__name__)


@app.route("/calculate")
def calculate():
    op = request.args.get("op", type=str)
    arg1 = request.args.get("arg1", type=float)
    arg2 = request.args.get("arg2", type=float)

    if arg1 is None or arg2 is None:
        return "Invalid arguments", 400

    if op == "sum":
        result = arg1 + arg2
    elif op == "subtract":
        result = arg1 - arg2
    elif op == "multiply":
        result = arg1 * arg2
    elif op == "divide":
        if arg2 == 0:
            return "Cannot divide by zero", 400
        result = arg1 / arg2
    else:
        return "Unknown operation", 400

    return str(result)


if __name__ == "__main__":
    app.run(debug=True)