from pydantic import BaseModel

class TransactionBase(BaseModel):
    item_id: int
    buyer_id: int
    seller_id: int
    price: int
    balance: int


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True