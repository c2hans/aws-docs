---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_StartDocumentInsights.html
---

# StartDocumentInsights

Starts an asynchronous job that analyzes a document using the configuration defined by a project or a set of blueprints. Use [GetDocumentInsights](API_GetDocumentInsights.md) to retrieve the results of the job.

## Request Syntax
<a name="API_StartDocumentInsights_RequestSyntax"></a>

```
{
   "Blueprints": [
      {
         "BlueprintArn": "{{string}}",
         "BlueprintVersion": "{{string}}"
      }
   ],
   "EncryptionConfiguration": {
      "KmsEncryptionContext": {
         "{{string}}" : "{{string}}"
      },
      "KmsKeyId": "{{string}}"
   },
   "InputConfiguration": {
      "S3Uri": "{{string}}"
   },
   "NotificationConfiguration": {
      "EventBridgeConfiguration": {
         "State": "{{string}}"
      }
   },
   "OutputConfiguration": {
      "S3Uri": "{{string}}"
   },
   "ProjectArn": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_StartDocumentInsights_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Blueprints](#API_StartDocumentInsights_RequestSyntax) **   <a name="Textract-StartDocumentInsights-request-Blueprints"></a>
The blueprints used to extract custom structured output from the document.
Type: Array of [BlueprintItem](API_BlueprintItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: No

 ** [EncryptionConfiguration](#API_StartDocumentInsights_RequestSyntax) **   <a name="Textract-StartDocumentInsights-request-EncryptionConfiguration"></a>
The AWS KMS encryption configuration used to encrypt the analysis output. If you don't specify a value, Amazon Textract encrypts the output using an AWS owned key.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [InputConfiguration](#API_StartDocumentInsights_RequestSyntax) **   <a name="Textract-StartDocumentInsights-request-InputConfiguration"></a>
The Amazon S3 location of the input document to analyze.
Type: [InputConfiguration](API_InputConfiguration.md) object
Required: Yes

 ** [NotificationConfiguration](#API_StartDocumentInsights_RequestSyntax) **   <a name="Textract-StartDocumentInsights-request-NotificationConfiguration"></a>
Notification settings for the job.
Type: [NotificationConfiguration](API_NotificationConfiguration.md) object
Required: No

 ** [OutputConfiguration](#API_StartDocumentInsights_RequestSyntax) **   <a name="Textract-StartDocumentInsights-request-OutputConfiguration"></a>
The Amazon S3 location where the analysis results are written.
Type: [OutputConfiguration](API_OutputConfiguration.md) object
Required: Yes

 ** [ProjectArn](#API_StartDocumentInsights_RequestSyntax) **   <a name="Textract-StartDocumentInsights-request-ProjectArn"></a>
The Amazon Resource Name (ARN) of the project whose configuration is used to analyze the document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:(aws|[0-9]{12}):project/[a-zA-Z0-9-]{12,36}$`
Required: No

 ** [Tags](#API_StartDocumentInsights_RequestSyntax) **   <a name="Textract-StartDocumentInsights-request-Tags"></a>
A set of tags (key-value pairs) to assign to the document insights job.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_StartDocumentInsights_ResponseSyntax"></a>

```
{
   "JobArn": "string"
}
```

## Response Elements
<a name="API_StartDocumentInsights_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobArn](#API_StartDocumentInsights_ResponseSyntax) **   <a name="Textract-StartDocumentInsights-response-JobArn"></a>
The Amazon Resource Name (ARN) of the document insights job that was started. Use it with [GetDocumentInsights](API_GetDocumentInsights.md) to retrieve the results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:[0-9]{12}:job/[a-zA-Z0-9-_]+$`

## Errors
<a name="API_StartDocumentInsights_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Textract experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
An input parameter violated a constraint. For example, in synchronous operations, an `InvalidParameterException` exception occurs when neither of the `S3Object` or `Bytes` values are supplied in the `Document` request parameter. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** LimitExceededException **
An Amazon Textract service limit was exceeded. For example, if you start too many asynchronous jobs concurrently, calls to start operations (`StartDocumentTextDetection`, for example) raise a LimitExceededException exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Textract service limit.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 Returned when an operation tried to access a nonexistent resource.
HTTP Status Code: 400

 ** ValidationException **
 Indicates that a request was not valid. Check request for proper formatting.
HTTP Status Code: 400

## See Also
<a name="API_StartDocumentInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/textract-2018-06-27/StartDocumentInsights)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/textract-2018-06-27/StartDocumentInsights)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/StartDocumentInsights)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/textract-2018-06-27/StartDocumentInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/StartDocumentInsights)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/textract-2018-06-27/StartDocumentInsights)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/textract-2018-06-27/StartDocumentInsights)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/textract-2018-06-27/StartDocumentInsights)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/textract-2018-06-27/StartDocumentInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/StartDocumentInsights)
