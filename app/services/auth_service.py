from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.security import (
    create_access_token,
    create_refresh_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import TokenResponse
from app.schemas.user import UserCreate

settings = get_settings()


class AuthService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register_user(self, payload: UserCreate) -> User:
        existing_user = self.user_repository.get_by_email(payload.email)

        if existing_user:
            raise ValueError("User with this email already exists")

        hashed_password = hash_password(payload.password)

        return self.user_repository.create(
            name=payload.name,
            email=payload.email,
            hashed_password=hashed_password,
        )

    def login_user(self, email: str, password: str) -> TokenResponse:
        user = self.user_repository.get_by_email(email)

        if not user or not verify_password(password, user.hashed_password):
            raise ValueError("Invalid credentials")

        return TokenResponse(
            access_token=create_access_token(str(user.id)),
            refresh_token=create_refresh_token(str(user.id)),
        )

    def refresh_access_token(self, refresh_token: str) -> TokenResponse:
        try:
            payload = jwt.decode(
                refresh_token,
                settings.jwt_secret_key,
                algorithms=[settings.jwt_algorithm],
            )
        except JWTError as exc:
            raise ValueError("Invalid refresh token") from exc

        token_type = payload.get("type")
        subject = payload.get("sub")

        if token_type != "refresh" or subject is None:
            raise ValueError("Invalid refresh token")

        return TokenResponse(
            access_token=create_access_token(subject),
            refresh_token=create_refresh_token(subject),
        )