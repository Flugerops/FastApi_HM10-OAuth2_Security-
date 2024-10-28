from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import app
from ..utils import oauth2_scheme, get_current_user, hash_pwd
from ..db import User, AsyncDB


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return {"current_user": current_user}


@app.post("/token")
async def login(
    form: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[Session, Depends(AsyncDB.get_session)],
):
    print(form.username)
    user = session.scalar(select(User).where(User.username == form.username))
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    hashed_password = hash_pwd(form.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=402, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}
