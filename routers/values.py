from fastapi import APIRouter
from schema import Values


router = APIRouter()


@router.post("/add/")
async def add_numbers(numbers: Values, tags=["add_numbers"]):
    output = numbers.num1 + numbers.num2
    return {"result": f"{output}"}
