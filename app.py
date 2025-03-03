from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_data():
    # Expecting a JSON payload with an "input_data" key.
    data = request.get_json()
    input_data = data.get("input_data", [])
    
    # Remove duplicates based on the company name (assumed to be the first element)
    unique_companies = {}
    for company in input_data:
        if company:
            name = company[0]
            if name not in unique_companies:
                unique_companies[name] = company

    # Convert dictionary back to list
    output_data = list(unique_companies.values())

    # Return the output_data as a JSON array directly
    return jsonify(output_data)

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(host='0.0.0.0', port=5000, debug=True)
