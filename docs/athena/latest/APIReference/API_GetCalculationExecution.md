---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_GetCalculationExecution.html
---

# GetCalculationExecution
<a name="API_GetCalculationExecution"></a>

Describes a previously submitted calculation execution.

## Request Syntax
<a name="API_GetCalculationExecution_RequestSyntax"></a>

```
{
   "CalculationExecutionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCalculationExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CalculationExecutionId](#API_GetCalculationExecution_RequestSyntax) **   <a name="athena-GetCalculationExecution-request-CalculationExecutionId"></a>
The calculation execution UUID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

## Response Syntax
<a name="API_GetCalculationExecution_ResponseSyntax"></a>

```
{
   "CalculationExecutionId": "string",
   "Description": "string",
   "Result": {
      "ResultS3Uri": "string",
      "ResultType": "string",
      "StdErrorS3Uri": "string",
      "StdOutS3Uri": "string"
   },
   "SessionId": "string",
   "Statistics": {
      "DpuExecutionInMillis": number,
      "Progress": "string"
   },
   "Status": {
      "CompletionDateTime": number,
      "State": "string",
      "StateChangeReason": "string",
      "SubmissionDateTime": number
   },
   "WorkingDirectory": "string"
}
```

## Response Elements
<a name="API_GetCalculationExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CalculationExecutionId](#API_GetCalculationExecution_ResponseSyntax) **   <a name="athena-GetCalculationExecution-response-CalculationExecutionId"></a>
The calculation execution UUID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.

 ** [Description](#API_GetCalculationExecution_ResponseSyntax) **   <a name="athena-GetCalculationExecution-response-Description"></a>
The description of the calculation execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [Result](#API_GetCalculationExecution_ResponseSyntax) **   <a name="athena-GetCalculationExecution-response-Result"></a>
Contains result information. This field is populated only if the calculation is completed.
Type: [CalculationResult](API_CalculationResult.md) object

 ** [SessionId](#API_GetCalculationExecution_ResponseSyntax) **   <a name="athena-GetCalculationExecution-response-SessionId"></a>
The session ID that the calculation ran in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [Statistics](#API_GetCalculationExecution_ResponseSyntax) **   <a name="athena-GetCalculationExecution-response-Statistics"></a>
Contains information about the data processing unit (DPU) execution time and progress. This field is populated only when statistics are available.
Type: [CalculationStatistics](API_CalculationStatistics.md) object

 ** [Status](#API_GetCalculationExecution_ResponseSyntax) **   <a name="athena-GetCalculationExecution-response-Status"></a>
Contains information about the status of the calculation.
Type: [CalculationStatus](API_CalculationStatus.md) object

 ** [WorkingDirectory](#API_GetCalculationExecution_ResponseSyntax) **   <a name="athena-GetCalculationExecution-response-WorkingDirectory"></a>
The Amazon S3 location in which calculation results are stored.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^(https|s3|S3)://([^/]+)/?(.*)$`

## Errors
<a name="API_GetCalculationExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource, such as a workgroup, was not found.
 ** ResourceName **
The name of the Amazon resource.
HTTP Status Code: 400

## See Also
<a name="API_GetCalculationExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/GetCalculationExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/GetCalculationExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/GetCalculationExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/GetCalculationExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/GetCalculationExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/GetCalculationExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/GetCalculationExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/GetCalculationExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetCalculationExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/GetCalculationExecution)
