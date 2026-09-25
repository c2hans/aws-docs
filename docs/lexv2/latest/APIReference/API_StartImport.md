---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartImport.html
---

# StartImport
<a name="API_StartImport"></a>

Starts importing a bot, bot locale, or custom vocabulary from a zip archive that you uploaded to an S3 bucket.

## Request Syntax
<a name="API_StartImport_RequestSyntax"></a>

```
PUT /imports/ HTTP/1.1
Content-type: application/json

{
   "filePassword": "{{string}}",
   "importId": "{{string}}",
   "mergeStrategy": "{{string}}",
   "resourceSpecification": {
      "botImportSpecification": {
         "botName": "{{string}}",
         "botTags": {
            "{{string}}" : "{{string}}"
         },
         "dataPrivacy": {
            "childDirected": {{boolean}}
         },
         "errorLogSettings": {
            "enabled": {{boolean}}
         },
         "idleSessionTTLInSeconds": {{number}},
         "roleArn": "{{string}}",
         "testBotAliasTags": {
            "{{string}}" : "{{string}}"
         }
      },
      "botLocaleImportSpecification": {
         "audioFillerSettings": {
            "audioType": "{{string}}",
            "enabled": {{boolean}},
            "minimumPlayDurationInMilliseconds": {{number}},
            "responseDeliveryDelayInMilliseconds": {{number}},
            "startDelayInMilliseconds": {{number}}
         },
         "botId": "{{string}}",
         "botVersion": "{{string}}",
         "localeId": "{{string}}",
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
      },
      "customVocabularyImportSpecification": {
         "botId": "{{string}}",
         "botVersion": "{{string}}",
         "localeId": "{{string}}"
      },
      "testSetImportResourceSpecification": {
         "description": "{{string}}",
         "importInputLocation": {
            "s3BucketName": "{{string}}",
            "s3Path": "{{string}}"
         },
         "modality": "{{string}}",
         "roleArn": "{{string}}",
         "storageLocation": {
            "kmsKeyArn": "{{string}}",
            "s3BucketName": "{{string}}",
            "s3Path": "{{string}}"
         },
         "testSetName": "{{string}}",
         "testSetTags": {
            "{{string}}" : "{{string}}"
         }
      }
   }
}
```

## URI Request Parameters
<a name="API_StartImport_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartImport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filePassword](#API_StartImport_RequestSyntax) **   <a name="lexv2-StartImport-request-filePassword"></a>
The password used to encrypt the zip archive that contains the resource definition. You should always encrypt the zip archive to protect it during transit between your site and Amazon Lex.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [importId](#API_StartImport_RequestSyntax) **   <a name="lexv2-StartImport-request-importId"></a>
The unique identifier for the import. It is included in the response from the [CreateUploadUrl](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateUploadUrl.html) operation.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [mergeStrategy](#API_StartImport_RequestSyntax) **   <a name="lexv2-StartImport-request-mergeStrategy"></a>
The strategy to use when there is a name conflict between the imported resource and an existing resource. When the merge strategy is `FailOnConflict` existing resources are not overwritten and the import fails.
Type: String
Valid Values: `Overwrite | FailOnConflict | Append`
Required: Yes

 ** [resourceSpecification](#API_StartImport_RequestSyntax) **   <a name="lexv2-StartImport-request-resourceSpecification"></a>
Parameters for creating the bot, bot locale or custom vocabulary.
Type: [ImportResourceSpecification](API_ImportResourceSpecification.md) object
Required: Yes

## Response Syntax
<a name="API_StartImport_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "creationDateTime": number,
   "importId": "string",
   "importStatus": "string",
   "mergeStrategy": "string",
   "resourceSpecification": {
      "botImportSpecification": {
         "botName": "string",
         "botTags": {
            "string" : "string"
         },
         "dataPrivacy": {
            "childDirected": boolean
         },
         "errorLogSettings": {
            "enabled": boolean
         },
         "idleSessionTTLInSeconds": number,
         "roleArn": "string",
         "testBotAliasTags": {
            "string" : "string"
         }
      },
      "botLocaleImportSpecification": {
         "audioFillerSettings": {
            "audioType": "string",
            "enabled": boolean,
            "minimumPlayDurationInMilliseconds": number,
            "responseDeliveryDelayInMilliseconds": number,
            "startDelayInMilliseconds": number
         },
         "botId": "string",
         "botVersion": "string",
         "localeId": "string",
         "nluIntentConfidenceThreshold": number,
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
      },
      "customVocabularyImportSpecification": {
         "botId": "string",
         "botVersion": "string",
         "localeId": "string"
      },
      "testSetImportResourceSpecification": {
         "description": "string",
         "importInputLocation": {
            "s3BucketName": "string",
            "s3Path": "string"
         },
         "modality": "string",
         "roleArn": "string",
         "storageLocation": {
            "kmsKeyArn": "string",
            "s3BucketName": "string",
            "s3Path": "string"
         },
         "testSetName": "string",
         "testSetTags": {
            "string" : "string"
         }
      }
   }
}
```

## Response Elements
<a name="API_StartImport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [creationDateTime](#API_StartImport_ResponseSyntax) **   <a name="lexv2-StartImport-response-creationDateTime"></a>
The date and time that the import request was created.
Type: Timestamp

 ** [importId](#API_StartImport_ResponseSyntax) **   <a name="lexv2-StartImport-response-importId"></a>
A unique identifier for the import.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [importStatus](#API_StartImport_ResponseSyntax) **   <a name="lexv2-StartImport-response-importStatus"></a>
The current status of the import. When the status is `Complete` the bot, bot alias, or custom vocabulary is ready to use.
Type: String
Valid Values: `InProgress | Completed | Failed | Deleting`

 ** [mergeStrategy](#API_StartImport_ResponseSyntax) **   <a name="lexv2-StartImport-response-mergeStrategy"></a>
The strategy used when there was a name conflict between the imported resource and an existing resource. When the merge strategy is `FailOnConflict` existing resources are not overwritten and the import fails.
Type: String
Valid Values: `Overwrite | FailOnConflict | Append`

 ** [resourceSpecification](#API_StartImport_ResponseSyntax) **   <a name="lexv2-StartImport-response-resourceSpecification"></a>
The parameters used when importing the resource.
Type: [ImportResourceSpecification](API_ImportResourceSpecification.md) object

## Errors
<a name="API_StartImport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

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
<a name="API_StartImport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/StartImport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/StartImport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/StartImport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/StartImport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/StartImport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/StartImport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/StartImport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/StartImport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/StartImport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/StartImport)
