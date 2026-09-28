# GitHub Secrets Setup

This guide explains how to configure secrets for running the pipeline in GitHub Actions.

## Why Secrets?

The `.env` file containing `GOOGLE_API_KEY` is gitignored (not committed) for security. When running the pipeline via GitHub Actions or in production, the API key is retrieved from GitHub Secrets instead.

---

## Setup Instructions

### 1. Add GOOGLE_API_KEY to GitHub Secrets

**Step 1:** Go to your repository on GitHub  
**Step 2:** Navigate to **Settings** → **Secrets and variables** → **Actions**  
**Step 3:** Click **New repository secret**  
**Step 4:** 
- **Name:** `GOOGLE_API_KEY`
- **Secret:** Paste your actual Google Gemini API key

**Step 5:** Click **Add secret**

### 2. Local Development (Using .env)

For local testing, create a `.env` file in the project root:

```bash
# .env (NOT committed to git)
GOOGLE_API_KEY=your-actual-key-here
```

Then run:
```bash
python main.py
```

The application will load the key from `.env` automatically.

### 3. GitHub Actions Workflow

If you set up CI/CD in GitHub Actions, reference the secret like this:

```yaml
name: Run AI Digest Pipeline

on:
  schedule:
    - cron: '0 6 * * *'  # Daily at 6 AM UTC
  workflow_dispatch:

jobs:
  pipeline:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run pipeline
        env:
          GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
        run: python main.py
      
      - name: Upload digest artifact
        uses: actions/upload-artifact@v3
        with:
          name: daily-digest
          path: digests/
```

---

## Security Checklist

- [x] `.env` is in `.gitignore` (not committed)
- [x] `.env` is removed from git history (`git rm --cached .env`)
- [x] `GOOGLE_API_KEY` is configured in GitHub Secrets
- [x] `requirements.txt` is pinned (no secrets in dependencies)
- [x] Pipeline code doesn't log or print the API key

---

## Environment Variables

The pipeline reads from:

1. **Local Development:** `.env` file (gitignored)
2. **GitHub Actions:** Repository Secrets (via `${{ secrets.GOOGLE_API_KEY }}`)
3. **System Environment:** `os.environ.get("GOOGLE_API_KEY")`

---

## Troubleshooting

### Error: "GOOGLE_API_KEY environment variable is missing"

**Local Fix:**
1. Create `.env` in project root
2. Add `GOOGLE_API_KEY=your-key`
3. Run: `python main.py`

**GitHub Actions Fix:**
1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Verify `GOOGLE_API_KEY` secret exists
3. Re-run the workflow

### Error: "Invalid API key"

- Verify the key is correct in `.env` or GitHub Secrets
- Check the key hasn't expired or been revoked
- Ensure no extra whitespace in the key

---

## Best Practices

✅ **DO:**
- Store keys in GitHub Secrets for CI/CD
- Use `.env` for local development
- Rotate keys periodically
- Use environment-specific keys (dev, staging, prod)

❌ **DON'T:**
- Commit `.env` to git
- Hardcode API keys in source code
- Share API keys in chat/email
- Use the same key for multiple environments

---

## Support

For issues with GitHub Secrets, see:
- [GitHub Docs: Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Google Gemini API Docs](https://ai.google.dev/docs)
