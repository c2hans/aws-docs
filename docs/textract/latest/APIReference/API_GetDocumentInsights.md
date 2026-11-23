---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_GetDocumentInsights.html
---

# GetDocumentInsights

Gets the status and results of a document insights job that was started by [StartDocumentInsights](API_StartDocumentInsights.md).

## Request Syntax
<a name="API_GetDocumentInsights_RequestSyntax"></a>

```
{
   "JobArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDocumentInsights_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobArn](#API_GetDocumentInsights_RequestSyntax) **   <a name="Textract-GetDocumentInsights-request-JobArn"></a>
The Amazon Resource Name (ARN) of the document insights job to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:[0-9]{12}:job/[a-zA-Z0-9-_]+$`
Required: Yes

## Response Syntax
<a name="API_GetDocumentInsights_ResponseSyntax"></a>

```
{
   "ErrorMessage": "string",
   "ErrorType": "string",
   "OutputConfiguration": {
      "S3Uri": "string"
   },
   "Status": "string"
}
```

## Response Elements
<a name="API_GetDocumentInsights_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ErrorMessage](#API_GetDocumentInsights_ResponseSyntax) **   <a name="Textract-GetDocumentInsights-response-ErrorMessage"></a>
A human-readable description of the error that caused the job to fail. Present only when the job status is a failure state.
Type: String

 ** [ErrorType](#API_GetDocumentInsights_ResponseSyntax) **   <a name="Textract-GetDocumentInsights-response-ErrorType"></a>
The type of error that caused the job to fail. Present only when the job status is a failure state.
Type: String

 ** [OutputConfiguration](#API_GetDocumentInsights_ResponseSyntax) **   <a name="Textract-GetDocumentInsights-response-OutputConfiguration"></a>
The Amazon S3 location where the analysis results are written.
Type: [OutputConfiguration](API_OutputConfiguration.md) object

 ** [Status](#API_GetDocumentInsights_ResponseSyntax) **   <a name="Textract-GetDocumentInsights-response-Status"></a>
The current status of the document insights job, indicating whether it is still running, has completed, or has failed. When the job has failed, inspect `ErrorType` and `ErrorMessage` for details.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED | PARTIAL_SUCCESS`

## Errors
<a name="API_GetDocumentInsights_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Textract experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidJobIdException **
An invalid job identifier was passed to an asynchronous analysis operation.
HTTP Status Code: 400

 ** InvalidParameterException **
An input parameter violated a constraint. For example, in synchronous operations, an `InvalidParameterException` exception occurs when neither of the `S3Object` or `Bytes` values are supplied in the `Document` request parameter. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.
HTTP Status Code: 400

 ** ValidationException **
 Indicates that a request was not valid. Check request for proper formatting.
HTTP Status Code: 400

## See Also
<a name="API_GetDocumentInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/textract-2018-06-27/GetDocumentInsights)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/textract-2018-06-27/GetDocumentInsights)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/GetDocumentInsights)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/textract-2018-06-27/GetDocumentInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/GetDocumentInsights)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/textract-2018-06-27/GetDocumentInsights)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/textract-2018-06-27/GetDocumentInsights)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/textract-2018-06-27/GetDocumentInsights)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/textract-2018-06-27/GetDocumentInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/GetDocumentInsights)
