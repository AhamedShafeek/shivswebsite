import subprocess
import os

class GitManager:
    def __init__(self):
        # Set the repository path to the parent directory of backend
        self.repo_path = os.path.join(os.path.dirname(__file__), '..')
    
    def run_git_command(self, command):
        """Execute a git command"""
        try:
            result = subprocess.run(
                command,
                cwd=self.repo_path,
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise Exception(f"Git command failed: {e.stderr}")
    
    def get_status(self):
        """Get git status"""
        return self.run_git_command('git status')
    
    def add_all(self):
        """Stage all changes"""
        return self.run_git_command('git add .')
    
    def commit(self, message):
        """Commit changes"""
        return self.run_git_command(f'git commit -m "{message}"')
    
    def push(self, branch='main'):
        """Push changes to remote"""
        return self.run_git_command(f'git push origin {branch}')
    
    def commit_and_push(self, message, branch='main'):
        """Add, commit, and push changes"""
        try:
            # Stage all changes
            self.add_all()
            
            # Commit changes
            commit_result = self.commit(message)
            
            # Push to remote
            push_result = self.push(branch)
            
            return f"Successfully committed and pushed: {message}"
        except Exception as e:
            # If commit fails because there are no changes, that's okay
            if "nothing to commit" in str(e):
                return "No changes to commit"
            raise e
    
    def pull(self, branch='main'):
        """Pull changes from remote"""
        return self.run_git_command(f'git pull origin {branch}')
    
    def get_current_branch(self):
        """Get current branch name"""
        return self.run_git_command('git branch --show-current').strip()
    
    def has_changes(self):
        """Check if there are uncommitted changes"""
        status = self.get_status()
        return "nothing to commit" not in status
