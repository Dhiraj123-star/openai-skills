from openai import OpenAI

from config.settings import OPENAI_API_KEY
from data.sample_data import SALES_DATA
from services.skill_service import (
    cleanup_old_skills,
    upload_skill,
    list_skills,
    delete_skill,
)

from services.response_service import analyze_sales_data
from utils.logger import print_banner

print("OPENAI Skills API - Production Demo ")

client = OpenAI(api_key= OPENAI_API_KEY)

# cleanup 
print("Cleaning old skills.....\n")

deleted = cleanup_old_skills(client)

print(f"Deleted skills: {deleted}")

# upload
print("Uploading skill .....\n")

skill = upload_skill(client)

print(f"Uploaded skill: {skill.id}")

# list 
print("Listing skills .....\n")

skills = list_skills(client)

for s in skills.data:
    print(f"{s.id} -> {s.name}")

# Analyse 
print("Running GPT Analysis ....\n")

response = analyze_sales_data (
    client = client,
    skill_id = skill.id,
    sample_data = SALES_DATA,
)

print(response.output_text)

# Cleanup
print("\n Cleaning latest skill....\n")

delete_skill(client,skill.id)

print("Done!!!")