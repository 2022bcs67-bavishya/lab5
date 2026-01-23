# Lab 4 Setup Guide - Automated Docker Build & Push

## 🔶 TASK 1: SECRETS & CONFIGURATION

This task is **MANDATORY**. CI/CD will **FAIL** without this.

### ✅ Step 1: Repository Setup

You're using the same repo: `https://github.com/2022bcs67-bavishya/lab2`

### ✅ Step 2: Add GitHub Secrets

**Go to:** `https://github.com/2022bcs67-bavishya/lab2/settings/secrets/actions`

#### 🔐 Add Repository Secrets

Click **"New repository secret"** for each:

| Secret Name | Value | How to Get |
|------------|-------|------------|
| `DOCKERHUB_USERNAME` | `2022bcs0067` | Your Docker Hub username |
| `DOCKERHUB_TOKEN` | (token) | See instructions below |
| `GH_PAT` | (token) | See instructions below |

### 📌 How to Get Docker Hub Token

1. Go to: https://hub.docker.com/settings/security
2. Click **"New Access Token"**
3. Token description: `GitHub Actions`
4. Permissions: **Read, Write, Delete**
5. Click **"Generate"**
6. **Copy the token immediately** (you'll only see it once!)
7. Paste it as the value for `DOCKERHUB_TOKEN`

⚠️ **Important:** Docker Hub token ≠ password. You must generate a new access token.

### 📌 How to Get GitHub Personal Access Token (GH_PAT)

1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Token name: `Lab 4 MLOps Pipeline`
4. Select scopes:
   - ✅ `repo` (full control of private repositories)
   - ✅ `workflow` (update GitHub Action workflows)
5. Click **"Generate token"**
6. **Copy the token immediately** (you won't see it again!)
7. Paste it as the value for `GH_PAT`

### ✅ Step 3: Verify Secrets

After adding all secrets, you should see:
- ✅ `DOCKERHUB_USERNAME`
- ✅ `DOCKERHUB_TOKEN`
- ✅ `GH_PAT`

## 🔶 TASK 2: Automated Docker Workflow

The workflow file `.github/workflows/docker-build.yml` has been created. It will:
- ✅ Automatically build Docker image on push
- ✅ Push to Docker Hub
- ✅ Tag with commit SHA for traceability

## What Happens Next

When you push to the repository:
1. Training workflow runs (existing)
2. Docker build workflow runs (new)
3. Docker image is automatically built and pushed to Docker Hub
4. Image is tagged with commit SHA for traceability

## Verification

After pushing, check:
- GitHub Actions tab: https://github.com/2022bcs67-bavishya/lab2/actions
- Docker Hub: https://hub.docker.com/r/2022bcs0067/wine-quality-api/tags
