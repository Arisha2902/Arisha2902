import requests

def fetch_leetcode_stats():
    # API Endpoint
    url = "https://leetcode-stats-api.herokuapp.com/arisha2902"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Extract data
        total_solved = data.get("totalSolved", 0)
        easy_solved = data.get("easySolved", 0)
        medium_solved = data.get("mediumSolved", 0)
        hard_solved = data.get("hardSolved", 0)
        acceptance_rate = data.get("acceptanceRate", "0%")
        ranking = data.get("ranking", "N/A")

        return total_solved, easy_solved, medium_solved, hard_solved, acceptance_rate, ranking
    else:
        print("Failed to fetch LeetCode stats!")
        return None

def update_readme(total, easy, medium, hard, rate, rank):
    with open("README.md", "r") as file:
        lines = file.readlines()

    # Update specific section in README
    for i, line in enumerate(lines):
        if "## 🏆 LeetCode Stats" in line:
            lines[i + 2] = f"- **Total Problems Solved**: {total}\n"
            lines[i + 3] = f"- **Easy**: {easy}\n"
            lines[i + 4] = f"- **Medium**: {medium}\n"
            lines[i + 5] = f"- **Hard**: {hard}\n"
            lines[i + 6] = f"- **Acceptance Rate**: {rate}\n"
            lines[i + 7] = f"- **Ranking**: {rank}\n"

    with open("README.md", "w") as file:
        file.writelines(lines)

if __name__ == "__main__":
    stats = fetch_leetcode_stats()
    if stats:
        update_readme(*stats)
