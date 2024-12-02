def is_safe(report):
    """Determine if a single report is safe based on the given rules."""
    differences = [b - a for a, b in zip(report, report[1:])]
    # Rule 1: Check if differences are all positive or all negative
    all_increasing = all(d > 0 for d in differences)
    all_decreasing = all(d < 0 for d in differences)
    # Rule 2: Check if all differences are between -3 and 3 (inclusive)
    valid_differences = all(-3 <= d <= 3 for d in differences)
    return (all_increasing or all_decreasing) and valid_differences

def is_safe_with_dampener(report):
    """
    Determine if a report is safe, considering the Problem Dampener
    that can remove one level to make it safe.
    """
    if is_safe(report):
        return True
    # Try removing each level and check if the remaining levels are safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

# Get the file name from the uploaded file
file_name = list(uploaded.keys())[0]

# Read the file
with open(file_name, 'r') as file:
    lines = file.readlines()

# Process each line
safe_count = 0
for line in lines:
    report = list(map(int, line.split()))
    if is_safe_with_dampener(report):
        safe_count += 1

print(f"Number of safe reports with Problem Dampener: {safe_count}")