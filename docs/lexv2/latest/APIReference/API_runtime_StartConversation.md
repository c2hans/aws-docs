---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_StartConversation.html
---

# StartConversation
<a name="API_runtime_StartConversation"></a>

Starts an HTTP/2 bidirectional event stream that enables you to send audio, text, or DTMF input in real time. After your application starts a conversation, users send input to Amazon Lex as a stream of events. Amazon Lex processes the incoming events and responds with streaming text or audio events.

Audio input must be in the following format: `audio/lpcm sample-rate=8000 sample-size-bits=16 channel-count=1; is-big-endian=false`.

If the optional post-fulfillment response is specified, the messages are returned as follows. For more information, see [PostFulfillmentStatusSpecification](https://docs.aws.amazon.com/lexv2/latest/dg/API_PostFulfillmentStatusSpecification.html).
+  **Success message** - Returned if the Lambda function completes successfully and the intent state is fulfilled or ready fulfillment if the message is present.
+  **Failed message** - The failed message is returned if the Lambda function throws an exception or if the Lambda function returns a failed intent state without a message.
+  **Timeout message** - If you don't configure a timeout message and a timeout, and the Lambda function doesn't return within 30 seconds, the timeout message is returned. If you configure a timeout, the timeout message is returned when the period times out.

For more information, see [Completion message](https://docs.aws.amazon.com/lexv2/latest/dg/streaming-progress.html#progress-complete.html).

If the optional update message is configured, it is played at the specified frequency while the Lambda function is running and the update message state is active. If the fulfillment update message is not active, the Lambda function runs with a 30 second timeout.

For more information, see [Update message ](https://docs.aws.amazon.com/lexv2/latest/dg/streaming-progress.html#progress-update.html)

The `StartConversation` operation is supported only in the following SDKs:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/runtime.lex.v2-2020-08-07/StartConversation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/runtime.lex.v2-2020-08-07/StartConversation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/runtime.lex.v2-2020-08-07/StartConversation)

## Request Syntax
<a name="API_runtime_StartConversation_RequestSyntax"></a>

```
POST /bots/{{botId}}/botAliases/{{botAliasId}}/botLocales/{{localeId}}/sessions/{{sessionId}}/conversation HTTP/1.1
x-amz-lex-conversation-mode: {{conversationMode}}
Content-type: application/json

{
   "AudioInputEvent": {
      "audioChunk": {{blob}},
      "clientTimestampMillis": {{number}},
      "contentType": "{{string}}",
      "eventId": "{{string}}"
   },
   "ConfigurationEvent": {
      "clientTimestampMillis": {{number}},
      "disablePlayback": {{boolean}},
      "eventId": "{{string}}",
      "requestAttributes": {
         "{{string}}" : "{{string}}"
      },
      "responseContentType": "{{string}}",
      "sessionState": {
         "activeContexts": [
            {
               "contextAttributes": {
                  "{{string}}" : "{{string}}"
               },
               "name": "{{string}}",
               "timeToLive": {
                  "timeToLiveInSeconds": {{number}},
                  "turnsToLive": {{number}}
               }
            }
         ],
         "dialogAction": {
            "slotElicitationStyle": "{{string}}",
            "slotToElicit": "{{string}}",
            "subSlotToElicit": {
               "name": "{{string}}",
               "subSlotToElicit": "ElicitSubSlot"
            },
            "type": "{{string}}"
         },
         "intent": {
            "confirmationState": "{{string}}",
            "name": "{{string}}",
            "slots": {
               "{{string}}" : {
                  "shape": "{{string}}",
                  "subSlots": {
                     "{{string}}" : "Slot"
                  },
                  "value": {
                     "interpretedValue": "{{string}}",
                     "originalValue": "{{string}}",
                     "resolvedValues": [ "{{string}}" ]
                  },
                  "values": [
                     "Slot"
                  ]
               }
            },
            "state": "{{string}}"
         },
         "originatingRequestId": "{{string}}",
         "runtimeHints": {
            "slotHints": {
               "{{string}}" : {
                  "{{string}}" : {
                     "runtimeHintValues": [
                        {
                           "phrase": "{{string}}"
                        }
                     ],
                     "subSlotHints": {
                        "{{string}}" : "RuntimeHintDetails"
                     }
                  }
               }
            }
         },
         "sessionAttributes": {
            "{{string}}" : "{{string}}"
         }
      },
      "welcomeMessages": [
         {
            "content": "{{string}}",
            "contentType": "{{string}}",
            "imageResponseCard": {
               "buttons": [
                  {
                     "text": "{{string}}",
                     "value": "{{string}}"
                  }
               ],
               "imageUrl": "{{string}}",
               "subtitle": "{{string}}",
               "title": "{{string}}"
            }
         }
      ]
   },
   "DisconnectionEvent": {
      "clientTimestampMillis": {{number}},
      "eventId": "{{string}}"
   },
   "DTMFInputEvent": {
      "clientTimestampMillis": {{number}},
      "eventId": "{{string}}",
      "inputCharacter": "{{string}}"
   },
   "PlaybackCompletionEvent": {
      "clientTimestampMillis": {{number}},
      "eventId": "{{string}}"
   },
   "TextInputEvent": {
      "clientTimestampMillis": {{number}},
      "eventId": "{{string}}",
      "text": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_runtime_StartConversation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botAliasId](#API_runtime_StartConversation_RequestSyntax) **   <a name="lexv2-runtime_StartConversation-request-uri-botAliasId"></a>
The alias identifier in use for the bot that processes the request.
Required: Yes

 ** [botId](#API_runtime_StartConversation_RequestSyntax) **   <a name="lexv2-runtime_StartConversation-request-uri-botId"></a>
The identifier of the bot to process the request.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [conversationMode](#API_runtime_StartConversation_RequestSyntax) **   <a name="lexv2-runtime_StartConversation-request-conversationMode"></a>
The conversation type that you are using the Amazon Lex. If the conversation mode is `AUDIO` you can send both audio and DTMF information. If the mode is `TEXT` you can only send text.
Valid Values: `AUDIO | TEXT`

 ** [localeId](#API_runtime_StartConversation_RequestSyntax) **   <a name="lexv2-runtime_StartConversation-request-uri-localeId"></a>
The locale where the session is in use.
Length Constraints: Minimum length of 1.
Required: Yes

 ** [sessionId](#API_runtime_StartConversation_RequestSyntax) **   <a name="lexv2-runtime_StartConversation-request-uri-sessionId"></a>
The identifier of the user session that is having the conversation.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[0-9a-zA-Z._:-]+`
Required: Yes

## Request Body
<a name="API_runtime_StartConversation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AudioInputEvent](#API_runtime_StartConversation_RequestSyntax) **   <a name="lexv2-runtime_StartConversation-request-AudioInputEvent"></a>
Speech audio sent from your client application to Amazon Lex. Audio starts accumulating when Amazon Lex identifies a voice and continues until a natural pause in the speech is found before processing.
Type: [AudioInputEvent](API_runtime_AudioInputEvent.md) object
Required: No

 ** [ConfigurationEvent](#API_runtime_StartConversation_RequestSyntax) **   <a name="lexv2-runtime_StartConversation-request-ConfigurationEvent"></a>
Configuration information sent from your client application to Amazon Lex
Type: [ConfigurationEvent](API_runtime_ConfigurationEvent.md) object
Required: No

 ** [DisconnectionEvent](#API_runtime_StartConversation_RequestSyntax) **   <a name="lexv2-runtime_StartConversation-request-DisconnectionEvent"></a>
Event sent from the client application to indicate to Amazon Lex that the conversation is over.
Type: [DisconnectionEvent](API_runtime_DisconnectionEvent.md) object
Required: No

 ** [DTMFInputEvent](#API_runtime_StartConversation_RequestSyntax) **   <a name="lexv2-runtime_StartConversation-request-DTMFInputEvent"></a>
DTMF information sent to Amazon Lex by your application. Amazon Lex accumulates the DMTF information from when the user sends the first character and ends
+ when there's a pause longer that the value configured for the end timeout.
+ when there's a digit that is the configured end character.
+ when Amazon Lex accumulates characters equal to the maximum DTMF character configuration.
Type: [DTMFInputEvent](API_runtime_DTMFInputEvent.md) object
Required: No

 ** [PlaybackCompletionEvent](#API_runtime_StartConversation_RequestSyntax) **   <a name="lexv2-runtime_StartConversation-request-PlaybackCompletionEvent"></a>
Event sent from the client application to Amazon Lex to indicate that it has finished playing audio and that Amazon Lex should start listening for user input.
Type: [PlaybackCompletionEvent](API_runtime_PlaybackCompletionEvent.md) object
Required: No

 ** [TextInputEvent](#API_runtime_StartConversation_RequestSyntax) **   <a name="lexv2-runtime_StartConversation-request-TextInputEvent"></a>
Text sent from your client application to Amazon Lex. Each `TextInputEvent` is processed individually.
Type: [TextInputEvent](API_runtime_TextInputEvent.md) object
Required: No

## Response Syntax
<a name="API_runtime_StartConversation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccessDeniedException": {
   },
   "AudioResponseEvent": {
      "audioChunk": blob,
      "contentType": "string",
      "eventId": "string"
   },
   "BadGatewayException": {
   },
   "ConflictException": {
   },
   "DependencyFailedException": {
   },
   "HeartbeatEvent": {
      "eventId": "string"
   },
   "IntentResultEvent": {
      "eventId": "string",
      "inputMode": "string",
      "interpretations": [
         {
            "intent": {
               "confirmationState": "string",
               "name": "string",
               "slots": {
                  "string" : {
                     "shape": "string",
                     "subSlots": {
                        "string" : "Slot"
                     },
                     "value": {
                        "interpretedValue": "string",
                        "originalValue": "string",
                        "resolvedValues": [ "string" ]
                     },
                     "values": [
                        "Slot"
                     ]
                  }
               },
               "state": "string"
            },
            "interpretationSource": "string",
            "nluConfidence": {
               "score": number
            },
            "sentimentResponse": {
               "sentiment": "string",
               "sentimentScore": {
                  "mixed": number,
                  "negative": number,
                  "neutral": number,
                  "positive": number
               }
            }
         }
      ],
      "recognizedBotMember": {
         "botId": "string",
         "botName": "string"
      },
      "requestAttributes": {
         "string" : "string"
      },
      "sessionId": "string",
      "sessionState": {
         "activeContexts": [
            {
               "contextAttributes": {
                  "string" : "string"
               },
               "name": "string",
               "timeToLive": {
                  "timeToLiveInSeconds": number,
                  "turnsToLive": number
               }
            }
         ],
         "dialogAction": {
            "slotElicitationStyle": "string",
            "slotToElicit": "string",
            "subSlotToElicit": {
               "name": "string",
               "subSlotToElicit": "ElicitSubSlot"
            },
            "type": "string"
         },
         "intent": {
            "confirmationState": "string",
            "name": "string",
            "slots": {
               "string" : {
                  "shape": "string",
                  "subSlots": {
                     "string" : "Slot"
                  },
                  "value": {
                     "interpretedValue": "string",
                     "originalValue": "string",
                     "resolvedValues": [ "string" ]
                  },
                  "values": [
                     "Slot"
                  ]
               }
            },
            "state": "string"
         },
         "originatingRequestId": "string",
         "runtimeHints": {
            "slotHints": {
               "string" : {
                  "string" : {
                     "runtimeHintValues": [
                        {
                           "phrase": "string"
                        }
                     ],
                     "subSlotHints": {
                        "string" : "RuntimeHintDetails"
                     }
                  }
               }
            }
         },
         "sessionAttributes": {
            "string" : "string"
         }
      }
   },
   "InternalServerException": {
   },
   "PlaybackInterruptionEvent": {
      "causedByEventId": "string",
      "eventId": "string",
      "eventReason": "string"
   },
   "ResourceNotFoundException": {
   },
   "TextResponseEvent": {
      "eventId": "string",
      "messages": [
         {
            "content": "string",
            "contentType": "string",
            "imageResponseCard": {
               "buttons": [
                  {
                     "text": "string",
                     "value": "string"
                  }
               ],
               "imageUrl": "string",
               "subtitle": "string",
               "title": "string"
            }
         }
      ]
   },
   "ThrottlingException": {
   },
   "TranscriptEvent": {
      "eventId": "string",
      "transcript": "string"
   },
   "ValidationException": {
   }
}
```

## Response Elements
<a name="API_runtime_StartConversation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessDeniedException](#API_runtime_StartConversation_ResponseSyntax) **   <a name="lexv2-runtime_StartConversation-response-AccessDeniedException"></a>
Exception thrown when the credentials passed with the request are invalid or expired. Also thrown when the credentials in the request do not have permission to access the `StartConversation` operation.
Type: Exception
HTTP Status Code: 403

 ** [AudioResponseEvent](#API_runtime_StartConversation_ResponseSyntax) **   <a name="lexv2-runtime_StartConversation-response-AudioResponseEvent"></a>
An event sent from Amazon Lex to your client application containing audio to play to the user.
Type: [AudioResponseEvent](API_runtime_AudioResponseEvent.md) object

 ** [BadGatewayException](#API_runtime_StartConversation_ResponseSyntax) **   <a name="lexv2-runtime_StartConversation-response-BadGatewayException"></a>

Type: Exception
HTTP Status Code: 502

 ** [ConflictException](#API_runtime_StartConversation_ResponseSyntax) **   <a name="lexv2-runtime_StartConversation-response-ConflictException"></a>
Exception thrown when two clients are using the same AWS account, Amazon Lex bot, and session ID.
Type: Exception
HTTP Status Code: 409

 ** [DependencyFailedException](#API_runtime_StartConversation_ResponseSyntax) **   <a name="lexv2-runtime_StartConversation-response-DependencyFailedException"></a>

Type: Exception
HTTP Status Code: 424

 ** [HeartbeatEvent](#API_runtime_StartConversation_ResponseSyntax) **   <a name="lexv2-runtime_StartConversation-response-HeartbeatEvent"></a>
Event that Amazon Lex sends to indicate that the stream is still open between the client application and Amazon Lex
Type: [HeartbeatEvent](API_runtime_HeartbeatEvent.md) object

 ** [IntentResultEvent](#API_runtime_StartConversation_ResponseSyntax) **   <a name="lexv2-runtime_StartConversation-response-IntentResultEvent"></a>
Event sent from Amazon Lex to the client application containing the current state of the conversation between the user and Amazon Lex.
Type: [IntentResultEvent](API_runtime_IntentResultEvent.md) object

 ** [InternalServerException](#API_runtime_StartConversation_ResponseSyntax) **   <a name="lexv2-runtime_StartConversation-response-InternalServerException"></a>
An error occurred with Amazon Lex.
Type: Exception
HTTP Status Code: 500

 ** [PlaybackInterruptionEvent](#API_runtime_StartConversation_ResponseSyntax) **   <a name="lexv2-runtime_StartConversation-response-PlaybackInterruptionEvent"></a>
Event sent from Amazon Lex to indicate to the client application should stop playback of audio. For example, if the client is playing a prompt that asks for the user's telephone number, the user might start to say the phone number before the prompt is complete. Amazon Lex sends this event to the client application to indicate that the user is responding and that Amazon Lex is processing their input.
Type: [PlaybackInterruptionEvent](API_runtime_PlaybackInterruptionEvent.md) object

 ** [ResourceNotFoundException](#API_runtime_StartConversation_ResponseSyntax) **   <a name="lexv2-runtime_StartConversation-response-ResourceNotFoundException"></a>
Exception thrown if one of the input parameters points to a resource that does not exist. For example, if the bot ID specified does not exist.
Type: Exception
HTTP Status Code: 404

 ** [TextResponseEvent](#API_runtime_StartConversation_ResponseSyntax) **   <a name="lexv2-runtime_StartConversation-response-TextResponseEvent"></a>
The event sent from Amazon Lex to your application with text to present to the user.
Type: [TextResponseEvent](API_runtime_TextResponseEvent.md) object

 ** [ThrottlingException](#API_runtime_StartConversation_ResponseSyntax) **   <a name="lexv2-runtime_StartConversation-response-ThrottlingException"></a>
Exception thrown when your application exceeds the maximum number of concurrent requests.
Type: Exception
HTTP Status Code: 429

 ** [TranscriptEvent](#API_runtime_StartConversation_ResponseSyntax) **   <a name="lexv2-runtime_StartConversation-response-TranscriptEvent"></a>
Event sent from Amazon Lex to your client application that contains a transcript of voice audio.
Type: [TranscriptEvent](API_runtime_TranscriptEvent.md) object

 ** [ValidationException](#API_runtime_StartConversation_ResponseSyntax) **   <a name="lexv2-runtime_StartConversation-response-ValidationException"></a>
Exception thrown when one or more parameters could not be validated. The `message` contains the name of the field that isn't valid.
Type: Exception
HTTP Status Code: 400

## Errors
<a name="API_runtime_StartConversation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

HTTP Status Code: 403

 ** InternalServerException **

HTTP Status Code: 500

 ** ThrottlingException **

HTTP Status Code: 429

 ** ValidationException **

HTTP Status Code: 400

## See Also
<a name="API_runtime_StartConversation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/runtime.lex.v2-2020-08-07/StartConversation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/runtime.lex.v2-2020-08-07/StartConversation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/runtime.lex.v2-2020-08-07/StartConversation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/runtime.lex.v2-2020-08-07/StartConversation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/runtime.lex.v2-2020-08-07/StartConversation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/runtime.lex.v2-2020-08-07/StartConversation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/runtime.lex.v2-2020-08-07/StartConversation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/runtime.lex.v2-2020-08-07/StartConversation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/runtime.lex.v2-2020-08-07/StartConversation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/runtime.lex.v2-2020-08-07/StartConversation)
