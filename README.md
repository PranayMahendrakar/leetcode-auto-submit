# LeetCode Auto Submitter (Free GitHub Actions)

🚀 **Automatically submit LeetCode solutions using GitHub Actions** - runs continuously on a free schedule with no domain needed!

## What This Does

This project automatically submits a LeetCode solution (Palindrome Number) at regular intervals using GitHub Actions.

- ✅ **Completely Free** - Uses GitHub's free tier (2,000 mins/month for private repos, unlimited for public)
- - ✅ **No Domain Needed** - Runs entirely on GitHub infrastructure
  - - ✅ **No Server Setup** - No VPS, no hosting fees
    - - ✅ **Secure** - Uses GitHub Secrets for credentials
      - - ✅ **Customizable** - Change the schedule or problem anytime
       
        - ## Setup (5 minutes)
       
        - ### Step 1: Get Your LeetCode Credentials
       
        - 1. Login to LeetCode in your browser
          2. 2. Open DevTools (F12) → Application → Cookies → leetcode.com
             3. 3. Find and copy the values for:
                4.    - `csrftoken`
                      -    - `LEETCODE_SESSION`
                       
                           - ### Step 2: Add GitHub Secrets
                       
                           - 1. Go to your repo → **Settings** → **Secrets and variables** → **Actions**
                             2. 2. Click **New repository secret**
                                3. 3. Add these two secrets:
                                  
                                   4. | Secret Name | Value |
                                   5. |---|---|
                                   6. | `LEETCODE_CSRF` | Your CSRF token |
                                   7. | `LEETCODE_SESSION` | Your session cookie |
                                  
                                   8. ### Step 3: Enable GitHub Actions
                                  
                                   9. 1. Go to **Actions** tab in your repo
                                      2. 2. GitHub will automatically find the workflow - enable it
                                        
                                         3. ### Step 4: Run It!
                                        
                                         4. **Automatically:** Runs every 6 hours (edit the cron schedule in `.github/workflows/run.yml` if you want)
                                        
                                         5. **Manually:** Go to Actions tab → "Run LeetCode Submitter" → "Run workflow"
                                        
                                         6. ## How It Works
                                        
                                         7. 1. **GitHub Actions** triggers on a schedule
                                            2. 2. Checks out your code
                                               3. 3. Sets up Python 3.11
                                                  4. 4. Runs `leetcode_submit.py` with your credentials from GitHub Secrets
                                                     5. 5. Submits the solution and checks the result
                                                       
                                                        6. ## Customizing
                                                       
                                                        7. ### Change the Schedule
                                                       
                                                        8. Edit `.github/workflows/run.yml`:
                                                       
                                                        9. ```yaml
                                                           schedule:
                                                             - cron: '0 */6 * * *'   # Every 6 hours
                                                             # - cron: '0 8 * * *'    # Or: Daily at 8 AM UTC
                                                             # - cron: '*/30 * * * *' # Or: Every 30 minutes
                                                           ```

                                                           ### Change the Problem or Solution

                                                           Edit `leetcode_submit.py`:

                                                           ```python
                                                           PROBLEM_SLUG = "two-sum"        # Change problem
                                                           CODE = """your solution here"""  # Change code
                                                           ```

                                                           ## Cost

                                                           Completely free! GitHub includes:
                                                           - **2,000 free minutes/month** for private repos
                                                           - - **Unlimited minutes** for public repos
                                                            
                                                             - This script runs every 6 hours = 4 runs/day × 30 days = 120 runs/month. Each run takes ~30 seconds, so you use ~60 minutes/month. **You'll never hit the limit!**
                                                            
                                                             - ## Troubleshooting
                                                            
                                                             - **Error: "LEETCODE_SESSION is empty"**
                                                             - - Check your GitHub Secrets are set correctly (Settings → Secrets)
                                                              
                                                               - **"Failed to get question_id"**
                                                               - - Your LeetCode session cookie expired
                                                                 - - Update it in GitHub Secrets
                                                                  
                                                                   - **Submission failed**
                                                                   - - Check the Actions tab for error logs
                                                                     - - Make sure your solution code is valid Python
                                                                      
                                                                       - ## Security
                                                                      
                                                                       - ✅ Your credentials are stored in **GitHub Secrets** (encrypted)
                                                                       - ✅ Credentials are never logged or exposed
                                                                       - ✅ Only used during the GitHub Actions run
                                                                       - ✅ No personal data leaves GitHub
                                                                      
                                                                       - ## License
                                                                      
                                                                       - MIT - Free to use and modify!
