from google.colab import files

# Upload the file
uploaded = files.upload()

file_path = "filename.txt"  # Replace with your file path


def calculate_similarity_score(file_path):
    from collections import Counter

    # Read the file and parse data
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Split lines into two lists
    left_list = []
    right_list = []
    for line in lines:
        # Attempt to parse each line; skip invalid ones
        try:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
        except ValueError:
            # Print a warning if a line is skipped (optional)
            print(f"Skipped invalid line: {line.strip()}")

    # Count occurrences in the right list
    right_count = Counter(right_list)

    # Calculate similarity score
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_count.get(num, 0)

    return similarity_score


# Calculate and print the score
score = calculate_similarity_score(file_path)
print(f"Similarity Score: {score}")
