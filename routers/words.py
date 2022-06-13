from fastapi import APIRouter
from schema import Words


router = APIRouter()


@router.post("/joinwords/", tags=["joinwords"])
async def join_words(words: Words):
    output = words.w1 + "-" + words.w2
    print(output)
    return {"result": f"{output}"}
