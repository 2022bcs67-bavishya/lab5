# Setup Instructions for GitHub Repository

## Step 1: Create GitHub Repository

**You need to do this manually:**

1. Go to https://github.com/new
2. Repository name: `lab2`
3. Owner: `2022bcs67-bavishya` (or your GitHub username)
4. Description: "MLOps Pipeline for Wine Quality Prediction"
5. Make it **Private** (to ensure you're the only contributor)
6. **DO NOT** initialize with README, .gitignore, or license
7. Click "Create repository"

## Step 2: Initialize Git and Push

After creating the repository, run these commands in your terminal:

```powershell
# Navigate to your project directory
cd C:\Users\sanka\OneDrive\Documents\lab2

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: MLOps pipeline with training, API, and Docker"

# Add remote (replace with your actual username if different)
git remote add origin https://github.com/2022bcs67-bavishya/lab2.git

# Push to main branch
git branch -M main
git push -u origin main
```

## Step 3: Verify Repository Settings

1. Go to your repository: https://github.com/2022bcs67-bavishya/lab2
2. Go to Settings → Collaborators
3. Ensure no one else has access (you should be the only contributor)

## Step 4: Configure GitHub Secrets

Follow the instructions in `GITHUB_SECRETS_SETUP.md` to add:
- Docker Hub username
- Docker Hub access token
- GitHub Personal Access Token
- Variables for best F1 and R2 scores

## Notes

- The repository structure is already set up
- All necessary files are in place
- GitHub Actions workflow is configured
- Docker image is already pushed to Docker Hub
