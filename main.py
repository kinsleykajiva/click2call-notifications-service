from fastapi import FastAPI
from starlette.exceptions import HTTPException
from routes import index, users
from dotenv import load_dotenv
from starlette.responses import JSONResponse
from py_eureka_client import eureka_client
import os

from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = FastAPI()


app.include_router(index.router)
app.include_router(users.router)


@app.exception_handler(HTTPException)
async def validation_exception_handler (request, err):
	base_error_message = f"Failed to execute: {request.method}: {request.url}"
	# Change here to LOGGER
	return JSONResponse(status_code=400, content={
		"success": False,
		"status": 400,
		"message": f"{base_error_message}. Detail: {err}"
	})



if os.getenv('ENV_TYPE') is not None:
	print("SYSTEM::::running  in PRODUCTION")
	eureka_client.init(eureka_server=os.getenv('EUREKA_SERVER'), app_name=os.getenv('SERVICE_NAME'),
					   instance_port=int(os.getenv('PORT')), data_center_name=os.getenv('DATA_CENTER_NAME'),

					   region=os.getenv('REGION'), vip_adr=os.getenv('SERVICE_NAME'))
else:
	print("SYSTEM::::running  in local set up")
	eureka_client.init(eureka_server="http://localhost:8761/eureka/", app_name=os.getenv('SERVICE_NAME'), instance_port=int(os.getenv('PORT')), instance_host='localhost', instance_ip='172.0.0.1')
