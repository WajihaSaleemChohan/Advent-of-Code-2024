from google.colab import files
uploaded = files.upload()

# Function to check if a report is safe
def is_safe(report):
    """Determine if a single report is safe based on the given rules."""
    differences = [b - a for a, b in zip(report, report[1:])]
    # Rule 1: Check if differences are all positive or all negative
    all_increasing = all(d > 0 for d in differences)
    all_decreasing = all(d < 0 for d in differences)
    # Rule 2: Check if all differences are between -3 and 3 (inclusive)
    valid_differences = all(-3 <= d <= 3 for d in differences)
    return (all_increasing or all_decreasing) and valid_differences

# Read the file
file_name = list(uploaded.keys())[0]  # Get the uploaded file name
with open(file_name, 'r') as file:
    lines = file.readlines()

# Process each line
safe_count = 0
for line in lines:
    report = list(map(int, line.split()))
    if is_safe(report):
        safe_count += 1

print(f"Number of safe reports: {safe_count}")
