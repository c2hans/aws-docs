---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBotLocale.html
---

# CreateBotLocale
<a name="API_CreateBotLocale"></a>

Creates a locale in the bot. The locale contains the intents and slot types that the bot uses in conversations with users in the specified language and locale. You must add a locale to a bot before you can add intents and slot types to the bot.

## Request Syntax
<a name="API_CreateBotLocale_RequestSyntax"></a>

```
PUT /bots/{{botId}}/botversions/{{botVersion}}/botlocales/ HTTP/1.1
Content-type: application/json

{
   "audioFillerSettings": {
      "audioType": "{{string}}",
      "enabled": {{boolean}},
      "minimumPlayDurationInMilliseconds": {{number}},
      "responseDeliveryDelayInMilliseconds": {{number}},
      "startDelayInMilliseconds": {{number}}
   },
   "description": "{{string}}",
   "generativeAISettings": {
      "buildtimeSettings": {
         "descriptiveBotBuilder": {
            "bedrockModelSpecification": {
               "customPrompt": "{{string}}",
               "guardrail": {
                  "identifier": "{{string}}",
                  "version": "{{string}}"
               },
               "modelArn": "{{string}}",
               "traceStatus": "{{string}}"
            },
            "enabled": {{boolean}}
         },
         "sampleUtteranceGeneration": {
            "bedrockModelSpecification": {
               "customPrompt": "{{string}}",
               "guardrail": {
                  "identifier": "{{string}}",
                  "version": "{{string}}"
               },
               "modelArn": "{{string}}",
               "traceStatus": "{{string}}"
            },
            "enabled": {{boolean}}
         }
      },
      "runtimeSettings": {
         "nluImprovement": {
            "assistedNluMode": "{{string}}",
            "enabled": {{boolean}},
            "intentDisambiguationSettings": {
               "customDisambiguationMessage": "{{string}}",
               "enabled": {{boolean}},
               "maxDisambiguationIntents": {{number}}
            }
         },
         "slotResolutionImprovement": {
            "bedrockModelSpecification": {
               "customPrompt": "{{string}}",
               "guardrail": {
                  "identifier": "{{string}}",
                  "version": "{{string}}"
               },
               "modelArn": "{{string}}",
               "traceStatus": "{{string}}"
            },
            "enabled": {{boolean}}
         }
      }
   },
   "localeId": "{{string}}",
   "nluIntentConfidenceThreshold": {{number}},
   "speechDetectionSensitivity": "{{string}}",
   "speechRecognitionSettings": {
      "speechModelConfig": {
         "deepgramConfig": {
            "apiTokenSecretArn": "{{string}}",
            "modelId": "{{string}}"
         }
      },
      "speechModelPreference": "{{string}}"
   },
   "unifiedSpeechSettings": {
      "speechFoundationModel": {
         "modelArn": "{{string}}",
         "voiceId": "{{string}}"
      }
   },
   "voiceSettings": {
      "engine": "{{string}}",
      "voiceId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateBotLocale_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_CreateBotLocale_RequestSyntax) **   <a name="lexv2-CreateBotLocale-request-uri-botId"></a>
The identifier of the bot to create the locale for.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_CreateBotLocale_RequestSyntax) **   <a name="lexv2-CreateBotLocale-request-uri-botVersion"></a>
The version of the bot to create the locale for. This can only be the draft version of the bot.
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`
Required: Yes

## Request Body
<a name="API_CreateBotLocale_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [audioFillerSettings](#API_CreateBotLocale_RequestSyntax) **   <a name="lexv2-CreateBotLocale-request-audioFillerSettings"></a>
Audio filler settings to configure for the new bot locale. When enabled, Amazon Lex plays a brief background audio filler during speech-to-speech interactions to mask processing delays. Requires `unifiedSpeechSettings` (speech-to-speech) to be configured on the bot locale.
Type: [AudioFillerSettings](API_AudioFillerSettings.md) object
Required: No

 ** [description](#API_CreateBotLocale_RequestSyntax) **   <a name="lexv2-CreateBotLocale-request-description"></a>
A description of the bot locale. Use this to help identify the bot locale in lists.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** [generativeAISettings](#API_CreateBotLocale_RequestSyntax) **   <a name="lexv2-CreateBotLocale-request-generativeAISettings"></a>
Contains specifications about the generative AI capabilities from Amazon Bedrock that you can turn on for your bot.
Type: [GenerativeAISettings](API_GenerativeAISettings.md) object
Required: No

 ** [localeId](#API_CreateBotLocale_RequestSyntax) **   <a name="lexv2-CreateBotLocale-request-localeId"></a>
The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Type: String
Required: Yes

 ** [nluIntentConfidenceThreshold](#API_CreateBotLocale_RequestSyntax) **   <a name="lexv2-CreateBotLocale-request-nluIntentConfidenceThreshold"></a>
Determines the threshold where Amazon Lex will insert the `AMAZON.FallbackIntent`, `AMAZON.KendraSearchIntent`, or both when returning alternative intents. `AMAZON.FallbackIntent` and `AMAZON.KendraSearchIntent` are only inserted if they are configured for the bot.
For example, suppose a bot is configured with the confidence threshold of 0.80 and the `AMAZON.FallbackIntent`. Amazon Lex returns three alternative intents with the following confidence scores: IntentA (0.70), IntentB (0.60), IntentC (0.50). The response from the `RecognizeText` operation would be:
+ AMAZON.FallbackIntent
+ IntentA
+ IntentB
+ IntentC
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

 ** [speechDetectionSensitivity](#API_CreateBotLocale_RequestSyntax) **   <a name="lexv2-CreateBotLocale-request-speechDetectionSensitivity"></a>
The sensitivity level for voice activity detection (VAD) in the bot locale. This setting helps optimize speech recognition accuracy by adjusting how the system responds to background noise during voice interactions.
Type: String
Valid Values: `Default | HighNoiseTolerance | MaximumNoiseTolerance`
Required: No

 ** [speechRecognitionSettings](#API_CreateBotLocale_RequestSyntax) **   <a name="lexv2-CreateBotLocale-request-speechRecognitionSettings"></a>
Speech-to-text settings to configure for the new bot locale.
Type: [SpeechRecognitionSettings](API_SpeechRecognitionSettings.md) object
Required: No

 ** [unifiedSpeechSettings](#API_CreateBotLocale_RequestSyntax) **   <a name="lexv2-CreateBotLocale-request-unifiedSpeechSettings"></a>
Unified speech settings to configure for the new bot locale.
Type: [UnifiedSpeechSettings](API_UnifiedSpeechSettings.md) object
Required: No

 ** [voiceSettings](#API_CreateBotLocale_RequestSyntax) **   <a name="lexv2-CreateBotLocale-request-voiceSettings"></a>
The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user.
Type: [VoiceSettings](API_VoiceSettings.md) object
Required: No

## Response Syntax
<a name="API_CreateBotLocale_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "audioFillerSettings": {
      "audioType": "string",
      "enabled": boolean,
      "minimumPlayDurationInMilliseconds": number,
      "responseDeliveryDelayInMilliseconds": number,
      "startDelayInMilliseconds": number
   },
   "botId": "string",
   "botLocaleStatus": "string",
   "botVersion": "string",
   "creationDateTime": number,
   "description": "string",
   "generativeAISettings": {
      "buildtimeSettings": {
         "descriptiveBotBuilder": {
            "bedrockModelSpecification": {
               "customPrompt": "string",
               "guardrail": {
                  "identifier": "string",
                  "version": "string"
               },
               "modelArn": "string",
               "traceStatus": "string"
            },
            "enabled": boolean
         },
         "sampleUtteranceGeneration": {
            "bedrockModelSpecification": {
               "customPrompt": "string",
               "guardrail": {
                  "identifier": "string",
                  "version": "string"
               },
               "modelArn": "string",
               "traceStatus": "string"
            },
            "enabled": boolean
         }
      },
      "runtimeSettings": {
         "nluImprovement": {
            "assistedNluMode": "string",
            "enabled": boolean,
            "intentDisambiguationSettings": {
               "customDisambiguationMessage": "string",
               "enabled": boolean,
               "maxDisambiguationIntents": number
            }
         },
         "slotResolutionImprovement": {
            "bedrockModelSpecification": {
               "customPrompt": "string",
               "guardrail": {
                  "identifier": "string",
                  "version": "string"
               },
               "modelArn": "string",
               "traceStatus": "string"
            },
            "enabled": boolean
         }
      }
   },
   "localeId": "string",
   "localeName": "string",
   "nluIntentConfidenceThreshold": number,
   "speechDetectionSensitivity": "string",
   "speechRecognitionSettings": {
      "speechModelConfig": {
         "deepgramConfig": {
            "apiTokenSecretArn": "string",
            "modelId": "string"
         }
      },
      "speechModelPreference": "string"
   },
   "unifiedSpeechSettings": {
      "speechFoundationModel": {
         "modelArn": "string",
         "voiceId": "string"
      }
   },
   "voiceSettings": {
      "engine": "string",
      "voiceId": "string"
   }
}
```

## Response Elements
<a name="API_CreateBotLocale_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [audioFillerSettings](#API_CreateBotLocale_ResponseSyntax) **   <a name="lexv2-CreateBotLocale-response-audioFillerSettings"></a>
The audio filler settings configured for the created bot locale.
Type: [AudioFillerSettings](API_AudioFillerSettings.md) object

 ** [botId](#API_CreateBotLocale_ResponseSyntax) **   <a name="lexv2-CreateBotLocale-response-botId"></a>
The specified bot identifier.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botLocaleStatus](#API_CreateBotLocale_ResponseSyntax) **   <a name="lexv2-CreateBotLocale-response-botLocaleStatus"></a>
The status of the bot.
When the status is `Creating` the bot locale is being configured. When the status is `Building` Amazon Lex is building the bot for testing and use.
If the status of the bot is `ReadyExpressTesting`, you can test the bot using the exact utterances specified in the bots' intents. When the bot is ready for full testing or to run, the status is `Built`.
If there was a problem with building the bot, the status is `Failed`. If the bot was saved but not built, the status is `NotBuilt`.
Type: String
Valid Values: `Creating | Building | Built | ReadyExpressTesting | Failed | Deleting | NotBuilt | Importing | Processing`

 ** [botVersion](#API_CreateBotLocale_ResponseSyntax) **   <a name="lexv2-CreateBotLocale-response-botVersion"></a>
The specified bot version.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [creationDateTime](#API_CreateBotLocale_ResponseSyntax) **   <a name="lexv2-CreateBotLocale-response-creationDateTime"></a>
A timestamp specifying the date and time that the bot locale was created.
Type: Timestamp

 ** [description](#API_CreateBotLocale_ResponseSyntax) **   <a name="lexv2-CreateBotLocale-response-description"></a>
The specified description of the bot locale.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [generativeAISettings](#API_CreateBotLocale_ResponseSyntax) **   <a name="lexv2-CreateBotLocale-response-generativeAISettings"></a>
Contains specifications about the generative AI capabilities from Amazon Bedrock that you can turn on for your bot.
Type: [GenerativeAISettings](API_GenerativeAISettings.md) object

 ** [localeId](#API_CreateBotLocale_ResponseSyntax) **   <a name="lexv2-CreateBotLocale-response-localeId"></a>
The specified locale identifier.
Type: String

 ** [localeName](#API_CreateBotLocale_ResponseSyntax) **   <a name="lexv2-CreateBotLocale-response-localeName"></a>
The specified locale name.
Type: String

 ** [nluIntentConfidenceThreshold](#API_CreateBotLocale_ResponseSyntax) **   <a name="lexv2-CreateBotLocale-response-nluIntentConfidenceThreshold"></a>
The specified confidence threshold for inserting the `AMAZON.FallbackIntent` and `AMAZON.KendraSearchIntent` intents.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.

 ** [speechDetectionSensitivity](#API_CreateBotLocale_ResponseSyntax) **   <a name="lexv2-CreateBotLocale-response-speechDetectionSensitivity"></a>
The sensitivity level for voice activity detection (VAD) that was specified for the bot locale.
Type: String
Valid Values: `Default | HighNoiseTolerance | MaximumNoiseTolerance`

 ** [speechRecognitionSettings](#API_CreateBotLocale_ResponseSyntax) **   <a name="lexv2-CreateBotLocale-response-speechRecognitionSettings"></a>
The speech-to-text settings configured for the created bot locale.
Type: [SpeechRecognitionSettings](API_SpeechRecognitionSettings.md) object

 ** [unifiedSpeechSettings](#API_CreateBotLocale_ResponseSyntax) **   <a name="lexv2-CreateBotLocale-response-unifiedSpeechSettings"></a>
The unified speech settings configured for the created bot locale.
Type: [UnifiedSpeechSettings](API_UnifiedSpeechSettings.md) object

 ** [voiceSettings](#API_CreateBotLocale_ResponseSyntax) **   <a name="lexv2-CreateBotLocale-response-voiceSettings"></a>
The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user.
Type: [VoiceSettings](API_VoiceSettings.md) object

## Errors
<a name="API_CreateBotLocale_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** PreconditionFailedException **
Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.
HTTP Status Code: 412

 ** ServiceQuotaExceededException **
You have reached a quota for your bot.
HTTP Status Code: 402

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_CreateBotLocale_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/CreateBotLocale)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/CreateBotLocale)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/CreateBotLocale)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/CreateBotLocale)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/CreateBotLocale)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/CreateBotLocale)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/CreateBotLocale)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/CreateBotLocale)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/CreateBotLocale)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/CreateBotLocale)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
