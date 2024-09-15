import json

# Open the JSONL file (assuming it's in JSONL format)
with open('small_math_dataset.json', 'r') as f:
    lines = f.readlines()

# Initialize the transformed data structure
transformed_data = []

# Process each line (each line should be a separate JSON object)
for line in lines:
    item = json.loads(line.strip())  # Load individual JSON objects
    transformed_data.append({
        "conversations": [
            {"role": "system", "content": "MathGPT: your go-to chatbot for solving math problems."},
            {"role": "human", "content": item["prompt"]},  # Question part
            {"role": "gpt", "content": item["completion"]}  # Answer part
        ]
    })

# Save the transformed data to a new JSONL file
with open('math_conversations.jsonl', 'w') as f:
    for entry in transformed_data:
        f.write(json.dumps(entry) + '\n')

print("Transformation complete and saved to math_conversations.jsonl")
