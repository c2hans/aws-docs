---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ExecutionEvent.html
---

# ExecutionEvent
<a name="API_ExecutionEvent"></a>

Represents an event that occurred during a plan execution. These events provide a detailed timeline of the execution process.

## Contents
<a name="API_ExecutionEvent_Contents"></a>

 ** eventId **   <a name="regionswitch-Type-ExecutionEvent-eventId"></a>
The event ID for an execution event.
Type: String
Required: Yes

 ** description **   <a name="regionswitch-Type-ExecutionEvent-description"></a>
The description for an execution event.
Type: String
Required: No

 ** error **   <a name="regionswitch-Type-ExecutionEvent-error"></a>
Errors for an execution event.
Type: String
Required: No

 ** executionBlockType **   <a name="regionswitch-Type-ExecutionEvent-executionBlockType"></a>
The execution block type for an execution event.
Type: String
Valid Values: `CustomActionLambda | ManualApproval | AuroraGlobalDatabase | EC2AutoScaling | ARCRoutingControl | ARCRegionSwitchPlan | Parallel | ECSServiceScaling | EKSResourceScaling | Route53HealthCheck | DocumentDb | RdsPromoteReadReplica | RdsCreateCrossRegionReplica | LambdaEventSourceMapping | AuroraServerlessScaling | AuroraProvisionedScaling | NeptuneGlobalDatabase`
Required: No

 ** previousEventId **   <a name="regionswitch-Type-ExecutionEvent-previousEventId"></a>
The event ID of the previous execution event.
Type: String
Required: No

 ** resources **   <a name="regionswitch-Type-ExecutionEvent-resources"></a>
The resources for an execution event.
Type: Array of strings
Required: No

 ** stepName **   <a name="regionswitch-Type-ExecutionEvent-stepName"></a>
The step name for an execution event.
Type: String
Required: No

 ** timestamp **   <a name="regionswitch-Type-ExecutionEvent-timestamp"></a>
The timestamp for an execution event.
Type: Timestamp
Required: No

 ** type **   <a name="regionswitch-Type-ExecutionEvent-type"></a>
The type of an execution event.
Type: String
Valid Values: `unknown | executionPending | executionStarted | executionSucceeded | executionFailed | executionPausing | executionPaused | executionCanceling | executionCanceled | executionPendingApproval | executionBehaviorChangedToUngraceful | executionBehaviorChangedToGraceful | executionPendingChildPlanManualApproval | executionSuccessMonitoringApplicationHealth | stepStarted | stepUpdate | stepSucceeded | stepFailed | stepSkipped | stepPausedByError | stepPausedByOperator | stepCanceled | stepPendingApproval | stepExecutionBehaviorChangedToUngraceful | stepPendingApplicationHealthMonitor | planEvaluationWarning`
Required: No

## See Also
<a name="API_ExecutionEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/ExecutionEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/ExecutionEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/ExecutionEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
