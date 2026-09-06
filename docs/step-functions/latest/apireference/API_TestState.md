---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_TestState.html
---

# TestState
<a name="API_TestState"></a>

Accepts the definition of a single state and executes it. You can test a state without creating a state machine or updating an existing state machine. Using this API, you can test the following:
+ A state's [input and output processing](https://docs.aws.amazon.com/step-functions/latest/dg/test-state-isolation.html#test-state-input-output-dataflow) data flow
+ An [AWS service integration](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-services.html) request and response
+ An [HTTP Task](https://docs.aws.amazon.com/step-functions/latest/dg/call-https-apis.html) request and response

You can call this API on only one state at a time. The states that you can test include the following:
+  [All Task types](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-task-state.html#task-types) except [Activity](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html)
+  [Pass](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-pass-state.html)
+  [Wait](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-wait-state.html)
+  [Choice](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-choice-state.html)
+  [Succeed](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-succeed-state.html)
+  [Fail](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-fail-state.html)

The `TestState` API assumes an IAM role which must contain the required IAM permissions for the resources your state is accessing. For information about the permissions a state might need, see [IAM permissions to test a state](https://docs.aws.amazon.com/step-functions/latest/dg/test-state-isolation.html#test-state-permissions).

The `TestState` API can run for up to five minutes. If the execution of a state exceeds this duration, it fails with the `States.Timeout` error.

 `TestState` only supports the following when a mock is specified: [Activity tasks](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html), `.sync` or `.waitForTaskToken` [service integration patterns](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html), [Parallel](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-parallel-state.html), or [Map](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-map-state.html) states.

## Request Syntax
<a name="API_TestState_RequestSyntax"></a>

```
{
   "context": "{{string}}",
   "definition": "{{string}}",
   "input": "{{string}}",
   "inspectionLevel": "{{string}}",
   "mock": {
      "errorOutput": {
         "cause": "{{string}}",
         "error": "{{string}}"
      },
      "fieldValidationMode": "{{string}}",
      "result": "{{string}}"
   },
   "revealSecrets": {{boolean}},
   "roleArn": "{{string}}",
   "stateConfiguration": {
      "errorCausedByState": "{{string}}",
      "mapItemReaderData": "{{string}}",
      "mapIterationFailureCount": {{number}},
      "retrierRetryCount": {{number}}
   },
   "stateName": "{{string}}",
   "variables": "{{string}}"
}
```

## Request Parameters
<a name="API_TestState_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [context](#API_TestState_RequestSyntax) **   <a name="StepFunctions-TestState-request-context"></a>
A JSON string representing a valid Context object for the state under test. This field may only be specified if a mock is specified in the same request.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** [definition](#API_TestState_RequestSyntax) **   <a name="StepFunctions-TestState-request-definition"></a>
The [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) (ASL) definition of the state or state machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Required: Yes

 ** [input](#API_TestState_RequestSyntax) **   <a name="StepFunctions-TestState-request-input"></a>
A string that contains the JSON input data for the state.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** [inspectionLevel](#API_TestState_RequestSyntax) **   <a name="StepFunctions-TestState-request-inspectionLevel"></a>
Determines the values to return when a state is tested. You can specify one of the following types:
+  `INFO`: Shows the final state output. By default, Step Functions sets `inspectionLevel` to `INFO` if you don't specify a level.
+  `DEBUG`: Shows the final state output along with the input and output data processing result.
+  `TRACE`: Shows the HTTP request and response for an HTTP Task. This level also shows the final state output along with the input and output data processing result.
Each of these levels also provide information about the status of the state execution and the next state to transition to.
Type: String
Valid Values: `INFO | DEBUG | TRACE`
Required: No

 ** [mock](#API_TestState_RequestSyntax) **   <a name="StepFunctions-TestState-request-mock"></a>
Defines a mocked result or error for the state under test.
A mock can only be specified for Task, Map, or Parallel states. If it is specified for another state type, an exception will be thrown.
Type: [MockInput](API_MockInput.md) object
Required: No

 ** [revealSecrets](#API_TestState_RequestSyntax) **   <a name="StepFunctions-TestState-request-revealSecrets"></a>
Specifies whether or not to include secret information in the test result. For HTTP Tasks, a secret includes the data that an EventBridge connection adds to modify the HTTP request headers, query parameters, and body. Step Functions doesn't omit any information included in the state definition or the HTTP response.
If you set `revealSecrets` to `true`, you must make sure that the IAM user that calls the `TestState` API has permission for the `states:RevealSecrets` action. For an example of IAM policy that sets the `states:RevealSecrets` permission, see [IAM permissions to test a state](https://docs.aws.amazon.com/step-functions/latest/dg/test-state-isolation.html#test-state-permissions). Without this permission, Step Functions throws an access denied error.
By default, `revealSecrets` is set to `false`.
Type: Boolean
Required: No

 ** [roleArn](#API_TestState_RequestSyntax) **   <a name="StepFunctions-TestState-request-roleArn"></a>
The Amazon Resource Name (ARN) of the execution role with the required IAM permissions for the state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [stateConfiguration](#API_TestState_RequestSyntax) **   <a name="StepFunctions-TestState-request-stateConfiguration"></a>
Contains configurations for the state under test.
Type: [TestStateConfiguration](API_TestStateConfiguration.md) object
Required: No

 ** [stateName](#API_TestState_RequestSyntax) **   <a name="StepFunctions-TestState-request-stateName"></a>
Denotes the particular state within a state machine definition to be tested. If this field is specified, the `definition` must contain a fully-formed state machine definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: No

 ** [variables](#API_TestState_RequestSyntax) **   <a name="StepFunctions-TestState-request-variables"></a>
JSON object literal that sets variables used in the state under test. Object keys are the variable names and values are the variable values.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

## Response Syntax
<a name="API_TestState_ResponseSyntax"></a>

```
{
   "cause": "string",
   "error": "string",
   "inspectionData": {
      "afterArguments": "string",
      "afterInputPath": "string",
      "afterItemBatcher": "string",
      "afterItemSelector": "string",
      "afterItemsPath": "string",
      "afterItemsPointer": "string",
      "afterParameters": "string",
      "afterResultPath": "string",
      "afterResultSelector": "string",
      "errorDetails": {
         "catchIndex": number,
         "retryBackoffIntervalSeconds": number,
         "retryIndex": number
      },
      "input": "string",
      "maxConcurrency": number,
      "request": {
         "body": "string",
         "headers": "string",
         "method": "string",
         "protocol": "string",
         "url": "string"
      },
      "response": {
         "body": "string",
         "headers": "string",
         "protocol": "string",
         "statusCode": "string",
         "statusMessage": "string"
      },
      "result": "string",
      "toleratedFailureCount": number,
      "toleratedFailurePercentage": number,
      "variables": "string"
   },
   "nextState": "string",
   "output": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_TestState_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cause](#API_TestState_ResponseSyntax) **   <a name="StepFunctions-TestState-response-cause"></a>
A detailed explanation of the cause for the error when the execution of a state fails.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.

 ** [error](#API_TestState_ResponseSyntax) **   <a name="StepFunctions-TestState-response-error"></a>
The error returned when the execution of a state fails.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [inspectionData](#API_TestState_ResponseSyntax) **   <a name="StepFunctions-TestState-response-inspectionData"></a>
Returns additional details about the state's execution, including its input and output data processing flow, and HTTP request and response information. The `inspectionLevel` request parameter specifies which details are returned.
Type: [InspectionData](API_InspectionData.md) object

 ** [nextState](#API_TestState_ResponseSyntax) **   <a name="StepFunctions-TestState-response-nextState"></a>
The name of the next state to transition to. If you haven't defined a next state in your definition or if the execution of the state fails, this field doesn't contain a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.

 ** [output](#API_TestState_ResponseSyntax) **   <a name="StepFunctions-TestState-response-output"></a>
The JSON output data of the state. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
Type: String
Length Constraints: Maximum length of 262144.

 ** [status](#API_TestState_ResponseSyntax) **   <a name="StepFunctions-TestState-response-status"></a>
The execution status of the state.
Type: String
Valid Values: `SUCCEEDED | FAILED | RETRIABLE | CAUGHT_ERROR`

## Errors
<a name="API_TestState_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** InvalidDefinition **
The provided Amazon States Language definition is not valid.
HTTP Status Code: 400

 ** InvalidExecutionInput **
The provided JSON input data is not valid.
HTTP Status Code: 400

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** reason **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_TestState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/TestState)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/TestState)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/TestState)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/TestState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/TestState)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/TestState)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/TestState)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/TestState)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/TestState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/TestState)
