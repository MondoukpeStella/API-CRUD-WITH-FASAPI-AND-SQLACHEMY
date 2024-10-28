from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_all_measurements():
    pass

@router.post("/")
def create_measurement():
    pass

@router.get("/")
def get_measurement():
    pass

@router.put("/")
def update_measurement():
    pass

@router.delete("/")
def delete_measurement():
    pass