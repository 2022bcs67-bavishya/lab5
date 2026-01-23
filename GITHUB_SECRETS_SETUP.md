# GitHub Repository Secrets and Variables Setup Guide

This guide will help you configure the required GitHub repository secrets and variables for your MLOps pipeline.

## Required Secrets

### 1. Docker Hub Username
- **Secret Name:** `DOCKER_HUB_USERNAME`
- **Value:** `2022bcs0067` (or `2022BCS0067` - your Docker Hub username)

### 2. Docker Hub Access Token
- **Secret Name:** `DOCKER_HUB_TOKEN`
- **How to get it:**
  1. Go to https://hub.docker.com/settings/security
  2. Click "New Access Token"
  3. Give it a name (e.g., "GitHub Actions")
  4. Set permissions to "Read, Write, Delete"
  5. Copy the token (you'll only see it once!)
  6. Use this token as the value

### 3. GitHub Personal Access Token
- **Secret Name:** `GITHUB_TOKEN` (or `GH_PAT`)
- **How to get it:**
  1. Go to https://github.com/settings/tokens
  2. Click "Generate new token" → "Generate new token (classic)"
  3. Give it a name (e.g., "MLOps Pipeline")
  4. Select scopes:
     - `repo` (full control of private repositories)
     - `workflow` (update GitHub Action workflows)
  5. Click "Generate token"
  6. Copy the token immediately (you won't see it again!)
  7. Use this token as the value

## Required Variables (for tracking best scores)

### 4. Best F1 Score Variable
- **Variable Name:** `BEST_F1_SCORE`
- **Initial Value:** `0.0`
- **Type:** Variable (not Secret)

### 5. Best R2 Score Variable
- **Variable Name:** `BEST_R2_SCORE`
- **Initial Value:** `0.0`
- **Type:** Variable (not Secret)

## How to Add Secrets and Variables

### Steps:

1. **Go to your GitHub repository**
   - Navigate to: `https://github.com/YOUR_USERNAME/YOUR_REPO`

2. **Open Settings**
   - Click on "Settings" tab in your repository

3. **Navigate to Secrets and Variables**
   - In the left sidebar, click "Secrets and variables" → "Actions"

4. **Add Secrets:**
   - Click "New repository secret"
   - Enter the secret name (e.g., `DOCKER_HUB_USERNAME`)
   - Enter the secret value
   - Click "Add secret"
   - Repeat for all secrets

5. **Add Variables:**
   - Click on the "Variables" tab
   - Click "New repository variable"
   - Enter the variable name (e.g., `BEST_R2_SCORE`)
   - Enter the initial value (e.g., `0.0`)
   - Click "Add variable"
   - Repeat for all variables

## Summary of What to Add

### Secrets (click "New repository secret"):
- `DOCKER_HUB_USERNAME` = `2022bcs0067`
- `DOCKER_HUB_TOKEN` = (your Docker Hub access token)
- `GITHUB_TOKEN` = (your GitHub Personal Access Token)

### Variables (click "Variables" tab → "New repository variable"):
- `BEST_F1_SCORE` = `0.0`
- `BEST_R2_SCORE` = `0.0`

## Verification

After adding all secrets and variables, you should see:
- **3 secrets** in the Secrets tab
- **2 variables** in the Variables tab

## Usage in Workflows

These will be used in your GitHub Actions workflows like:
```yaml
env:
  DOCKER_HUB_USERNAME: ${{ secrets.DOCKER_HUB_USERNAME }}
  DOCKER_HUB_TOKEN: ${{ secrets.DOCKER_HUB_TOKEN }}
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  BEST_R2_SCORE: ${{ vars.BEST_R2_SCORE }}
  BEST_F1_SCORE: ${{ vars.BEST_F1_SCORE }}
```

## Important Notes

⚠️ **Never commit secrets to your repository!** Always use GitHub Secrets.
⚠️ **Docker Hub tokens expire** - you may need to regenerate them periodically.
⚠️ **GitHub tokens** should have minimal required permissions for security.
