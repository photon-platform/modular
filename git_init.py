import subprocess
import sys


def run_command(command):
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    stdout, stderr = process.communicate()
    return stdout.decode().strip(), stderr.decode().strip()


def init_github_repo(repo_name, github_user):
    # Initialize local Git repository
    print("Initializing local Git repository...")
    run_command(f"git init .")

    # Change directory to the new repository
    #  run_command(f"cd {repo_name}")

    #  Create a README file
    #  with open(f"{repo_name}/README.md", "w") as f:
    #  f.write(f"# {repo_name}")

    # Add and commit the README file
    run_command(f"git add *")
    run_command(f"git commit -m 'Initial commit'")

    # Create remote GitHub repository using the GitHub CLI
    print("Creating remote GitHub repository...")
    stdout, stderr = run_command(
        f"gh repo create {github_user}/{repo_name} --public -y"
    )
    if stderr:
        print(stderr)
        sys.exit(1)

    # Set the remote origin for the local Git repository and push
    print("Connecting local and remote repositories...")
    run_command(
        f"git remote add origin https://github.com/{github_user}/{repo_name}.git"
    )
    run_command(f"git branch -M main")
    run_command(f"git push -u origin main")

    print(f"Repository setup complete: https://github.com/{github_user}/{repo_name}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python init_github_repo.py <repository_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    github_user = "photon-platform"  # Replace with your GitHub username
    init_github_repo(repo_name, github_user)
