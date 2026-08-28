---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_CancelQuantumTask.html
---

# CancelQuantumTask
<a name="API_CancelQuantumTask"></a>

Cancels the specified task.

## Request Syntax
<a name="API_CancelQuantumTask_RequestSyntax"></a>

```
PUT /quantum-task/{{quantumTaskArn}}/cancel HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CancelQuantumTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [quantumTaskArn](#API_CancelQuantumTask_RequestSyntax) **   <a name="braket-CancelQuantumTask-request-uri-quantumTaskArn"></a>
The ARN of the quantum task to cancel.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_CancelQuantumTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CancelQuantumTask_RequestSyntax) **   <a name="braket-CancelQuantumTask-request-clientToken"></a>
The client token associated with the cancellation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_CancelQuantumTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "cancellationStatus": "string",
   "quantumTaskArn": "string"
}
```

## Response Elements
<a name="API_CancelQuantumTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cancellationStatus](#API_CancelQuantumTask_ResponseSyntax) **   <a name="braket-CancelQuantumTask-response-cancellationStatus"></a>
The status of the quantum task.
Type: String
Valid Values: `CANCELLING | CANCELLED`

 ** [quantumTaskArn](#API_CancelQuantumTask_ResponseSyntax) **   <a name="braket-CancelQuantumTask-response-quantumTaskArn"></a>
The ARN of the quantum task.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CancelQuantumTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
An error occurred due to a conflict.
HTTP Status Code: 409

 ** InternalServiceException **
The request failed because of an unknown error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The API throttling rate limit is exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input request failed to satisfy constraints expected by Amazon Braket.
 ** programSetValidationFailures **
The validation failures in the program set submitted in the request.
 ** reason **
The reason for validation failure.
HTTP Status Code: 400

## See Also
<a name="API_CancelQuantumTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/braket-2019-09-01/CancelQuantumTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/braket-2019-09-01/CancelQuantumTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/CancelQuantumTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/braket-2019-09-01/CancelQuantumTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/CancelQuantumTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/braket-2019-09-01/CancelQuantumTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/braket-2019-09-01/CancelQuantumTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/braket-2019-09-01/CancelQuantumTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/braket-2019-09-01/CancelQuantumTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/CancelQuantumTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
