from pydantic import BaseModel


class Words(BaseModel):
    w1: str
    w2: str
