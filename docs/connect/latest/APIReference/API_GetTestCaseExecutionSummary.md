---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_GetTestCaseExecutionSummary.html
---

# GetTestCaseExecutionSummary
<a name="API_GetTestCaseExecutionSummary"></a>

Retrieves an overview of a test execution that includes the status of the execution, start and end time, and observation summary.

## Request Syntax
<a name="API_GetTestCaseExecutionSummary_RequestSyntax"></a>

```
GET /test-cases/{{InstanceId}}/{{TestCaseId}}/{{TestCaseExecutionId}}/summary HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTestCaseExecutionSummary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_GetTestCaseExecutionSummary_RequestSyntax) **   <a name="connect-GetTestCaseExecutionSummary-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [TestCaseExecutionId](#API_GetTestCaseExecutionSummary_RequestSyntax) **   <a name="connect-GetTestCaseExecutionSummary-request-uri-TestCaseExecutionId"></a>
The identifier of the test case execution.
Length Constraints: Maximum length of 500.
Required: Yes

 ** [TestCaseId](#API_GetTestCaseExecutionSummary_RequestSyntax) **   <a name="connect-GetTestCaseExecutionSummary-request-uri-TestCaseId"></a>
The identifier of the test case.
Length Constraints: Maximum length of 500.
Required: Yes

## Request Body
<a name="API_GetTestCaseExecutionSummary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTestCaseExecutionSummary_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EndTime": number,
   "ObservationSummary": {
      "ObservationsFailed": number,
      "ObservationsPassed": number,
      "TotalObservations": number
   },
   "StartTime": number,
   "Status": "string"
}
```

## Response Elements
<a name="API_GetTestCaseExecutionSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndTime](#API_GetTestCaseExecutionSummary_ResponseSyntax) **   <a name="connect-GetTestCaseExecutionSummary-response-EndTime"></a>
The timestamp when the test case execution ended.
Type: Timestamp

 ** [ObservationSummary](#API_GetTestCaseExecutionSummary_ResponseSyntax) **   <a name="connect-GetTestCaseExecutionSummary-response-ObservationSummary"></a>
Summary statistics for the test case execution.
Type: [ObservationSummary](API_ObservationSummary.md) object

 ** [StartTime](#API_GetTestCaseExecutionSummary_ResponseSyntax) **   <a name="connect-GetTestCaseExecutionSummary-response-StartTime"></a>
The timestamp when the test case execution started.
Type: Timestamp

 ** [Status](#API_GetTestCaseExecutionSummary_ResponseSyntax) **   <a name="connect-GetTestCaseExecutionSummary-response-Status"></a>
The status of the test case execution.
Type: String
Valid Values: `INITIATED | PASSED | FAILED | IN_PROGRESS | STOPPED`

## Errors
<a name="API_GetTestCaseExecutionSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_GetTestCaseExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/GetTestCaseExecutionSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/GetTestCaseExecutionSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/GetTestCaseExecutionSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/GetTestCaseExecutionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/GetTestCaseExecutionSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/GetTestCaseExecutionSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/GetTestCaseExecutionSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/GetTestCaseExecutionSummary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/GetTestCaseExecutionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/GetTestCaseExecutionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
