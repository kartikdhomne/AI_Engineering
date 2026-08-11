from pydantic import BaseModel, Field, EmailStr, field_validator

class User(BaseModel):
    id: int = Field(gt=0, description="The positive integer id of the user")
    name: str = Field(min_length=3, description="The name of the user", alias="name") # alias for accept camelCase
    email: EmailStr
    age: int = Field(gt=0, lt=200, description="The age of the user")
    is_active: bool = True


    @field_validator("name")
    @classmethod
    def validate_username_must_be_alphanumeric(cls, v:str) -> str :
        if not v.isalnum():
            raise ValueError("Username must be alphanumeric")
        return v.lower()


user = User(id=1, name="JohnDoe123", email="john@example.com", age=25)
print(user)

raw_data = {
    "id": 2,
    "name": "Adam123",
    "email": "adam@example.com",
    "age" : 30,
    "is_active": False
}

# user2 = User(**raw_data)
user2 = User.model_validate(raw_data)
print(user2)