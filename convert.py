from datasets import load_from_disk

# Load the dataset from the saved folder
dataset = load_from_disk("small_math_dataset_50")

# Save the dataset as a JSON file
dataset.to_json("small_math_dataset_50.json")
