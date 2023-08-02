from github import Github

def create_github_repo(token, repo_name, repo_description=""):
    g = Github(token)
    user = g.get_user()
    repo = user.create_repo(name=repo_name, description=repo_description)
    print(f"Repository '{repo.name}' created successfully!")

# Replace 'YOUR_GITHUB_TOKEN' with your personal access token.
# You can generate a token from your GitHub account settings.
github_token = 'YOUR_GITHUB_TOKEN'

# Replace 'your-repo-name' and 'Your repository description' with desired values.
repository_name = 'your-repo-name'
repository_description = 'Your repository description'

create_github_repo(github_token, repository_name, repository_description)
