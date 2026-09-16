---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartSyncExecution.html
---

# StartSyncExecution
<a name="API_StartSyncExecution"></a>

Starts a Synchronous Express state machine execution. `StartSyncExecution` is not available for `STANDARD` workflows.

**Note**
 `StartSyncExecution` will return a `200 OK` response, even if your execution fails, because the status code in the API response doesn't reflect function errors. Error codes are reserved for errors that prevent your execution from running, such as permissions errors, limit errors, or issues with your state machine code and configuration.

## Request Syntax
<a name="API_StartSyncExecution_RequestSyntax"></a>

```
{
   "includedData": "{{string}}",
   "input": "{{string}}",
   "name": "{{string}}",
   "stateMachineArn": "{{string}}",
   "traceHeader": "{{string}}"
}
```

## Request Parameters
<a name="API_StartSyncExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [includedData](#API_StartSyncExecution_RequestSyntax) **   <a name="StepFunctions-StartSyncExecution-request-includedData"></a>
If your state machine definition is encrypted with a AWS KMS key, callers must have `kms:Decrypt` permission to decrypt the definition. Alternatively, you can call the API with `includedData = METADATA_ONLY` to get a successful response without the encrypted definition.
Type: String
Valid Values: `ALL_DATA | METADATA_ONLY`
Required: No

 ** [input](#API_StartSyncExecution_RequestSyntax) **   <a name="StepFunctions-StartSyncExecution-request-input"></a>
The string that contains the JSON input data for the execution, for example:
 `"{\"first_name\" : \"Alejandro\"}"`
If you don't include any JSON input data, you still must include the two braces, for example: `"{}"`
Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** [name](#API_StartSyncExecution_RequestSyntax) **   <a name="StepFunctions-StartSyncExecution-request-name"></a>
The name of the execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: No

 ** [stateMachineArn](#API_StartSyncExecution_RequestSyntax) **   <a name="StepFunctions-StartSyncExecution-request-stateMachineArn"></a>
The Amazon Resource Name (ARN) of the state machine to execute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [traceHeader](#API_StartSyncExecution_RequestSyntax) **   <a name="StepFunctions-StartSyncExecution-request-traceHeader"></a>
Passes the AWS X-Ray trace header. The trace header can also be passed in the request payload.
 For X-Ray traces, all AWS services use the `X-Amzn-Trace-Id` header from the HTTP request. Using the header is the preferred mechanism to identify a trace. `StartExecution` and `StartSyncExecution` API operations can also use `traceHeader` from the body of the request payload. If **both** sources are provided, Step Functions will use the **header value** (preferred) over the value in the request body.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `\p{ASCII}*`
Required: No

## Response Syntax
<a name="API_StartSyncExecution_ResponseSyntax"></a>

```
{
   "billingDetails": {
      "billedDurationInMilliseconds": number,
      "billedMemoryUsedInMB": number
   },
   "cause": "string",
   "error": "string",
   "executionArn": "string",
   "input": "string",
   "inputDetails": {
      "included": boolean
   },
   "name": "string",
   "output": "string",
   "outputDetails": {
      "included": boolean
   },
   "startDate": number,
   "stateMachineArn": "string",
   "status": "string",
   "stopDate": number,
   "traceHeader": "string"
}
```

## Response Elements
<a name="API_StartSyncExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [billingDetails](#API_StartSyncExecution_ResponseSyntax) **   <a name="StepFunctions-StartSyncExecution-response-billingDetails"></a>
An object that describes workflow billing details, including billed duration and memory use.
Type: [BillingDetails](API_BillingDetails.md) object

 ** [cause](#API_StartSyncExecution_ResponseSyntax) **   <a name="StepFunctions-StartSyncExecution-response-cause"></a>
A more detailed explanation of the cause of the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.

 ** [error](#API_StartSyncExecution_ResponseSyntax) **   <a name="StepFunctions-StartSyncExecution-response-error"></a>
The error code of the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [executionArn](#API_StartSyncExecution_ResponseSyntax) **   <a name="StepFunctions-StartSyncExecution-response-executionArn"></a>
The Amazon Resource Name (ARN) that identifies the execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [input](#API_StartSyncExecution_ResponseSyntax) **   <a name="StepFunctions-StartSyncExecution-response-input"></a>
The string that contains the JSON input data of the execution. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
Type: String
Length Constraints: Maximum length of 262144.

 ** [inputDetails](#API_StartSyncExecution_ResponseSyntax) **   <a name="StepFunctions-StartSyncExecution-response-inputDetails"></a>
Provides details about execution input or output.
Type: [CloudWatchEventsExecutionDataDetails](API_CloudWatchEventsExecutionDataDetails.md) object

 ** [name](#API_StartSyncExecution_ResponseSyntax) **   <a name="StepFunctions-StartSyncExecution-response-name"></a>
The name of the execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.

 ** [output](#API_StartSyncExecution_ResponseSyntax) **   <a name="StepFunctions-StartSyncExecution-response-output"></a>
The JSON output data of the execution. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
This field is set only if the execution succeeds. If the execution fails, this field is null.
Type: String
Length Constraints: Maximum length of 262144.

 ** [outputDetails](#API_StartSyncExecution_ResponseSyntax) **   <a name="StepFunctions-StartSyncExecution-response-outputDetails"></a>
Provides details about execution input or output.
Type: [CloudWatchEventsExecutionDataDetails](API_CloudWatchEventsExecutionDataDetails.md) object

 ** [startDate](#API_StartSyncExecution_ResponseSyntax) **   <a name="StepFunctions-StartSyncExecution-response-startDate"></a>
The date the execution is started.
Type: Timestamp

 ** [stateMachineArn](#API_StartSyncExecution_ResponseSyntax) **   <a name="StepFunctions-StartSyncExecution-response-stateMachineArn"></a>
The Amazon Resource Name (ARN) that identifies the state machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [status](#API_StartSyncExecution_ResponseSyntax) **   <a name="StepFunctions-StartSyncExecution-response-status"></a>
The current status of the execution.
Type: String
Valid Values: `SUCCEEDED | FAILED | TIMED_OUT`

 ** [stopDate](#API_StartSyncExecution_ResponseSyntax) **   <a name="StepFunctions-StartSyncExecution-response-stopDate"></a>
If the execution has already ended, the date the execution stopped.
Type: Timestamp

 ** [traceHeader](#API_StartSyncExecution_ResponseSyntax) **   <a name="StepFunctions-StartSyncExecution-response-traceHeader"></a>
The AWS X-Ray trace header that was passed to the execution.
 For X-Ray traces, all AWS services use the `X-Amzn-Trace-Id` header from the HTTP request. Using the header is the preferred mechanism to identify a trace. `StartExecution` and `StartSyncExecution` API operations can also use `traceHeader` from the body of the request payload. If **both** sources are provided, Step Functions will use the **header value** (preferred) over the value in the request body.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `\p{ASCII}*`

## Errors
<a name="API_StartSyncExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** InvalidExecutionInput **
The provided JSON input data is not valid.
HTTP Status Code: 400

 ** InvalidName **
The provided name is not valid.
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

 ** StateMachineDeleting **
The specified state machine is being deleted.
HTTP Status Code: 400

 ** StateMachineDoesNotExist **
The specified state machine does not exist.
HTTP Status Code: 400

 ** StateMachineTypeNotSupported **
State machine type is not supported.
HTTP Status Code: 400

## See Also
<a name="API_StartSyncExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/StartSyncExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/StartSyncExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/StartSyncExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/StartSyncExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/StartSyncExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/StartSyncExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/StartSyncExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/StartSyncExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/StartSyncExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/StartSyncExecution)
