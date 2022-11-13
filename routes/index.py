import os

import requests
from dotenv import load_dotenv
from fastapi import APIRouter, Request
from starlette.exceptions import HTTPException

from templates.emails.accountDetailsUpdatedEmail import accountDetailsEmail
from templates.emails.addedToTeamEmail import addedToTeamEmail
from templates.emails.askedToJoinCompanyWithNoUserAccontemail import askedToJoinCompanyWithNoUserAccountEmail
from templates.emails.scriptTagToDeveloperInstructionEmail import scriptToDeveloperInstructions
from templates.emails.signUpEmail import signupEmail
from utils.utils import sendEmail

load_dotenv()

BASE_URL = 'https://xxxxxxxxxxxxxxx.com'

router = APIRouter(
	prefix="",
	tags=[],
)

@router.get("/")
async def root ():
	return {"message": "notifications service here @4"}

@router.get("/info")
async def rootinfo():
	return {
		"success": True,
		"message": "info -notifications API",
	}




@router.post("/account-creation")
async def createNew23 (request: Request):
	bodyJson = await request.json()
	email = (bodyJson['email'])
	name = (bodyJson['name'])
	activateLink = (bodyJson['activateLink'])
	
	name = name if name == '' else 'New user'
	
	sendEmail(name, "✔ " + "xxxxxxxxxxxxxxx Account Creation", email, signupEmail(name, BASE_URL + '/activate/' + activateLink));
	return {
		'success': True,
		'message': "Email sent successfully",
	}


@router.post("/account-details-update")
async def createN3ewew (request: Request):
	bodyJson = await request.json()
	email = (bodyJson['email'])
	name = (bodyJson['name'])
	
	name = name if name == '' else 'Our Valued user'
	sendEmail(name, "xxxxxxxxxxxxxxx Account Details Updated", email, accountDetailsEmail(name, ''))
	return {
		'success': True,
		'message': "Email sent successfully",
	}
