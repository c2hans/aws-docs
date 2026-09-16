---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_RedriveExecution.html
---

# RedriveExecution
<a name="API_RedriveExecution"></a>

Restarts unsuccessful executions of Standard workflows that didn't complete successfully in the last 14 days. These include failed, aborted, or timed out executions. When you [redrive](https://docs.aws.amazon.com/step-functions/latest/dg/redrive-executions.html) an execution, it continues the failed execution from the unsuccessful step and uses the same input. Step Functions preserves the results and execution history of the successful steps, and doesn't rerun these steps when you redrive an execution. Redriven executions use the same state machine definition and execution ARN as the original execution attempt.

For workflows that include an [Inline Map](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-map-state.html) or [Parallel](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-parallel-state.html) state, `RedriveExecution` API action reschedules and redrives only the iterations and branches that failed or aborted.

To redrive a workflow that includes a Distributed Map state whose Map Run failed, you must redrive the [parent workflow](https://docs.aws.amazon.com/step-functions/latest/dg/use-dist-map-orchestrate-large-scale-parallel-workloads.html#dist-map-orchestrate-parallel-workloads-key-terms). The parent workflow redrives all the unsuccessful states, including a failed Map Run. If a Map Run was not started in the original execution attempt, the redriven parent workflow starts the Map Run.

**Note**
This API action is not supported by `EXPRESS` state machines.
However, you can restart the unsuccessful executions of Express child workflows in a Distributed Map by redriving its Map Run. When you redrive a Map Run, the Express child workflows are rerun using the [StartExecution](API_StartExecution.md) API action. For more information, see [Redriving Map Runs](https://docs.aws.amazon.com/step-functions/latest/dg/redrive-map-run.html).

You can redrive executions if your original execution meets the following conditions:
+ The execution status isn't `SUCCEEDED`.
+ Your workflow execution has not exceeded the redrivable period of 14 days. Redrivable period refers to the time during which you can redrive a given execution. This period starts from the day a state machine completes its execution.
+ The workflow execution has not exceeded the maximum open time of one year. For more information about state machine quotas, see [Quotas related to state machine executions](https://docs.aws.amazon.com/step-functions/latest/dg/limits-overview.html#service-limits-state-machine-executions).
+ The execution event history count is less than 24,999. Redriven executions append their event history to the existing event history. Make sure your workflow execution contains less than 24,999 events to accommodate the `ExecutionRedriven` history event and at least one other history event.

## Request Syntax
<a name="API_RedriveExecution_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "executionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_RedriveExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_RedriveExecution_RequestSyntax) **   <a name="StepFunctions-RedriveExecution-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the AWS SDK automatically generates a client token and uses it for the request to ensure idempotency. The API will return idempotent responses for the last 10 client tokens used to successfully redrive the execution. These client tokens are valid for up to 15 minutes after they are first used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [executionArn](#API_RedriveExecution_RequestSyntax) **   <a name="StepFunctions-RedriveExecution-request-executionArn"></a>
The Amazon Resource Name (ARN) of the execution to be redriven.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_RedriveExecution_ResponseSyntax"></a>

```
{
   "redriveDate": number
}
```

## Response Elements
<a name="API_RedriveExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [redriveDate](#API_RedriveExecution_ResponseSyntax) **   <a name="StepFunctions-RedriveExecution-response-redriveDate"></a>
The date the execution was last redriven.
Type: Timestamp

## Errors
<a name="API_RedriveExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ExecutionDoesNotExist **
The specified execution does not exist.
HTTP Status Code: 400

 ** ExecutionLimitExceeded **
The maximum number of running executions has been reached. Running executions must end or be stopped before a new execution can be started.
HTTP Status Code: 400

 ** ExecutionNotRedrivable **
The execution Amazon Resource Name (ARN) that you specified for `executionArn` cannot be redriven.
HTTP Status Code: 400

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** reason **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_RedriveExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/RedriveExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/RedriveExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/RedriveExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/RedriveExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/RedriveExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/RedriveExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/RedriveExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/RedriveExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/RedriveExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/RedriveExecution)
