Deploy/View images to database sqlite with fastapi
cd realistic
=======
## Dependencies 
* databases==0.5.3  
* fastapi==0.68.0  
* Hypercorn==0.11.2  
* pydantic==1.8.2   
* python-multipart==0.0.5  
* SQLAlchemy==1.4.20  
* starlette==0.14.2  
* uvicorn==0.15.0  

### run command
uvicorn main:api
## Screens
### Add image from form to database sqlite
![Add image from form to database sqlite](https://github.com/fredhmacau/deploy-view-files-databases-with-fastapi/blob/main/screens/Captura%20de%20ecr%C3%A3%20de%202022-01-04%2016-37-49.png)  
### Response status  
![Response status](https://github.com/fredhmacau/deploy-view-files-databases-with-fastapi/blob/main/screens/Captura%20de%20ecr%C3%A3%20de%202022-01-04%2016-38-48.png)  
### GET image from http://127.0.0.1:8000/img/{name_image}  
![GET image from](https://github.com/fredhmacau/deploy-view-files-databases-with-fastapi/blob/main/screens/Captura%20de%20ecr%C3%A3%20de%202022-01-04%2016-40-40.png)  
### Response image  
![Response image](https://github.com/fredhmacau/deploy-view-files-databases-with-fastapi/blob/main/screens/Captura%20de%20ecr%C3%A3%20de%202022-01-04%2016-41-20.png)  
