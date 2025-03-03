from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_data():
    data = request.get_json()
    input_data = data.get("input_data", [])
    
    # Remove duplicates based on the company name.
    # Skip entries that are empty or have an empty company name.
    unique_companies = {}
    for company in input_data:
        # Ensure company is a list, has elements, and its first element (name) is a non-empty string.
        if isinstance(company, list) and company and isinstance(company[0], str) and company[0].strip():
            name = company[0].strip()
            if name not in unique_companies:
                unique_companies[name] = company
        else:
            # Skip empty or malformed entries.
            continue

    output_data = list(unique_companies.values())
    return jsonify(output_data)

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(host='0.0.0.0', port=5000, debug=True)
