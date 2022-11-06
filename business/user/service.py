from .repository import UserRepository, UserCreate, User
from ..wallet.repository import WalletRepository, WalletCreate
from sqlalchemy.orm import Session

class UserService():
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)
        self.wallet_repository = WalletRepository(db)
        
    def get_user(self, user_id: int):
        return self.user_repository.get_user(user_id)
    
    def get_user_by_email(self, email: str):
        return self.user_repository.get_user_by_email(email)
    
    def get_users_page(self, skip: int, limit: int):
        return self.user_repository.get_users(skip, limit)
    
    def create_user_with_wallet(self, user: UserCreate):
        user = self.create_user(user)
        self.create_wallet(user.id)
        return user
    
    def create_user(self, user: UserCreate):
        return self.user_repository.create_user(user)
    
    def update_user(self, user: User):
        return self.user_repository.update_user(user)
    
    def delete_user(self, user_id: int):
        return self.user_repository.delete_user(user_id)
    
    def create_wallet(self, user_id: int):
        wallet = WalletCreate(user_id=user_id, balance=0)
        return self.wallet_repository.create_wallet(wallet)

    def add_founds(self, user_id: int, amount: int):
        user = self.user_repository.get_user(user_id)
        wallet = self.wallet_repository.get_wallet_by_user_id(user_id)
        wallet.balance += amount
        return self.wallet_repository.update_wallet(wallet)
