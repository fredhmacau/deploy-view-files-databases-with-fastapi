from os import write
import shutil
from fastapi import FastAPI,UploadFile,File,responses,status

api=FastAPI()

@api.post("/uploadfile",status_code=status.HTTP_201_CREATED)
async def upload_file(file:UploadFile=File(...)):
    expensions = ["image/jpeg", "image/png"]
    if file.content_type not in expensions:
        return {"error_type":"invalid content type"}
    else:
        with open (f"{file.filename}","wb") as write_file:
            shutil.copyfileobj(file.file,write_file)
        return {"message":"sucess"}


@api.get("/img/{name}")
def img_file(name:str):
    return responses.FileResponse(path=name)