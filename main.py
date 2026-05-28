"""
OpenAI Skills API — Optimized Full Demo

Features:
1. Delete old duplicate skills
2. Upload fresh skill
3. Wait for propagation
4. List skills
5. Use skill with GPT-5.2 + shell tool
6. Cleanup latest skill automatically
"""

import os
import time
from dotenv import load_dotenv
from openai import OpenAI


# ─────────────────────────────────────────────────────────────
# STEP 0: Load Environment Variables
# ─────────────────────────────────────────────────────────────

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY not found in .env")

client = OpenAI(api_key=OPENAI_API_KEY)

print("=" * 70)
print("🚀 OpenAI Skills API — Optimized Demo")
print("=" * 70)


# ─────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────

SKILL_NAME = "data-analyzer"
SKILL_FILE_PATH = "my_skill/SKILL.md"


# ─────────────────────────────────────────────────────────────
# STEP 1: Delete Existing Duplicate Skills
# ─────────────────────────────────────────────────────────────

print("\n🧹 STEP 1: Cleaning old duplicate skills...\n")

existing_skills = client.skills.list()

deleted_count = 0

for existing_skill in existing_skills.data:
    if existing_skill.name == SKILL_NAME:
        try:
            client.skills.delete(existing_skill.id)
            print(f"🗑️ Deleted old skill: {existing_skill.id}")
            deleted_count += 1
        except Exception as e:
            print(f"⚠️ Failed to delete {existing_skill.id}: {e}")

print(f"\n✅ Total old skills deleted: {deleted_count}")


# ─────────────────────────────────────────────────────────────
# STEP 2: Upload Fresh Skill
# ─────────────────────────────────────────────────────────────

print("\n📤 STEP 2: Uploading fresh custom skill...\n")

with open(SKILL_FILE_PATH, "rb") as f:
    skill = client.skills.create(
        files=[
            (
                SKILL_FILE_PATH,
                f,
                "text/markdown",
            )
        ]
    )

skill_id = skill.id

print("✅ Skill uploaded successfully!")
print(f"Skill ID   : {skill_id}")
print(f"Skill Name : {skill.name}")


# ─────────────────────────────────────────────────────────────
# STEP 3: Wait for Skill Propagation
# ─────────────────────────────────────────────────────────────

print("\n⏳ STEP 3: Waiting for skill propagation...\n")

time.sleep(5)


# ─────────────────────────────────────────────────────────────
# STEP 4: Retrieve Skill
# ─────────────────────────────────────────────────────────────

print("📋 STEP 4: Fetching uploaded skill details...\n")

retrieved_skill = client.skills.retrieve(skill_id)

print(f"Retrieved Skill : {retrieved_skill.name}")
print(f"Retrieved ID    : {retrieved_skill.id}")


# ─────────────────────────────────────────────────────────────
# STEP 5: List Current Skills
# ─────────────────────────────────────────────────────────────

print("\n📚 STEP 5: Listing current available skills...\n")

all_skills = client.skills.list()

print(f"{'Skill ID':<45} {'Skill Name'}")
print("-" * 80)

for s in all_skills.data:
    print(f"{s.id:<45} {s.name}")


# ─────────────────────────────────────────────────────────────
# STEP 6: Use Skill with GPT-5.2
# ─────────────────────────────────────────────────────────────

print("\n💬 STEP 6: Using skill with GPT-5.2...\n")

sample_data = """
Monthly Sales Data (2024)

January:   $12,400
February:  $9,800
March:     $15,200
April:     $14,700
May:       $18,300
June:      $16,900
July:      $11,200
August:    $13,500
September: $17,800
October:   $20,100
November:  $22,400
December:  $25,000
"""

response = client.responses.create(
    model="gpt-5.2",
    input=f"""
Analyze the following sales dataset
and provide useful business insights:

{sample_data}
""",
    tools=[
        {
            "type": "shell",
            "environment": {
                "type": "container_auto",
                "skills": [
                    {
                        "type": "skill_reference",
                        "skill_id": skill_id,
                    }
                ],
            },
        }
    ],
)

print("🤖 GPT Response:\n")

if hasattr(response, "output_text"):
    print(response.output_text)
else:
    for item in response.output:
        if hasattr(item, "content"):
            for block in item.content:
                if hasattr(block, "text"):
                    print(block.text)

print(f"\n📊 Response Status: {response.status}")


# ─────────────────────────────────────────────────────────────
# STEP 7: Delete Latest Skill
# ─────────────────────────────────────────────────────────────

print(f"\n🗑️ STEP 7: Deleting latest skill: {skill_id}\n")

client.skills.delete(skill_id)

print("✅ Latest skill deleted successfully!")


# ─────────────────────────────────────────────────────────────
# FINAL VERIFICATION
# ─────────────────────────────────────────────────────────────

print("\n📚 Final Skills Verification...\n")

remaining_skills = client.skills.list()

print(f"{'Skill ID':<45} {'Skill Name'}")
print("-" * 80)

if remaining_skills.data:
    for s in remaining_skills.data:
        print(f"{s.id:<45} {s.name}")
else:
    print("✅ No remaining skills found.")


# ─────────────────────────────────────────────────────────────
# COMPLETED
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("✅ OpenAI Skills API workflow completed successfully.")
print("=" * 70)