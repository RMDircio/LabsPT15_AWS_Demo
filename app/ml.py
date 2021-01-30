"""Machine learning functions"""

from fastapi import APIRouter

router = APIRouter()


@router.get('/hello_ML_user')
async def hello_user(name= 'Regina'):
    """Returns a simple greeting 👋"""
    return {'user_name' : f'Hello {name}'}