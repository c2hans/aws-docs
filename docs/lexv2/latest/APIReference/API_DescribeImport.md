---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeImport.html
---

# DescribeImport
<a name="API_DescribeImport"></a>

Gets information about a specific import.

## Request Syntax
<a name="API_DescribeImport_RequestSyntax"></a>

```
GET /imports/{{importId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeImport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [importId](#API_DescribeImport_RequestSyntax) **   <a name="lexv2-DescribeImport-request-uri-importId"></a>
The unique identifier of the import to describe.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_DescribeImport_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeImport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationDateTime": number,
   "failureReasons": [ "string" ],
   "importedResourceId": "string",
   "importedResourceName": "string",
   "importId": "string",
   "importStatus": "string",
   "lastUpdatedDateTime": number,
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
<a name="API_DescribeImport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDateTime](#API_DescribeImport_ResponseSyntax) **   <a name="lexv2-DescribeImport-response-creationDateTime"></a>
The date and time that the import was created.
Type: Timestamp

 ** [failureReasons](#API_DescribeImport_ResponseSyntax) **   <a name="lexv2-DescribeImport-response-failureReasons"></a>
If the `importStatus` field is `Failed`, this provides one or more reasons for the failure.
Type: Array of strings

 ** [importedResourceId](#API_DescribeImport_ResponseSyntax) **   <a name="lexv2-DescribeImport-response-importedResourceId"></a>
The unique identifier that Amazon Lex assigned to the resource created by the import.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 10.
Pattern: `^([0-9a-zA-Z_])+$`

 ** [importedResourceName](#API_DescribeImport_ResponseSyntax) **   <a name="lexv2-DescribeImport-response-importedResourceName"></a>
The name of the imported resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

 ** [importId](#API_DescribeImport_ResponseSyntax) **   <a name="lexv2-DescribeImport-response-importId"></a>
The unique identifier of the described import.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [importStatus](#API_DescribeImport_ResponseSyntax) **   <a name="lexv2-DescribeImport-response-importStatus"></a>
The status of the import process. When the status is `Completed` the resource is imported and ready for use.
Type: String
Valid Values: `InProgress | Completed | Failed | Deleting`

 ** [lastUpdatedDateTime](#API_DescribeImport_ResponseSyntax) **   <a name="lexv2-DescribeImport-response-lastUpdatedDateTime"></a>
The date and time that the import was last updated.
Type: Timestamp

 ** [mergeStrategy](#API_DescribeImport_ResponseSyntax) **   <a name="lexv2-DescribeImport-response-mergeStrategy"></a>
The strategy used when there was a name conflict between the imported resource and an existing resource. When the merge strategy is `FailOnConflict` existing resources are not overwritten and the import fails.
Type: String
Valid Values: `Overwrite | FailOnConflict | Append`

 ** [resourceSpecification](#API_DescribeImport_ResponseSyntax) **   <a name="lexv2-DescribeImport-response-resourceSpecification"></a>
The specifications of the imported bot, bot locale, or custom vocabulary.
Type: [ImportResourceSpecification](API_ImportResourceSpecification.md) object

## Errors
<a name="API_DescribeImport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_DescribeImport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DescribeImport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DescribeImport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescribeImport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DescribeImport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescribeImport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DescribeImport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DescribeImport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DescribeImport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DescribeImport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescribeImport)
