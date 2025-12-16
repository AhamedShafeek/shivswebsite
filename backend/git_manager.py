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
            error_msg = e.stderr if e.stderr else str(e)
            raise Exception(f"Git command failed: {error_msg}")
        except FileNotFoundError:
            raise Exception("Git is not installed or not in PATH. Please install Git first.")
    
    def is_git_repo(self):
        """Check if current directory is a git repository"""
        try:
            self.run_git_command('git rev-parse --git-dir')
            return True
        except:
            return False
    
    def has_remote(self):
        """Check if repository has a remote configured"""
        try:
            result = self.run_git_command('git remote -v')
            return len(result.strip()) > 0
        except:
            return False
    
    def get_status(self):
        """Get git status"""
        if not self.is_git_repo():
            raise Exception("Not a git repository. Run 'git init' first or use the setup_git.py script.")
        return self.run_git_command('git status')
    
    def add_all(self):
        """Stage all changes"""
        if not self.is_git_repo():
            raise Exception("Not a git repository. Please initialize git first.")
        return self.run_git_command('git add .')
    
    def commit(self, message):
        """Commit changes"""
        if not self.is_git_repo():
            raise Exception("Not a git repository. Please initialize git first.")
        return self.run_git_command(f'git commit -m "{message}"')
    
    def push(self, branch='main'):
        """Push changes to remote"""
        if not self.is_git_repo():
            raise Exception("Not a git repository. Please initialize git first.")
        if not self.has_remote():
            raise Exception("No remote repository configured. Please add a remote first using 'git remote add origin <url>'")
        return self.run_git_command(f'git push origin {branch}')
    
    def has_changes(self):
        """Check if there are uncommitted changes"""
        try:
            status = self.run_git_command('git status --porcelain')
            return len(status.strip()) > 0
        except:
            return False
    
    def commit_and_push(self, message, branch='main'):
        """Add, commit, and push changes"""
        try:
            # Check if git is set up
            if not self.is_git_repo():
                raise Exception("Not a git repository. Please run setup_git.py first or initialize git manually.")
            
            if not self.has_remote():
                raise Exception("No remote repository configured. Please add a remote first.")
            
            # Check if there are any changes first
            if not self.has_changes():
                return "No changes to commit. Working tree is clean."
            
            # Stage all changes
            self.add_all()
            
            # Commit changes
            try:
                commit_result = self.commit(message)
            except Exception as e:
                error_str = str(e).lower()
                if "nothing to commit" in error_str or "working tree clean" in error_str:
                    return "No changes to commit. Working tree is clean."
                raise e
            
            # Push to remote
            try:
                push_result = self.push(branch)
            except Exception as e:
                error_str = str(e).lower()
                if "permission denied" in error_str or "publickey" in error_str:
                    raise Exception("Authentication failed. Please set up SSH keys or switch to HTTPS. See GIT_SETUP_GUIDE.md")
                raise e
            
            return f"✓ Successfully committed and pushed: {message}"
        except Exception as e:
            # More user-friendly error message
            error_msg = str(e)
            error_lower = error_msg.lower()
            
            if "nothing to commit" in error_lower or "working tree clean" in error_lower:
                return "No changes to commit. Working tree is clean."
            elif "permission denied" in error_lower or "publickey" in error_lower:
                return "Authentication failed. Please check GIT_SETUP_GUIDE.md for SSH/HTTPS setup."
            elif "could not resolve host" in error_lower:
                return "Network error. Please check your internet connection."
            
            raise Exception(f"Git operation failed: {error_msg}")
    
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
