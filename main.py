# Sửa từ dòng này:
# from fastapi import Fastapi

# Thành dòng chuẩn xác này:
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Local Test Environment"}