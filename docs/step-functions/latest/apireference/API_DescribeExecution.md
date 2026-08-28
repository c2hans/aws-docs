---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeExecution.html
---

# DescribeExecution
<a name="API_DescribeExecution"></a>

Provides information about a state machine execution, such as the state machine associated with the execution, the execution input and output, and relevant execution metadata. If you've [redriven](https://docs.aws.amazon.com/step-functions/latest/dg/redrive-executions.html) an execution, you can use this API action to return information about the redrives of that execution. In addition, you can use this API action to return the Map Run Amazon Resource Name (ARN) if the execution was dispatched by a Map Run.

If you specify a version or alias ARN when you call the [StartExecution](API_StartExecution.md) API action, `DescribeExecution` returns that ARN.

**Note**
This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.

Executions of an `EXPRESS` state machine aren't supported by `DescribeExecution` unless a Map Run dispatched them.

## Request Syntax
<a name="API_DescribeExecution_RequestSyntax"></a>

```
{
   "executionArn": "{{string}}",
   "includedData": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [executionArn](#API_DescribeExecution_RequestSyntax) **   <a name="StepFunctions-DescribeExecution-request-executionArn"></a>
The Amazon Resource Name (ARN) of the execution to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [includedData](#API_DescribeExecution_RequestSyntax) **   <a name="StepFunctions-DescribeExecution-request-includedData"></a>
If your state machine definition is encrypted with a AWS KMS key, callers must have `kms:Decrypt` permission to decrypt the definition. Alternatively, you can call DescribeStateMachine API with `includedData = METADATA_ONLY` to get a successful response without the encrypted definition.
Type: String
Valid Values: `ALL_DATA | METADATA_ONLY`
Required: No

## Response Syntax
<a name="API_DescribeExecution_ResponseSyntax"></a>

```
{
   "cause": "string",
   "error": "string",
   "executionArn": "string",
   "input": "string",
   "inputDetails": {
      "included": boolean
   },
   "mapRunArn": "string",
   "name": "string",
   "output": "string",
   "outputDetails": {
      "included": boolean
   },
   "redriveCount": number,
   "redriveDate": number,
   "redriveStatus": "string",
   "redriveStatusReason": "string",
   "startDate": number,
   "stateMachineAliasArn": "string",
   "stateMachineArn": "string",
   "stateMachineVersionArn": "string",
   "status": "string",
   "stopDate": number,
   "traceHeader": "string"
}
```

## Response Elements
<a name="API_DescribeExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cause](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-cause"></a>
The cause string if the state machine execution failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.

 ** [error](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-error"></a>
The error string if the state machine execution failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [executionArn](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-executionArn"></a>
The Amazon Resource Name (ARN) that identifies the execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [input](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-input"></a>
The string that contains the JSON input data of the execution. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
Type: String
Length Constraints: Maximum length of 262144.

 ** [inputDetails](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-inputDetails"></a>
Provides details about execution input or output.
Type: [CloudWatchEventsExecutionDataDetails](API_CloudWatchEventsExecutionDataDetails.md) object

 ** [mapRunArn](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-mapRunArn"></a>
The Amazon Resource Name (ARN) that identifies a Map Run, which dispatched this execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [name](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-name"></a>
The name of the execution.
A name must *not* contain:
+ white space
+ brackets `< > { } [ ]`
+ wildcard characters `? *`
+ special characters `" # % \ ^ | ~ ` $ & , ; : /`
+ control characters (`U+0000-001F`, `U+007F-009F`, `U+FFFE-FFFF`)
+ surrogates (`U+D800-DFFF`)
+ invalid characters (` U+10FFFF`)
To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and \_.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.

 ** [output](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-output"></a>
The JSON output data of the execution. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
This field is set only if the execution succeeds. If the execution fails, this field is null.
Type: String
Length Constraints: Maximum length of 262144.

 ** [outputDetails](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-outputDetails"></a>
Provides details about execution input or output.
Type: [CloudWatchEventsExecutionDataDetails](API_CloudWatchEventsExecutionDataDetails.md) object

 ** [redriveCount](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-redriveCount"></a>
The number of times you've redriven an execution. If you have not yet redriven an execution, the `redriveCount` is 0. This count is only updated if you successfully redrive an execution.
Type: Integer

 ** [redriveDate](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-redriveDate"></a>
The date the execution was last redriven. If you have not yet redriven an execution, the `redriveDate` is null.
The `redriveDate` is unavailable if you redrive a Map Run that starts child workflow executions of type `EXPRESS`.
Type: Timestamp

 ** [redriveStatus](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-redriveStatus"></a>
Indicates whether or not an execution can be redriven at a given point in time.
+ For executions of type `STANDARD`, `redriveStatus` is `NOT_REDRIVABLE` if calling the [RedriveExecution](API_RedriveExecution.md) API action would return the `ExecutionNotRedrivable` error.
+ For a Distributed Map that includes child workflows of type `STANDARD`, `redriveStatus` indicates whether or not the Map Run can redrive child workflow executions.
+ For a Distributed Map that includes child workflows of type `EXPRESS`, `redriveStatus` indicates whether or not the Map Run can redrive child workflow executions.

  You can redrive failed or timed out `EXPRESS` workflows *only if* they're a part of a Map Run. When you [redrive](https://docs.aws.amazon.com/step-functions/latest/dg/redrive-map-run.html) the Map Run, these workflows are restarted using the [StartExecution](API_StartExecution.md) API action.
Type: String
Valid Values: `REDRIVABLE | NOT_REDRIVABLE | REDRIVABLE_BY_MAP_RUN`

 ** [redriveStatusReason](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-redriveStatusReason"></a>
When `redriveStatus` is `NOT_REDRIVABLE`, `redriveStatusReason` specifies the reason why an execution cannot be redriven.
+ For executions of type `STANDARD`, or for a Distributed Map that includes child workflows of type `STANDARD`, `redriveStatusReason` can include one of the following reasons:
  +  `State machine is in DELETING status`.
  +  `Execution is RUNNING and cannot be redriven`.
  +  `Execution is SUCCEEDED and cannot be redriven`.
  +  `Execution was started before the launch of RedriveExecution`.
  +  `Execution history event limit exceeded`.
  +  `Execution has exceeded the max execution time`.
  +  `Execution redrivable period exceeded`.
+ For a Distributed Map that includes child workflows of type `EXPRESS`, `redriveStatusReason` is only returned if the child workflows are not redrivable. This happens when the child workflow executions have completed successfully.
Type: String
Length Constraints: Maximum length of 262144.

 ** [startDate](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-startDate"></a>
The date the execution is started.
Type: Timestamp

 ** [stateMachineAliasArn](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-stateMachineAliasArn"></a>
The Amazon Resource Name (ARN) of the state machine alias associated with the execution. The alias ARN is a combination of state machine ARN and the alias name separated by a colon (:). For example, `stateMachineARN:PROD`.
If you start an execution from a `StartExecution` request with a state machine version ARN, this field will be null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [stateMachineArn](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-stateMachineArn"></a>
The Amazon Resource Name (ARN) of the executed stated machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [stateMachineVersionArn](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-stateMachineVersionArn"></a>
The Amazon Resource Name (ARN) of the state machine version associated with the execution. The version ARN is a combination of state machine ARN and the version number separated by a colon (:). For example, `stateMachineARN:1`.
If you start an execution from a `StartExecution` request without specifying a state machine version or alias ARN, Step Functions returns a null value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [status](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-status"></a>
The current status of the execution.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | TIMED_OUT | ABORTED | PENDING_REDRIVE`

 ** [stopDate](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-stopDate"></a>
If the execution ended, the date the execution stopped.
Type: Timestamp

 ** [traceHeader](#API_DescribeExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeExecution-response-traceHeader"></a>
The AWS X-Ray trace header that was passed to the execution.
 For X-Ray traces, all AWS services use the `X-Amzn-Trace-Id` header from the HTTP request. Using the header is the preferred mechanism to identify a trace. `StartExecution` and `StartSyncExecution` API operations can also use `traceHeader` from the body of the request payload. If **both** sources are provided, Step Functions will use the **header value** (preferred) over the value in the request body.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `\p{ASCII}*`

## Errors
<a name="API_DescribeExecution_Errors"></a>

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

## See Also
<a name="API_DescribeExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/DescribeExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/DescribeExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/DescribeExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/DescribeExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/DescribeExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/DescribeExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/DescribeExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/DescribeExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/DescribeExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/DescribeExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
