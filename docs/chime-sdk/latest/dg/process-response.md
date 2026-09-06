---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/process-response.html
---

# Processing responses from an AppInstanceBot for Amazon Chime SDK messaging
<a name="process-response"></a>

When a user sends a message, the AppInstanceBot responds with a channel message. You can list channel messages to get the bot's response.

The following example shows you to use the CLI to list channel messages.

```
aws chime-sdk-messaging list-channel-messages \
--chime-bearer {{caller_app_instance_user_arn}} \
--channel-arn {{channel_arn}}
```

Success responses from an AppInstanceBot take the following format.

```
{
    "MessageId": "{{messageId}}",
    "Content": "*{\"{{Messages}}\":[{\"...\"}]}*",
    "ContentType": "{{application/amz-chime-lex-msgs}}",
    "MessageAttributes": {
        "CHIME.LEX.sessionState.intent.name": {
            "StringValues": [
                "{{lex_bot_intent_name}}"
            ]
        },
        "CHIME.LEX.sessionState.intent.state": {
            "StringValues": [
                "{{lex_bot_intent_fullfilment_status}}"
            ]
        },
        "CHIME.LEX.sessionState.originatingRequestId": {
            "StringValues": [
                "{{lex_bot_originating_request_id}}"
            ]
        },
        "CHIME.LEX.sessionState.sessionId": {
            "StringValues": [
                "{{lex_bot_session_id}}"
            ]
        }
    },
    "Sender": {
        "Arn": "{{app_instance_bot_arn}}",
        "Name": "{{app_instance_bot_name}}"
    },
    "Type": "STANDARD",
}
```

**Content**
The `Content` field contains a list of messages originating from the Amazon Lex V2 bot. For more information about those messages, refer to [ messages](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeText.html#lexv2-runtime_RecognizeText-response-messages) in the Amazon Lex V2 `RecognizeText` API.
The following example shows how to use the `Content` field in a welcome message.

```
{
    "Messages":
    [
        {
            "Content": "{{Hello!}}",
            "ContentType": "{{PlainText}}"
        },
        {
            "ContentType": "ImageResponseCard",
            "ImageResponseCard":
            {
                "Title": "{{Hello! I'm BB, the Bank Bot.}}",
                "Subtitle": "{{I can help you with the following transactions}}",
                "Buttons":
                [
                    {
                        "Text": "{{Check balance}}",
                        "Value": "{{Check balance}}"
                    },
                    {
                        "Text": "{{Escalate to agent}}",
                        "Value": "{{Escalate to agent}}"
                    }
                ]
            }
        }
    ]
}
```
For a failure response, the Content field contains an error message and code in the following format:

```
{
    "Code": {{error_code}}
}
```

**ContentType**
The `ContentType` refers to the type of payload the `Content` field contains, and must be checked to parse the `Content` field.
The Lex V2 bot uses a different `ContentType`.
`ContentType` is set to `application/amz-chime-lex-msgs` for a success response, or `application/amz-chime-lex-error` for a failure response.

**MessageAttributes**
A *MessageAttribute* is a map of string keys to string values. A response from an `AppInstanceBot` contains the following message attributes mapped to a response from an Amazon Lex bot.
+ **CHIME.LEX.sessionState.intent.name** – The name of the Lex bot intent that the request attempted to fulfill.
+ **CHIME.LEX.sessionState.intent.state** – The current state of the intent. Possible values include: `Fulfilled`, `InProgress`, and `Failed`.
+ **CHIME.LEX.sessionState.originatingRequestId** – A unique identifier for a specific request to Amazon Lex bot. This is set to the `MessageId` of the originating user message that triggered the AppInstanceBot.
+ **CHIME.LEX.sessionState.sessionId** – A unique identifier for a conversation between the user and the bot. When a user starts a chat with your bot, Amazon Lex creates a session.
For more information about Amazon Lex sessions and session states, refer to [SessionState](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_SessionState.html) in the *Amazon Lex API Reference*, and [Managing sessions](https://docs.aws.amazon.com/lexv2/latest/dg/using-sessions.html) in the *in the Amazon Lex V2 Developer Guide*
For more information about the attributes that Amazon Lex V2 returns, refer to the [Amazon Lex Runtime V2](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_Operations_Amazon_Lex_Runtime_V2.html) APIs.
