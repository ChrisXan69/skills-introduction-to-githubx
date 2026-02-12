# How to Start the GitHub Skills Course

Welcome to the Introduction to GitHub course! 🎉

## ✅ Current Status

The course has been **successfully initiated**. The GitHub Skills automated system has:
- ✅ Created Issue #2 with course instructions
- ✅ Prepared the learning environment
- ✅ Activated GitHub Actions workflows

## 📋 What You'll Learn

In this course you will learn to:
1. Create branches
2. Make commits
3. Open pull requests
4. Merge pull requests

## 🚀 Next Steps - Start Now

To advance to the next step of the course, you need to create a branch called `my-first-branch`:

### Option 1: Using the GitHub Web Interface (Recommended)

1. Open your repository on GitHub (the page where you're viewing this file)

2. Click on the **< > Code** tab in the header menu

3. Find and click on the dropdown menu that says **main** (near the top left corner)

4. In the text box that says **Find or create a branch...**, type exactly:
   ```
   my-first-branch
   ```

5. Click **Create branch: my-first-branch from main**

6. Done! GitHub Actions will detect the new branch and automatically:
   - Verify that the branch was created correctly
   - Post Step 2 instructions in Issue #2
   - Continue guiding you through the course

### Option 2: Using Git Command Line

If you prefer using the terminal:

```bash
# Make sure you're in the repository
cd your-repository  # Replace with your repository name

# Create and switch to the new branch from main
git checkout -b my-first-branch main

# Push the branch to GitHub
git push -u origin my-first-branch
```

## 📚 Useful Resources

- **[Issue #2: Detailed Course Instructions](../../issues/2)** - Check here for complete instructions and progress
- [GitHub Documentation on Branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)
- [Video: What is GitHub?](https://www.youtube.com/watch?v=pBy1zgt0XPc)

## 💡 Important

- This is an **interactive** course that requires manual actions
- Each step you complete will automatically trigger the next one
- GitHub Actions (the "Mona" bot) will comment on Issue #2 with feedback and new instructions
- You don't need to manually close or modify anything - the system does it for you

## ❓ Troubleshooting

If you don't see progress after creating the branch:
1. Wait 20-30 seconds for GitHub Actions to process your action
2. Verify that the branch is named exactly `my-first-branch` (no extra spaces or capital letters)
3. Check the [Actions](../../actions) tab to see if there are running jobs
4. If problems persist, report an issue in the [official course repository](https://github.com/skills/introduction-to-github/issues)

---

Good luck with your GitHub learning journey! 🚀
