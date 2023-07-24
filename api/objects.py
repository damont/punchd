from pydantic import BaseModel
import hashlib


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    
    @property
    def user_id(self):
        return hashlib.sha256(self.email.encode()).hexdigest()
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

