import time
from config.settings import (
    SKILL_NAME,
    SKILL_FILE_PATH,
    SKILL_PROPAGATION_WAIT

)

def cleanup_old_skills(client):
    existing_skills= client.skills.list()

    deleted_count = 0

    for skill in existing_skills.data:
        if skill.name == SKILL_NAME:
            client.skills.delete(skill.id)
            print(f"Deleted old skill: {skill.id}")
            deleted_count+=1
    
    return deleted_count

def upload_skill(client):
    with open(SKILL_FILE_PATH,"rb") as f:
        skill = client.skills.create(
            files= [
                (
                SKILL_FILE_PATH,
                f,
                "text/markdown",
                )
            ]
        )
    time.sleep(SKILL_PROPAGATION_WAIT)

    return skill


def list_skills(client):
    return client.skills.list()

def delete_skill(client,skill_id):
    return client.skills.delete(skill_id)

