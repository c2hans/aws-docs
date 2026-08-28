---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StepExecution.html
---

# StepExecution
<a name="API_StepExecution"></a>

Detailed information about an the execution state of an Automation step.

## Contents
<a name="API_StepExecution_Contents"></a>

 ** Action **   <a name="systemsmanager-Type-StepExecution-Action"></a>
The action this step performs. The action determines the behavior of the step.
Type: String
Pattern: `^aws:[a-zA-Z]{3,25}$`
Required: No

 ** ExecutionEndTime **   <a name="systemsmanager-Type-StepExecution-ExecutionEndTime"></a>
If a step has finished execution, this contains the time the execution ended. If the step hasn't yet concluded, this field isn't populated.
Type: Timestamp
Required: No

 ** ExecutionStartTime **   <a name="systemsmanager-Type-StepExecution-ExecutionStartTime"></a>
If a step has begun execution, this contains the time the step started. If the step is in Pending status, this field isn't populated.
Type: Timestamp
Required: No

 ** FailureDetails **   <a name="systemsmanager-Type-StepExecution-FailureDetails"></a>
Information about the Automation failure.
Type: [FailureDetails](API_FailureDetails.md) object
Required: No

 ** FailureMessage **   <a name="systemsmanager-Type-StepExecution-FailureMessage"></a>
If a step failed, this message explains why the execution failed.
Type: String
Required: No

 ** Inputs **   <a name="systemsmanager-Type-StepExecution-Inputs"></a>
Fully-resolved values passed into the step before execution.
Type: String to string map
Required: No

 ** IsCritical **   <a name="systemsmanager-Type-StepExecution-IsCritical"></a>
The flag which can be used to help decide whether the failure of current step leads to the Automation failure.
Type: Boolean
Required: No

 ** IsEnd **   <a name="systemsmanager-Type-StepExecution-IsEnd"></a>
The flag which can be used to end automation no matter whether the step succeeds or fails.
Type: Boolean
Required: No

 ** MaxAttempts **   <a name="systemsmanager-Type-StepExecution-MaxAttempts"></a>
The maximum number of tries to run the action of the step. The default value is `1`.
Type: Integer
Required: No

 ** NextStep **   <a name="systemsmanager-Type-StepExecution-NextStep"></a>
The next step after the step succeeds.
Type: String
Required: No

 ** OnFailure **   <a name="systemsmanager-Type-StepExecution-OnFailure"></a>
The action to take if the step fails. The default value is `Abort`.
Type: String
Required: No

 ** Outputs **   <a name="systemsmanager-Type-StepExecution-Outputs"></a>
Returned values from the execution of the step.
Type: String to array of strings map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** OverriddenParameters **   <a name="systemsmanager-Type-StepExecution-OverriddenParameters"></a>
A user-specified list of parameters to override when running a step.
Type: String to array of strings map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** ParentStepDetails **   <a name="systemsmanager-Type-StepExecution-ParentStepDetails"></a>
Information about the parent step.
Type: [ParentStepDetails](API_ParentStepDetails.md) object
Required: No

 ** Response **   <a name="systemsmanager-Type-StepExecution-Response"></a>
A message associated with the response code for an execution.
Type: String
Required: No

 ** ResponseCode **   <a name="systemsmanager-Type-StepExecution-ResponseCode"></a>
The response code returned by the execution of the step.
Type: String
Required: No

 ** StepExecutionId **   <a name="systemsmanager-Type-StepExecution-StepExecutionId"></a>
The unique ID of a step execution.
Type: String
Required: No

 ** StepName **   <a name="systemsmanager-Type-StepExecution-StepName"></a>
The name of this execution step.
Type: String
Required: No

 ** StepStatus **   <a name="systemsmanager-Type-StepExecution-StepStatus"></a>
The execution status for this step.
Type: String
Valid Values: `Pending | InProgress | Waiting | Success | TimedOut | Cancelling | Cancelled | Failed | PendingApproval | Approved | Rejected | Scheduled | RunbookInProgress | PendingChangeCalendarOverride | ChangeCalendarOverrideApproved | ChangeCalendarOverrideRejected | CompletedWithSuccess | CompletedWithFailure | Exited`
Required: No

 ** TargetLocation **   <a name="systemsmanager-Type-StepExecution-TargetLocation"></a>
The combination of AWS Regions and AWS accounts targeted by the current Automation execution.
Type: [TargetLocation](API_TargetLocation.md) object
Required: No

 ** Targets **   <a name="systemsmanager-Type-StepExecution-Targets"></a>
The targets for the step execution.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** TimeoutSeconds **   <a name="systemsmanager-Type-StepExecution-TimeoutSeconds"></a>
The timeout seconds of the step.
Type: Long
Required: No

 ** TriggeredAlarms **   <a name="systemsmanager-Type-StepExecution-TriggeredAlarms"></a>
The CloudWatch alarms that were invoked by the automation.
Type: Array of [AlarmStateInformation](API_AlarmStateInformation.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** ValidNextSteps **   <a name="systemsmanager-Type-StepExecution-ValidNextSteps"></a>
Strategies used when step fails, we support Continue and Abort. Abort will fail the automation when the step fails. Continue will ignore the failure of current step and allow automation to run the next step. With conditional branching, we add step:stepName to support the automation to go to another specific step.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

 ** WarningMessage **   <a name="systemsmanager-Type-StepExecution-WarningMessage"></a>
A message that describes a non-critical issue that occurred during the step execution. Present only if the step status includes a warning.
Type: String
Required: No

## See Also
<a name="API_StepExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/StepExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/StepExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/StepExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
