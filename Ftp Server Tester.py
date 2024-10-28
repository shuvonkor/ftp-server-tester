import requests

def fetch_github_repositories(user):
    """
    Fetches all public repositories of a given GitHub user.

    Parameters:
    user (str): The GitHub username or organization name.

    Returns:
    list: A list of dictionaries containing repository information.
    """
    url = f"https://api.github.com/users/{user}/repos"
    repositories = []

    try:
        # Send a GET request to the GitHub API
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        
        # Parse the JSON response
        data = response.json()
        
        # Loop through each repository and extract details
        for repo in data:
            repo_info = {
                "name": repo["name"],
                "description": repo["description"],
                "url": repo["html_url"],
                "language": repo["language"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"]
            }
            repositories.append(repo_info)
        
        # Output the information
        print(f"Repositories for user '{user}':")
        for repo in repositories:
            print("\nRepository Name:", repo["name"])
            print("Description:", repo["description"])
            print("URL:", repo["url"])
            print("Primary Language:", repo["language"])
            print("Stars:", repo["stars"])
            print("Forks:", repo["forks"])
        
        return repositories

    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")
        return []

# Example usage:
user = input("Enter the GitHub username or organization: ")
fetch_github_repositories(user)
