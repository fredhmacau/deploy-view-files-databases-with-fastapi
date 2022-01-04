from fastapi import FastAPI, status, File, UploadFile, HTTPException
from fastapi.responses import Response
from starlette.middleware.cors import CORSMiddleware
from schema_db import db
import io


api = FastAPI()
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

@api.on_event("startup")
async def init():
    await db.connect()


@api.get("/")
def index():
    return


@api.post("/img", status_code=status.HTTP_201_CREATED, tags=["img"])
async def img_upload(img: UploadFile = File(...)):
    extensions = ["image/jpeg", "image/png"]
    if img.content_type not in extensions:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="file with content_type invalid",
        )
    else:
        query = (
            "INSERT INTO imgs(name,img,content_type) VALUES (:name,:img,:content_type)"
        )
        try:
            await db.execute(
                query=query,
                values={
                    "name": img.filename,
                    "img": await img.read(),
                    "content_type": img.content_type,
                },
            )
            return {"message": "success"}
        except Exception as exc:
            return {"message": "occurred error in proccess image", "error": f"{exc}"}


@api.get("/img/{name}", status_code=status.HTTP_200_OK, tags=["img"])
async def get_img(name: str):
    query = "SELECT name,img,content_type FROM imgs WHERE name=:name"
    result = await db.fetch_one(query=query, values={"name": name})
    if result:
        img_byte = io.BytesIO(result["img"])
        return Response(content=img_byte.read(), media_type=result["content_type"])
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="img not found"
        )


@api.on_event("shutdown")
async def finish():
    await db.disconnect()
