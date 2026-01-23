# Lab 4 Quick Start - Step by Step

## ✅ STEP 1: Add GitHub Secrets (DO THIS FIRST!)

**Go to:** https://github.com/2022bcs67-bavishya/lab2/settings/secrets/actions

### Click "New repository secret" and add:

1. **Name:** `DOCKERHUB_USERNAME`
   - **Value:** `2022bcs0067`

2. **Name:** `DOCKERHUB_TOKEN`
   - **Value:** Get from https://hub.docker.com/settings/security
   - Click "New Access Token" → Generate → Copy token

3. **Name:** `GH_PAT`
   - **Value:** Get from https://github.com/settings/tokens
   - Click "Generate new token (classic)" → Select `repo` and `workflow` scopes → Generate → Copy token

## ✅ STEP 2: Verify Secrets

You should see 3 secrets:
- ✅ DOCKERHUB_USERNAME
- ✅ DOCKERHUB_TOKEN  
- ✅ GH_PAT

## ✅ STEP 3: Push Changes

The Docker build workflow is ready. Just push:

```bash
git add .
git commit -m "Add Lab 4: Automated Docker build workflow"
git push origin main
```

## ✅ STEP 4: Verify Automation

After pushing:
1. Go to: https://github.com/2022bcs67-bavishya/lab2/actions
2. You should see "Docker Build and Push" workflow running
3. Check Docker Hub: https://hub.docker.com/r/2022bcs0067/wine-quality-api/tags
4. New image should appear automatically!

## 🎯 What Changed from Lab 3 → Lab 4

| Aspect | Lab 3 | Lab 4 |
|--------|-------|-------|
| Docker build | Manual | ✅ Automated |
| Docker push | Manual | ✅ Automated |
| Deployment trigger | CLI | ✅ GitHub Push |
| Traceability | Weak | ✅ Strong (CI logs + tags) |

**👉 One git push now deploys automatically!**
