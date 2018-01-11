##############################
# Builders
##############################


def build_plain_speech(body):
    return {'type': 'PlainText', 'text': body}


def build_response(message, session_attributes=None):
    return {'version': '1.0', 'sessionAttributes': session_attributes or {}, 'response': message}


def build_simple_card(title, body):
    return {'type': 'Simple', 'title': title, 'content': body}


##############################
# Responses
##############################


def conversation(title, body, session_attributes):
    speechlet = {
        'outputSpeech': build_plain_speech(body),
        'card': build_simple_card(title, body),
        'shouldEndSession': False
    }
    return build_response(speechlet, session_attributes=session_attributes)


def statement(title, body):
    speechlet = {
        'outputSpeech': build_plain_speech(body),
        'card': build_simple_card(title, body),
        'shouldEndSession': True
    }
    return build_response(speechlet)


def continue_dialog():
    message = {'shouldEndSession': False, 'directives': [{'type': 'Dialog.Delegate'}]}
    return build_response(message)


##############################
# Custom Intents
##############################


def things_intent(event, context):
    dialog_state = event['request']['dialogState']

    if dialog_state in ("STARTED", "IN_PROGRESS"):
        return continue_dialog()

    elif dialog_state == "COMPLETED":
        value = event['request']['intent']['slots']['taskTitle']['value']
        return statement("things_intent", "Task {} was added!".format(value))

    else:
        return statement("things_intent", "No dialog")


##############################
# Required Intents
##############################


def cancel_intent():
    return statement("CancelIntent", "You want to cancel")


def help_intent():
    return statement("CancelIntent", "You want help")


def stop_intent():
    return statement("StopIntent", "You want to stop")


##############################
# On Launch
##############################


def on_launch(event, context):
    return statement("title", "body")


##############################
# Routing
##############################


def intent_router(event, context):
    intent = event['request']['intent']['name']

    # Custom Intents

    if intent == "ThingsIntent":
        return things_intent(event, context)

    # Required Intents

    if intent == "AMAZON.CancelIntent":
        return cancel_intent()

    if intent == "AMAZON.HelpIntent":
        return help_intent()

    if intent == "AMAZON.StopIntent":
        return stop_intent()


##############################
# Program Entry
##############################


def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)

    elif event['request']['type'] == "IntentRequest":
        return intent_router(event, context)