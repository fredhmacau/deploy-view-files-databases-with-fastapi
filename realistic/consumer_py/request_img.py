import requests
import shutil
import io

def main(name_img,extension):
    url = f"http://127.0.0.1:8000/img/{name_img}.{extension}"
    resp=requests.get(url,stream=True)
    with open(f"{name_img}.{extension}","wb") as file:
        file.write(resp.content)
    

if __name__=="__main__":
    main("code","png")