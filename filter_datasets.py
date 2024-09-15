from datasets import load_dataset

# Load the dataset from Hugging Face
dataset = load_dataset("higgsfield/school-math-questions")

# Sample 500 questions (or filter based on Grade 5 if applicable)
sampled_dataset = dataset['train'].shuffle(seed=42).select(range(50))

# Save the smaller dataset
sampled_dataset.save_to_disk("small_math_dataset_50")

