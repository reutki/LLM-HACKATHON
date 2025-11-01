import os

# Define the path to the images directory
base_path = os.path.join(os.path.dirname(__file__), 'images')

# List of object categories in the required order
categories = ['apples', 'soda_cans', 'mugs', 'cars', 'forks', 'pears']

counts = []

for category in categories:
    category_path = os.path.join(base_path, category)
    if os.path.exists(category_path):
        # Count only files (ignore subdirectories, hidden files)
        num_images = len([
            f for f in os.listdir(category_path)
            if os.path.isfile(os.path.join(category_path, f)) and not f.startswith('.')
        ])
    else:
        num_images = 0
    counts.append(num_images)
    print(f"{category}: {num_images}")

# Form the HIDDEN_WORD by concatenating the counts
hidden_word = ''.join(str(c) for c in counts)
flag = f"SIGMOID_{{{hidden_word}}}"
print("\nFLAG:", flag)
