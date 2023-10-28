import json
import copy
import openai

from prompts import *


def get_game_start_messages():
    return get_setup()


def get_scenario():
    return BASE_SCENARIO_PROMPT.substitute({})


def get_setup():
    return BASE_SETUP.substitute({})


def get_instruction():
    return INSTRUCTION_PROMPT.substitute({})


def classify_user_request_type(user_request, model="gpt-3.5-turbo"):
    messages = []
    messages.append({"role": "system", "content": f"""INSTRUCTION
{get_instruction()}

SCENARIO
{get_scenario()}

SETUP
{get_setup()}
"""})
    messages.append({"role": "user",
                     "content": CLASSIFY_USER_REQUEST_PROMPT.substitute({"user_request": user_request})})
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages)
    response_message = response["choices"][0]["message"]
    # print(type(response_message))
    # print(response_message)
    user_request_type = json.loads(response_message["content"])["class"]
    return user_request_type


def describe_that_action_is_not_controlled(messages, user_request, model="gpt-3.5-turbo"):
    messages_new = copy.deepcopy(messages)
    messages_new = []
    messages_new.append({"role": "system", "content": f"""INSTRUCTION
{get_instruction()}

SCENARIO
{get_scenario()}

SETUP
{get_setup()}
"""})
    messages_new.append({"role": "user", "content": DESCRIBE_NOT_CONTOLLED_ACTION_PROMPT.substitute(
        {"user_request": user_request})})
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages)
    response_message = response["choices"][0]["message"]
    # print(type(response_message))
    # print(response_message)
    return response_message["content"]


def get_response_by_messages(messages, user_request):
    user_request_type = classify_user_request_type(user_request)
    # messages.append({"role": "assistant", "content": user_request_type})
    if user_request_type == "Doing":
        pass
    elif user_request_type == "Ask":
        pass
    elif user_request_type == "Not under your control":
        messages.append(
            {"role": "assistant", "content": describe_that_action_is_not_controlled(messages, user_request)})
    return messages
