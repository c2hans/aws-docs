---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateBotLocale.html
---

# UpdateBotLocale
<a name="API_UpdateBotLocale"></a>

Updates the settings that a bot has for a specific locale.

## Request Syntax
<a name="API_UpdateBotLocale_RequestSyntax"></a>

```
PUT /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/ HTTP/1.1
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
   "nluIntentConfidenceThreshold": {{number}},
   "speakerDiarizationSettings": {
      "enabled": {{boolean}}
   },
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
<a name="API_UpdateBotLocale_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_UpdateBotLocale_RequestSyntax) **   <a name="lexv2-UpdateBotLocale-request-uri-botId"></a>
The unique identifier of the bot that contains the locale.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_UpdateBotLocale_RequestSyntax) **   <a name="lexv2-UpdateBotLocale-request-uri-botVersion"></a>
The version of the bot that contains the locale to be updated. The version can only be the `DRAFT` version.
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`
Required: Yes

 ** [localeId](#API_UpdateBotLocale_RequestSyntax) **   <a name="lexv2-UpdateBotLocale-request-uri-localeId"></a>
The identifier of the language and locale to update. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Required: Yes

## Request Body
<a name="API_UpdateBotLocale_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [audioFillerSettings](#API_UpdateBotLocale_RequestSyntax) **   <a name="lexv2-UpdateBotLocale-request-audioFillerSettings"></a>
Updated audio filler settings to apply to the bot locale. When enabled, requires `unifiedSpeechSettings` (speech-to-speech) to be configured on the bot locale.
Type: [AudioFillerSettings](API_AudioFillerSettings.md) object
Required: No

 ** [description](#API_UpdateBotLocale_RequestSyntax) **   <a name="lexv2-UpdateBotLocale-request-description"></a>
The new description of the locale.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** [generativeAISettings](#API_UpdateBotLocale_RequestSyntax) **   <a name="lexv2-UpdateBotLocale-request-generativeAISettings"></a>
Contains settings for generative AI features powered by Amazon Bedrock for your bot locale. Use this object to turn generative AI features on and off. Pricing may differ if you turn a feature on. For more information, see LINK.
Type: [GenerativeAISettings](API_GenerativeAISettings.md) object
Required: No

 ** [nluIntentConfidenceThreshold](#API_UpdateBotLocale_RequestSyntax) **   <a name="lexv2-UpdateBotLocale-request-nluIntentConfidenceThreshold"></a>
The new confidence threshold where Amazon Lex inserts the `AMAZON.FallbackIntent` and `AMAZON.KendraSearchIntent` intents in the list of possible intents for an utterance.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

 ** [speakerDiarizationSettings](#API_UpdateBotLocale_RequestSyntax) **   <a name="lexv2-UpdateBotLocale-request-speakerDiarizationSettings"></a>
The updated speaker diarization settings to apply to the bot locale. If you omit this field, Amazon Lex keeps the setting currently stored on the bot locale. To turn speaker diarization off, set `enabled` to `false` explicitly.
Type: [SpeakerDiarizationSettings](API_SpeakerDiarizationSettings.md) object
Required: No

 ** [speechDetectionSensitivity](#API_UpdateBotLocale_RequestSyntax) **   <a name="lexv2-UpdateBotLocale-request-speechDetectionSensitivity"></a>
The new sensitivity level for voice activity detection (VAD) in the bot locale. This setting helps optimize speech recognition accuracy by adjusting how the system responds to background noise during voice interactions.
Type: String
Valid Values: `Default | HighNoiseTolerance | MaximumNoiseTolerance`
Required: No

 ** [speechRecognitionSettings](#API_UpdateBotLocale_RequestSyntax) **   <a name="lexv2-UpdateBotLocale-request-speechRecognitionSettings"></a>
Updated speech-to-text settings to apply to the bot locale.
Type: [SpeechRecognitionSettings](API_SpeechRecognitionSettings.md) object
Required: No

 ** [unifiedSpeechSettings](#API_UpdateBotLocale_RequestSyntax) **   <a name="lexv2-UpdateBotLocale-request-unifiedSpeechSettings"></a>
Updated unified speech settings to apply to the bot locale.
Type: [UnifiedSpeechSettings](API_UnifiedSpeechSettings.md) object
Required: No

 ** [voiceSettings](#API_UpdateBotLocale_RequestSyntax) **   <a name="lexv2-UpdateBotLocale-request-voiceSettings"></a>
The new Amazon Polly voice Amazon Lex should use for voice interaction with the user.
Type: [VoiceSettings](API_VoiceSettings.md) object
Required: No

## Response Syntax
<a name="API_UpdateBotLocale_ResponseSyntax"></a>

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
   "failureReasons": [ "string" ],
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
   "lastUpdatedDateTime": number,
   "localeId": "string",
   "localeName": "string",
   "nluIntentConfidenceThreshold": number,
   "recommendedActions": [ "string" ],
   "speakerDiarizationSettings": {
      "enabled": boolean
   },
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
<a name="API_UpdateBotLocale_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [audioFillerSettings](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-audioFillerSettings"></a>
The updated audio filler settings for the bot locale.
Type: [AudioFillerSettings](API_AudioFillerSettings.md) object

 ** [botId](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-botId"></a>
The identifier of the bot that contains the updated locale.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botLocaleStatus](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-botLocaleStatus"></a>
The current status of the locale. When the bot status is `Built` the locale is ready for use.
Type: String
Valid Values: `Creating | Building | Built | ReadyExpressTesting | Failed | Deleting | NotBuilt | Importing | Processing`

 ** [botVersion](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-botVersion"></a>
The version of the bot that contains the updated locale.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [creationDateTime](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-creationDateTime"></a>
A timestamp of the date and time that the locale was created.
Type: Timestamp

 ** [description](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-description"></a>
The updated description of the locale.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [failureReasons](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-failureReasons"></a>
If the `botLocaleStatus` is `Failed`, the `failureReasons` field lists the errors that occurred while building the bot.
Type: Array of strings

 ** [generativeAISettings](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-generativeAISettings"></a>
Contains settings for generative AI features powered by Amazon Bedrock for your bot locale.
Type: [GenerativeAISettings](API_GenerativeAISettings.md) object

 ** [lastUpdatedDateTime](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-lastUpdatedDateTime"></a>
A timestamp of the date and time that the locale was last updated.
Type: Timestamp

 ** [localeId](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-localeId"></a>
The language and locale of the updated bot locale.
Type: String

 ** [localeName](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-localeName"></a>
The updated locale name for the locale.
Type: String

 ** [nluIntentConfidenceThreshold](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-nluIntentConfidenceThreshold"></a>
The updated confidence threshold for inserting the `AMAZON.FallbackIntent` and `AMAZON.KendraSearchIntent` intents in the list of possible intents for an utterance.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.

 ** [recommendedActions](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-recommendedActions"></a>
Recommended actions to take to resolve an error in the `failureReasons` field.
Type: Array of strings

 ** [speakerDiarizationSettings](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-speakerDiarizationSettings"></a>
The updated speaker diarization settings for the bot locale.
Type: [SpeakerDiarizationSettings](API_SpeakerDiarizationSettings.md) object

 ** [speechDetectionSensitivity](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-speechDetectionSensitivity"></a>
The updated sensitivity level for voice activity detection (VAD) in the bot locale.
Type: String
Valid Values: `Default | HighNoiseTolerance | MaximumNoiseTolerance`

 ** [speechRecognitionSettings](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-speechRecognitionSettings"></a>
The updated speech-to-text settings for the bot locale.
Type: [SpeechRecognitionSettings](API_SpeechRecognitionSettings.md) object

 ** [unifiedSpeechSettings](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-unifiedSpeechSettings"></a>
The updated unified speech settings for the bot locale.
Type: [UnifiedSpeechSettings](API_UnifiedSpeechSettings.md) object

 ** [voiceSettings](#API_UpdateBotLocale_ResponseSyntax) **   <a name="lexv2-UpdateBotLocale-response-voiceSettings"></a>
The updated Amazon Polly voice to use for voice interaction with the user.
Type: [VoiceSettings](API_VoiceSettings.md) object

## Errors
<a name="API_UpdateBotLocale_Errors"></a>

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
<a name="API_UpdateBotLocale_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/UpdateBotLocale)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/UpdateBotLocale)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UpdateBotLocale)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/UpdateBotLocale)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UpdateBotLocale)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/UpdateBotLocale)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/UpdateBotLocale)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/UpdateBotLocale)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/UpdateBotLocale)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UpdateBotLocale)
