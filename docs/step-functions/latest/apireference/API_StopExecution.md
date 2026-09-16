---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StopExecution.html
---

# StopExecution
<a name="API_StopExecution"></a>

Stops an execution.

This API action is not supported by `EXPRESS` state machines.

For an execution with encryption enabled, Step Functions will encrypt the error and cause fields using the AWS KMS key for the execution role.

A caller can stop an execution without using any AWS KMS permissions in the execution role if the caller provides a null value for both `error` and `cause` fields because no data needs to be encrypted.

## Request Syntax
<a name="API_StopExecution_RequestSyntax"></a>

```
{
   "cause": "{{string}}",
   "error": "{{string}}",
   "executionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_StopExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cause](#API_StopExecution_RequestSyntax) **   <a name="StepFunctions-StopExecution-request-cause"></a>
A more detailed explanation of the cause of the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.
Required: No

 ** [error](#API_StopExecution_RequestSyntax) **   <a name="StepFunctions-StopExecution-request-error"></a>
The error code of the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [executionArn](#API_StopExecution_RequestSyntax) **   <a name="StepFunctions-StopExecution-request-executionArn"></a>
The Amazon Resource Name (ARN) of the execution to stop.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_StopExecution_ResponseSyntax"></a>

```
{
   "stopDate": number
}
```

## Response Elements
<a name="API_StopExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [stopDate](#API_StopExecution_ResponseSyntax) **   <a name="StepFunctions-StopExecution-response-stopDate"></a>
The date the execution is stopped.
Type: Timestamp

## Errors
<a name="API_StopExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ExecutionDoesNotExist **
The specified execution does not exist.
HTTP Status Code: 400

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** KmsAccessDeniedException **
Either your AWS KMS key policy or API caller does not have the required permissions.
HTTP Status Code: 400

 ** KmsInvalidStateException **
The AWS KMS key is not in valid state, for example: Disabled or Deleted.
 ** kmsKeyState **
Current status of the AWS KMS; key. For example: `DISABLED`, `PENDING_DELETION`, `PENDING_IMPORT`, `UNAVAILABLE`, `CREATING`.
HTTP Status Code: 400

 ** KmsThrottlingException **
Received when AWS KMS returns `ThrottlingException` for a AWS KMS call that Step Functions makes on behalf of the caller.
HTTP Status Code: 400

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** reason **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StopExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/StopExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/StopExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/StopExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/StopExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/StopExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/StopExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/StopExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/StopExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/StopExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/StopExecution)
