from flask import Flask, request, jsonify
from counter.line_counter import LineCounter

app = Flask(__name__)

@app.route('/count_lines', methods=['POST'])
def count_lines():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    content = request.get_json()

    if 'code' not in content:
        return jsonify({"error": "JSON must contain 'code' key"}), 400

    code = content['code']
    counter = LineCounter()
    num_lines = counter.count_lines(code.splitlines())

    return jsonify({"lines_of_code": num_lines})

if __name__ == '__main__':
    app.run(debug=True)
