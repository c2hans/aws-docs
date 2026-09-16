---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartBotRecommendation.html
---

# StartBotRecommendation
<a name="API_StartBotRecommendation"></a>

Use this to provide your transcript data, and to start the bot recommendation process.

## Request Syntax
<a name="API_StartBotRecommendation_RequestSyntax"></a>

```
PUT /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/botrecommendations/ HTTP/1.1
Content-type: application/json

{
   "encryptionSetting": {
      "associatedTranscriptsPassword": "{{string}}",
      "botLocaleExportPassword": "{{string}}",
      "kmsKeyArn": "{{string}}"
   },
   "transcriptSourceSetting": {
      "s3BucketTranscriptSource": {
         "kmsKeyArn": "{{string}}",
         "pathFormat": {
            "objectPrefixes": [ "{{string}}" ]
         },
         "s3BucketName": "{{string}}",
         "transcriptFilter": {
            "lexTranscriptFilter": {
               "dateRangeFilter": {
                  "endDateTime": {{number}},
                  "startDateTime": {{number}}
               }
            }
         },
         "transcriptFormat": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_StartBotRecommendation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_StartBotRecommendation_RequestSyntax) **   <a name="lexv2-StartBotRecommendation-request-uri-botId"></a>
The unique identifier of the bot containing the bot recommendation.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_StartBotRecommendation_RequestSyntax) **   <a name="lexv2-StartBotRecommendation-request-uri-botVersion"></a>
The version of the bot containing the bot recommendation.
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`
Required: Yes

 ** [localeId](#API_StartBotRecommendation_RequestSyntax) **   <a name="lexv2-StartBotRecommendation-request-uri-localeId"></a>
The identifier of the language and locale of the bot recommendation to start. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html)
Required: Yes

## Request Body
<a name="API_StartBotRecommendation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [encryptionSetting](#API_StartBotRecommendation_RequestSyntax) **   <a name="lexv2-StartBotRecommendation-request-encryptionSetting"></a>
The object representing the passwords that will be used to encrypt the data related to the bot recommendation results, as well as the AWS KMS key ARN used to encrypt the associated metadata.
Type: [EncryptionSetting](API_EncryptionSetting.md) object
Required: No

 ** [transcriptSourceSetting](#API_StartBotRecommendation_RequestSyntax) **   <a name="lexv2-StartBotRecommendation-request-transcriptSourceSetting"></a>
The object representing the Amazon S3 bucket containing the transcript, as well as the associated metadata.
Type: [TranscriptSourceSetting](API_TranscriptSourceSetting.md) object
Required: Yes

## Response Syntax
<a name="API_StartBotRecommendation_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "botId": "string",
   "botRecommendationId": "string",
   "botRecommendationStatus": "string",
   "botVersion": "string",
   "creationDateTime": number,
   "encryptionSetting": {
      "associatedTranscriptsPassword": "string",
      "botLocaleExportPassword": "string",
      "kmsKeyArn": "string"
   },
   "localeId": "string",
   "transcriptSourceSetting": {
      "s3BucketTranscriptSource": {
         "kmsKeyArn": "string",
         "pathFormat": {
            "objectPrefixes": [ "string" ]
         },
         "s3BucketName": "string",
         "transcriptFilter": {
            "lexTranscriptFilter": {
               "dateRangeFilter": {
                  "endDateTime": number,
                  "startDateTime": number
               }
            }
         },
         "transcriptFormat": "string"
      }
   }
}
```

## Response Elements
<a name="API_StartBotRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_StartBotRecommendation_ResponseSyntax) **   <a name="lexv2-StartBotRecommendation-response-botId"></a>
The unique identifier of the bot containing the bot recommendation.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botRecommendationId](#API_StartBotRecommendation_ResponseSyntax) **   <a name="lexv2-StartBotRecommendation-response-botRecommendationId"></a>
The identifier of the bot recommendation that you have created.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botRecommendationStatus](#API_StartBotRecommendation_ResponseSyntax) **   <a name="lexv2-StartBotRecommendation-response-botRecommendationStatus"></a>
The status of the bot recommendation.
If the status is Failed, then the reasons for the failure are listed in the failureReasons field.
Type: String
Valid Values: `Processing | Deleting | Deleted | Downloading | Updating | Available | Failed | Stopping | Stopped`

 ** [botVersion](#API_StartBotRecommendation_ResponseSyntax) **   <a name="lexv2-StartBotRecommendation-response-botVersion"></a>
The version of the bot containing the bot recommendation.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [creationDateTime](#API_StartBotRecommendation_ResponseSyntax) **   <a name="lexv2-StartBotRecommendation-response-creationDateTime"></a>
A timestamp of the date and time that the bot recommendation was created.
Type: Timestamp

 ** [encryptionSetting](#API_StartBotRecommendation_ResponseSyntax) **   <a name="lexv2-StartBotRecommendation-response-encryptionSetting"></a>
The object representing the passwords that were used to encrypt the data related to the bot recommendation results, as well as the AWS KMS key ARN used to encrypt the associated metadata.
Type: [EncryptionSetting](API_EncryptionSetting.md) object

 ** [localeId](#API_StartBotRecommendation_ResponseSyntax) **   <a name="lexv2-StartBotRecommendation-response-localeId"></a>
The identifier of the language and locale of the bot recommendation to start. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html)
Type: String

 ** [transcriptSourceSetting](#API_StartBotRecommendation_ResponseSyntax) **   <a name="lexv2-StartBotRecommendation-response-transcriptSourceSetting"></a>
The object representing the Amazon S3 bucket containing the transcript, as well as the associated metadata.
Type: [TranscriptSourceSetting](API_TranscriptSourceSetting.md) object

## Errors
<a name="API_StartBotRecommendation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** PreconditionFailedException **
Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.
HTTP Status Code: 412

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
<a name="API_StartBotRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/StartBotRecommendation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/StartBotRecommendation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/StartBotRecommendation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/StartBotRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/StartBotRecommendation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/StartBotRecommendation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/StartBotRecommendation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/StartBotRecommendation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/StartBotRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/StartBotRecommendation)
