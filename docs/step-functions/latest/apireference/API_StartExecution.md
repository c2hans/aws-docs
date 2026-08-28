---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
---

# StartExecution
<a name="API_StartExecution"></a>

Starts a state machine execution.

A qualified state machine ARN can either refer to a *Distributed Map state* defined within a state machine, a version ARN, or an alias ARN.

The following are some examples of qualified and unqualified state machine ARNs:
+ The following qualified state machine ARN refers to a *Distributed Map state* with a label `mapStateLabel` in a state machine named `myStateMachine`.

   `arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel`
**Note**
If you provide a qualified state machine ARN that refers to a *Distributed Map state*, the request fails with `ValidationException`.
+ The following qualified state machine ARN refers to an alias named `PROD`.

   `arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine:PROD>`
**Note**
If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.
+ The following unqualified state machine ARN refers to a state machine named `myStateMachine`.

   `arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine>`

If you start an execution with an unqualified state machine ARN, Step Functions uses the latest revision of the state machine for the execution.

To start executions of a state machine [version](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html), call `StartExecution` and provide the version ARN or the ARN of an [alias](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html) that points to the version.

**Note**
 `StartExecution` is idempotent for `STANDARD` workflows. For a `STANDARD` workflow, if you call `StartExecution` with the same name and input as a running execution, the call succeeds and return the same response as the original request. If the execution is closed or if the input is different, it returns a `400 ExecutionAlreadyExists` error. You can reuse the name 90 days after it closes.
 `StartExecution` isn't idempotent for `EXPRESS` workflows.

## Request Syntax
<a name="API_StartExecution_RequestSyntax"></a>

```
{
   "input": "{{string}}",
   "name": "{{string}}",
   "stateMachineArn": "{{string}}",
   "traceHeader": "{{string}}"
}
```

## Request Parameters
<a name="API_StartExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [input](#API_StartExecution_RequestSyntax) **   <a name="StepFunctions-StartExecution-request-input"></a>
The string that contains the JSON input data for the execution, for example:
 `"{\"first_name\" : \"Alejandro\"}"`
If you don't include any JSON input data, you still must include the two braces, for example: `"{}"`
Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** [name](#API_StartExecution_RequestSyntax) **   <a name="StepFunctions-StartExecution-request-name"></a>
Optional name of the execution. For STANDARD workflows, this name must be unique for your AWS account, region, and state machine. If a previous execution with the same name exists, you can reuse the name 90 days after it closes. For EXPRESS workflows, execution names can be reused immediately. For more information, see [ Limits Related to State Machine Executions](https://docs.aws.amazon.com/step-functions/latest/dg/limits.html#service-limits-state-machine-executions) in the * AWS Step Functions Developer Guide*.
If you don't provide a name for the execution, Step Functions automatically generates a universally unique identifier (UUID) as the execution name.
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
Required: No

 ** [stateMachineArn](#API_StartExecution_RequestSyntax) **   <a name="StepFunctions-StartExecution-request-stateMachineArn"></a>
The Amazon Resource Name (ARN) of the state machine to execute.
The `stateMachineArn` parameter accepts one of the following inputs:
+  **An unqualified state machine ARN** – Refers to a state machine ARN that isn't qualified with a version or alias ARN. The following is an example of an unqualified state machine ARN.

   `arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine>`

  Step Functions doesn't associate state machine executions that you start with an unqualified ARN with a version. This is true even if that version uses the same revision that the execution used.
+  **A state machine version ARN** – Refers to a version ARN, which is a combination of state machine ARN and the version number separated by a colon (:). The following is an example of the ARN for version 10.

   `arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine>:10`

  Step Functions doesn't associate executions that you start with a version ARN with any aliases that point to that version.
+  **A state machine alias ARN** – Refers to an alias ARN, which is a combination of state machine ARN and the alias name separated by a colon (:). The following is an example of the ARN for an alias named `PROD`.

   `arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine:PROD>`

  Step Functions associates executions that you start with an alias ARN with that alias and the state machine version used for that execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [traceHeader](#API_StartExecution_RequestSyntax) **   <a name="StepFunctions-StartExecution-request-traceHeader"></a>
Passes the AWS X-Ray trace header. The trace header can also be passed in the request payload.
 For X-Ray traces, all AWS services use the `X-Amzn-Trace-Id` header from the HTTP request. Using the header is the preferred mechanism to identify a trace. `StartExecution` and `StartSyncExecution` API operations can also use `traceHeader` from the body of the request payload. If **both** sources are provided, Step Functions will use the **header value** (preferred) over the value in the request body.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `\p{ASCII}*`
Required: No

## Response Syntax
<a name="API_StartExecution_ResponseSyntax"></a>

```
{
   "executionArn": "string",
   "startDate": number
}
```

## Response Elements
<a name="API_StartExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executionArn](#API_StartExecution_ResponseSyntax) **   <a name="StepFunctions-StartExecution-response-executionArn"></a>
The Amazon Resource Name (ARN) that identifies the execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [startDate](#API_StartExecution_ResponseSyntax) **   <a name="StepFunctions-StartExecution-response-startDate"></a>
The date the execution is started.
Type: Timestamp

## Errors
<a name="API_StartExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ExecutionAlreadyExists **
The execution has the same `name` as another execution (but a different `input`).
Executions with the same `name` and `input` are considered idempotent.
HTTP Status Code: 400

 ** ExecutionLimitExceeded **
The maximum number of running executions has been reached. Running executions must end or be stopped before a new execution can be started.
HTTP Status Code: 400

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

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** reason **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StartExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/StartExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/StartExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/StartExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/StartExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/StartExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/StartExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/StartExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/StartExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/StartExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/StartExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
