import time

from config.settings import (
    SKILL_FILE_PATH,
    SKILL_PROPAGATION_WAIT,
)


def upload_skill(client):
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

    time.sleep(SKILL_PROPAGATION_WAIT)

    return skill


def delete_skill(client, skill_id):
    client.skills.delete(skill_id)