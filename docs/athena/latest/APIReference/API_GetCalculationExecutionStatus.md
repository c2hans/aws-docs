---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_GetCalculationExecutionStatus.html
---

# GetCalculationExecutionStatus
<a name="API_GetCalculationExecutionStatus"></a>

Gets the status of a current calculation.

## Request Syntax
<a name="API_GetCalculationExecutionStatus_RequestSyntax"></a>

```
{
   "CalculationExecutionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCalculationExecutionStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CalculationExecutionId](#API_GetCalculationExecutionStatus_RequestSyntax) **   <a name="athena-GetCalculationExecutionStatus-request-CalculationExecutionId"></a>
The calculation execution UUID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

## Response Syntax
<a name="API_GetCalculationExecutionStatus_ResponseSyntax"></a>

```
{
   "Statistics": {
      "DpuExecutionInMillis": number,
      "Progress": "string"
   },
   "Status": {
      "CompletionDateTime": number,
      "State": "string",
      "StateChangeReason": "string",
      "SubmissionDateTime": number
   }
}
```

## Response Elements
<a name="API_GetCalculationExecutionStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Statistics](#API_GetCalculationExecutionStatus_ResponseSyntax) **   <a name="athena-GetCalculationExecutionStatus-response-Statistics"></a>
Contains information about the DPU execution time and progress.
Type: [CalculationStatistics](API_CalculationStatistics.md) object

 ** [Status](#API_GetCalculationExecutionStatus_ResponseSyntax) **   <a name="athena-GetCalculationExecutionStatus-response-Status"></a>
Contains information about the calculation execution status.
Type: [CalculationStatus](API_CalculationStatus.md) object

## Errors
<a name="API_GetCalculationExecutionStatus_Errors"></a>

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
<a name="API_GetCalculationExecutionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/GetCalculationExecutionStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/GetCalculationExecutionStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/GetCalculationExecutionStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/GetCalculationExecutionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/GetCalculationExecutionStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/GetCalculationExecutionStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/GetCalculationExecutionStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/GetCalculationExecutionStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetCalculationExecutionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/GetCalculationExecutionStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
