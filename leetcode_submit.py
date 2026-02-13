#!/usr/bin/env python3
"""
LeetCode Solution Submitter - Palindrome Number
Reads credentials from environment variables for security.
"""

import json, time, os
from urllib.request import Request, urlopen
from urllib.error import HTTPError

API = "https://leetcode.com/graphql"
HEADERS = {
      "Content-Type": "application/json",
      "Referer": "https://leetcode.com",
      "Origin": "https://leetcode.com",
      "User-Agent": "Mozilla/5.0",
}

# ============================================================
# COOKIES - Read from environment variables (set in GitHub Secrets)
# ============================================================
CSRF = os.environ.get("LEETCODE_CSRF", "DKtf8TkYjjpOxRcvcBjXY0OmRTg8y85F")
SESSION = os.environ.get("LEETCODE_SESSION", "")
COOKIE = f"csrftoken={CSRF}; LEETCODE_SESSION={SESSION}"

if not SESSION:
      print("⚠️  WARNING: LEETCODE_SESSION is empty. Set it as an environment variable or GitHub Secret.")

# ============================================================
# SOLUTION
# ============================================================
PROBLEM_SLUG = "palindrome-number"
LANGUAGE = "python3"
CODE = """class Solution:
    def isPalindrome(self, x: int) -> bool:
            if x < 0:
                        return False
                                return str(x) == str(x)[::-1]"""

# ============================================================

def gql(query, variables):
      headers = {**HEADERS, "Cookie": COOKIE, "x-csrftoken": CSRF}
      req = Request(API, json.dumps({"query": query, "variables": variables}).encode(),
                    headers, method="POST")
      with urlopen(req) as r:
                return json.loads(r.read())

  def get_question_id(slug):
        q = """query q($titleSlug:String!){question(titleSlug:$titleSlug){
                questionId title titleSlug difficulty}}"""
        return gql(q, {"titleSlug": slug})["data"]["question"]

def submit_solution(slug, question_id):
      url = f"https://leetcode.com/problems/{slug}/submit/"
      payload = json.dumps({"lang": LANGUAGE, "question_id": question_id, "typed_code": CODE}).encode()
      headers = {**HEADERS, "Cookie": COOKIE, "x-csrftoken": CSRF,
                 "Referer": f"https://leetcode.com/problems/{slug}/"}
      req = Request(url, payload, headers, method="POST")
      with urlopen(req) as r:
                return json.loads(r.read())

  def check_result(submission_id):
        url = f"https://leetcode.com/submissions/detail/{submission_id}/check/"
        headers = {**HEADERS, "Cookie": COOKIE, "x-csrftoken": CSRF}
        for _ in range(30):
                  time.sleep(2)
                  req = Request(url, headers=headers)
                  with urlopen(req) as r:
                                result = json.loads(r.read())
                            if result.get("state") == "SUCCESS":
                                          return result
elif result.get("state") not in ("PENDING", "STARTED"):
            return result
        print("  ⏳ Judging...", end="\r", flush=True)
    return {"status_msg": "Timed out"}

def main():
      print("\n=== Submitting: 9. Palindrome Number ===\n")

    info = get_question_id(PROBLEM_SLUG)
    print(f"✅ Problem: {info['questionId']}. {info['title']} [{info['difficulty']}]")

    print("📤 Submitting...")
    resp = submit_solution(PROBLEM_SLUG, info["questionId"])
    sid = resp.get("submission_id")
    if not sid:
              print(f"❌ Failed: {resp}"); return
          print(f"   Submission ID: {sid}")

    print("⏳ Waiting for result...\n")
    result = check_result(sid)

    status = result.get("status_msg", "Unknown")
    print(f"{'='*40}")
    if status == "Accepted":
              print(f"✅ ACCEPTED!")
              print(f"   Runtime: {result.get('status_runtime', '?')}")
              print(f"   Memory:  {result.get('status_memory', '?')}")
else:
          print(f"❌ {status}")
          for k in ("runtime_error", "compile_error"):
                        if result.get(k): print(f"   {result[k]}")

                print(f"\n🔗 https://leetcode.com/submissions/detail/{sid}/")

if __name__ == "__main__":
      main()
