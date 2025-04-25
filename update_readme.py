import requests

def fetch_striver_sheet_progress():
    # Example: If your progress is stored in a Google Sheet or API
    # Replace with the actual URL or API endpoint
    progress_endpoint = "YOUR_DATA_SOURCE_URL"
    response = requests.get(progress_endpoint)

    if response.status_code == 200:
        data = response.json()  # Modify based on the response format (JSON, CSV, etc.)
        # Extract relevant progress data
        solved = data.get("solved_problems")  # Example key
        total = data.get("total_problems")  # Example key
        return solved, total
    else:
        print("Error fetching data!")
        return None, None

# Example usage
solved, total = fetch_striver_sheet_progress()
print(f"Problems Solved: {solved}/{total}")
