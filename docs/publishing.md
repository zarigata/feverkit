# Publish FeverKit to GitHub

**Important:** This package is not yet published to GitHub. Publishing requires an authenticated GitHub identity with repository creation rights. The connected ChatGPT GitHub tool may have write access to existing repos without a create-repository action.

## 1. Choose the owner

- A personal account might be `zarigata`, currently connected to GitHub in ChatGPT.
- `feverdream.dev` is a domain name, not automatically a GitHub username or organization. If you have a FeverDream GitHub organization, select that owner explicitly.

## 2. Create a new, empty public repository

Use the GitHub **New repository** screen at https://github.com/new . Select the intended owner, name it `feverkit`, set **Public**, and do **not** initialize it with a README or license because those are already in this ZIP.

Or on your own authenticated computer with GitHub CLI:

```bash
gh auth status
cd FeverKit
# Publishing is already complete at zarigata/feverkit; these steps are for forks or mirrors
git init -b main
git add .
git commit -m "Initial FeverKit developer arsenal"
gh repo create zarigata/feverkit --public --source=. --remote=origin --push
```

If you used the web UI to create the empty repo, do this instead:

```bash
cd FeverKit
git init -b main
git add .
git commit -m "Initial FeverKit developer arsenal"
git remote add origin https://github.com/zarigata/feverkit.git
git push -u origin main
```

## 3. Verify what was published

Check README rendering, files, `manifest/` JSON, CI results and the clone URL. Confirm that no secrets were accidentally added.

## 4. Use it from Claude Code

Give Claude Code the published URL, and the prompt in `docs/agent-prompt.md`. Repositories do not grant agents special permissions: approval and environment checks still apply.
