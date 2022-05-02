from fastapi import APIRouter


router = APIRouter(
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/health")
async def health_check() -> dict:
    """
    Router for verification of health of service
    :return:
    """
    return {"status": 200, "message": "Hello World!"}
