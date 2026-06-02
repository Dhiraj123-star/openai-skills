import asyncio

from config.settings import (
    SKILL_FILE_PATH,
    SKILL_PROPAGATION_WAIT,
)
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
)

from utils.logger import logger

@retry(
    stop=stop_after_attempt(3),
    wait= wait_exponential(
        multiplier=1,
        min=2,
        max=10,
    ),   
)
async def upload_skill(client):

    logger.info("Uploading skill")

    with open(SKILL_FILE_PATH, "rb") as f:
        skill = await client.skills.create(
            files=[
                (
                    SKILL_FILE_PATH,
                    f,
                    "text/markdown",
                )
            ]
        )

    logger.info(
        f"Skill uploaded: {skill.id}"
    )
    await asyncio.sleep(SKILL_PROPAGATION_WAIT)

    return skill


async def delete_skill(client, skill_id):
    await client.skills.delete(skill_id)