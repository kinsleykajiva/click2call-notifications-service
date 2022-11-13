import os

import requests
from dotenv import load_dotenv
from fastapi import APIRouter, Request
from starlette.exceptions import HTTPException

from templates.emails.accountActivateEmail import accountActivateEmail
from templates.emails.accountDeletedEmail import notifyUserDeletedByUser
from templates.emails.accountDetailsUpdatedEmail import accountDetailsEmail
from templates.emails.addedToTeamEmail import addedToTeamEmail
from templates.emails.askedToJoinCompanyWithNoUserAccontemail import askedToJoinCompanyWithNoUserAccountEmail
from templates.emails.companyAccountDeleteEmail import deleteCompnayAccount
from templates.emails.resetUserAccountCodeEmail import resetUserAccountCodeEmail
from templates.emails.scriptTagToDeveloperInstructionEmail import scriptToDeveloperInstructions
from templates.emails.signUpEmail import signupEmail
from templates.emails.userAccountActivateEmail import userAccountActivateEmail
from templates.emails.userAccountCreatedEmailByUserEmail import notifyUserAccountCreatedByUser
from utils.utils import sendEmail

load_dotenv()

router = APIRouter(
    prefix="/users",
    tags=[],
)


@router.post("/asked-new-user-to-join")
async def createNew1111(request: Request):
    body_json = await request.json()
    email = (body_json['email'])
    added_by_user = (body_json['addedByUser'])
    company_name = (body_json['companyName'])
    activate_link = (body_json['activateLink'])
    sendEmail('Our Valued user', "Inta Call - Asked to Join Company", email,
              askedToJoinCompanyWithNoUserAccountEmail(added_by_user, company_name, activate_link))

    return {
        'success': True,
        'message': "Email sent successfully",
    }


@router.post("/widget-instructions")
async def createNew34r(request: Request):
    bodyJson = await request.json()
    email = (bodyJson['email'])
    name = (bodyJson['name'])
    activattion_link = (bodyJson['activattionLink'])
    name = name if name == '' else 'Our Valued user'

    sendEmail(name, "Inta Call Website Widget Installation Instructions", email,
              scriptToDeveloperInstructions(activattion_link))

    return {
        'success': True,
        'message': "Email sent successfully",
    }


@router.post("/account-details-update")
async def create12New(request: Request):
    body_json = await request.json()
    email = (body_json['email'])
    name = (body_json['name'])
    activattion_link = (body_json['activattionLink'])
    name = name if name == '' else 'Our Valued user'

    sendEmail(name, "Inta Call Account Details Updated", email, accountDetailsEmail(name, activattion_link))

    return {
        'success': True,
        'message': "Email sent successfully",
    }


@router.post("/account-verification-verification")
async def create12tyNew(request: Request):
    """
    Send email to user to verify account
    :param request:
    :return:
    """
    body_json = await request.json()
    email = (body_json['email'])
    user_full_name = (body_json['user_full_name'])
    link_activate = (body_json['link_activate'])

    sendEmail(user_full_name, "Inta Call Account Verification/Activation", email,
              userAccountActivateEmail(user_full_name, link_activate))

    return {
        'success': True,
        'message': "Email sent successfully",
    }


@router.post("/user-account-created-by-user")
async def create1275New(request: Request):
    body_json = await request.json()
    email = (body_json['email'])
    name = (body_json['name'])
    user_full_name = (body_json['userFullName'])
    username = (body_json['Username'])
    password = (body_json['password'])
    the_sender_name = (body_json['theSenderName'])
    company_name = (body_json['companyName'])
    name = name if name == '' else 'Our Valued user'

    sendEmail(name, "Inta Call New User Account Setup", email,
              notifyUserAccountCreatedByUser(user_full_name, username, password, the_sender_name, company_name))

    return {
        'success': True,
        'message': "Email sent successfully",
    }


@router.post("/user-account-deleted-by-user")
async def create12r75New(request: Request):
    body_json = await request.json()
    email = (body_json['email'])
    name = (body_json['name'])
    user_full_name = (body_json['userFullName'])
    username = (body_json['Username'])
    company_name = (body_json['companyName'])
    name = name if name == '' else 'Our Valued user'

    sendEmail(name, "Inta Call New User Account Deleted", email,
              notifyUserDeletedByUser(user_full_name, username, company_name))

    return {
        'success': True,
        'message': "Email sent successfully",
    }


@router.post("/user-account-activate-by-user")
async def create12r75New(request: Request):
    body_json = await request.json()
    email = (body_json['email'])
    name = (body_json['name'])
    user_full_name = (body_json['userFullName'])
    username = (body_json['Username'])
    company_name = (body_json['companyName'])
    name = name if name == '' else 'Our Valued user'

    sendEmail(name, "Inta Call New User Account Deleted", email,
              accountActivateEmail(user_full_name, username, company_name))

    return {
        'success': True,
        'message': "Email sent successfully",
    }


@router.post("/user-added-to-team")
async def user_added_to_team(request: Request):
    body_json = await request.json()
    email = (body_json['email'])
    name = (body_json['name'])
    activate_link = (body_json['activateLink'])
    team_name = (body_json['teamName'])
    added_by_user = (body_json['addedByUser'])
    name = name if name == '' or name is None else 'Our Valued user'
    sendEmail(name, "Inta Call - Teams", email,
              addedToTeamEmail(name, activate_link, team_name, added_by_user))

    return {
        'success': True,
        'message': "Email sent successfully",
    }


@router.post("/delete-company-code")
async def user_added_to_team(request: Request):
    body_json = await request.json()
    email = (body_json['email'])
    code = (body_json['code'])
    expire_mins = (body_json['expire_mins'])
    company_name = (body_json['companyName'])

    sendEmail('Our Valued user', "Inta Call - Company Account Deletion ", email,
              deleteCompnayAccount(company_name, code, expire_mins))

    return {
        'success': True,
        'message': "Email sent successfully",
    }


@router.post("/reset-user-password-code")
async def reset_user_account_email(request: Request):
    body_json = await request.json()
    email = (body_json['email'])
    code = (body_json['code'])
    expire_mins = (body_json['expire_mins'])

    sendEmail('Our Valued user', "Inta Call - Reset Password ", email,
              resetUserAccountCodeEmail(code, expire_mins))

    return {
        'success': True,
        'message': "Email sent successfully",
    }


@router.post("/account-creation")
async def account_creation(request: Request):
    bodyJson = await request.json()
    email = (bodyJson['email'])
    name = (bodyJson['name'])
    activattionLink = (bodyJson['activattionLink'])

    name = name if name == '' else 'New user'

    sendEmail(name, "✔ " + "Inta Call Account Creation", email, signupEmail(name, activattionLink))

    return {
        'success': True,
        'message': "Email sent successfully",
    }
