---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AutomationExecution.html
---

# AutomationExecution
<a name="API_AutomationExecution"></a>

Detailed information about the current state of an individual Automation execution.

## Contents
<a name="API_AutomationExecution_Contents"></a>

 ** AlarmConfiguration **   <a name="systemsmanager-Type-AutomationExecution-AlarmConfiguration"></a>
The details for the CloudWatch alarm applied to your automation.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** AssociationId **   <a name="systemsmanager-Type-AutomationExecution-AssociationId"></a>
The ID of a State Manager association used in the Automation operation.
Type: String
Required: No

 ** AutomationExecutionId **   <a name="systemsmanager-Type-AutomationExecution-AutomationExecutionId"></a>
The execution ID.
Type: String
Length Constraints: Fixed length of 36.
Required: No

 ** AutomationExecutionStatus **   <a name="systemsmanager-Type-AutomationExecution-AutomationExecutionStatus"></a>
The execution status of the Automation.
Type: String
Valid Values: `Pending | InProgress | Waiting | Success | TimedOut | Cancelling | Cancelled | Failed | PendingApproval | Approved | Rejected | Scheduled | RunbookInProgress | PendingChangeCalendarOverride | ChangeCalendarOverrideApproved | ChangeCalendarOverrideRejected | CompletedWithSuccess | CompletedWithFailure | Exited`
Required: No

 ** AutomationSubtype **   <a name="systemsmanager-Type-AutomationExecution-AutomationSubtype"></a>
The subtype of the Automation operation. Currently, the only supported value is `ChangeRequest`.
Type: String
Valid Values: `ChangeRequest | AccessRequest`
Required: No

 ** ChangeRequestName **   <a name="systemsmanager-Type-AutomationExecution-ChangeRequestName"></a>
The name of the Change Manager change request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** CurrentAction **   <a name="systemsmanager-Type-AutomationExecution-CurrentAction"></a>
The action of the step that is currently running.
Type: String
Required: No

 ** CurrentStepName **   <a name="systemsmanager-Type-AutomationExecution-CurrentStepName"></a>
The name of the step that is currently running.
Type: String
Required: No

 ** DocumentName **   <a name="systemsmanager-Type-AutomationExecution-DocumentName"></a>
The name of the Automation runbook used during the execution.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** DocumentVersion **   <a name="systemsmanager-Type-AutomationExecution-DocumentVersion"></a>
The version of the document to use during execution.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** ExecutedBy **   <a name="systemsmanager-Type-AutomationExecution-ExecutedBy"></a>
The Amazon Resource Name (ARN) of the user who ran the automation.
Type: String
Required: No

 ** ExecutionEndTime **   <a name="systemsmanager-Type-AutomationExecution-ExecutionEndTime"></a>
The time the execution finished.
Type: Timestamp
Required: No

 ** ExecutionStartTime **   <a name="systemsmanager-Type-AutomationExecution-ExecutionStartTime"></a>
The time the execution started.
Type: Timestamp
Required: No

 ** FailureMessage **   <a name="systemsmanager-Type-AutomationExecution-FailureMessage"></a>
A message describing why an execution has failed, if the status is set to Failed.
Type: String
Required: No

 ** MaxConcurrency **   <a name="systemsmanager-Type-AutomationExecution-MaxConcurrency"></a>
The `MaxConcurrency` value specified by the user when the execution started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`
Required: No

 ** MaxErrors **   <a name="systemsmanager-Type-AutomationExecution-MaxErrors"></a>
The MaxErrors value specified by the user when the execution started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`
Required: No

 ** Mode **   <a name="systemsmanager-Type-AutomationExecution-Mode"></a>
The automation execution mode.
Type: String
Valid Values: `Auto | Interactive`
Required: No

 ** OpsItemId **   <a name="systemsmanager-Type-AutomationExecution-OpsItemId"></a>
The ID of an OpsItem that is created to represent a Change Manager change request.
Type: String
Required: No

 ** Outputs **   <a name="systemsmanager-Type-AutomationExecution-Outputs"></a>
The list of execution outputs as defined in the Automation runbook.
Type: String to array of strings map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Parameters **   <a name="systemsmanager-Type-AutomationExecution-Parameters"></a>
The key-value map of execution parameters, which were supplied when calling [StartAutomationExecution](API_StartAutomationExecution.md).
Type: String to array of strings map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** ParentAutomationExecutionId **   <a name="systemsmanager-Type-AutomationExecution-ParentAutomationExecutionId"></a>
The AutomationExecutionId of the parent automation.
Type: String
Length Constraints: Fixed length of 36.
Required: No

 ** ProgressCounters **   <a name="systemsmanager-Type-AutomationExecution-ProgressCounters"></a>
An aggregate of step execution statuses displayed in the AWS Systems Manager console for a multi-Region and multi-account Automation execution.
Type: [ProgressCounters](API_ProgressCounters.md) object
Required: No

 ** ResolvedTargets **   <a name="systemsmanager-Type-AutomationExecution-ResolvedTargets"></a>
A list of resolved targets in the rate control execution.
Type: [ResolvedTargets](API_ResolvedTargets.md) object
Required: No

 ** Runbooks **   <a name="systemsmanager-Type-AutomationExecution-Runbooks"></a>
Information about the Automation runbooks that are run as part of a runbook workflow.
The Automation runbooks specified for the runbook workflow can't run until all required approvals for the change request have been received.
Type: Array of [Runbook](API_Runbook.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** ScheduledTime **   <a name="systemsmanager-Type-AutomationExecution-ScheduledTime"></a>
The date and time the Automation operation is scheduled to start.
Type: Timestamp
Required: No

 ** StepExecutions **   <a name="systemsmanager-Type-AutomationExecution-StepExecutions"></a>
A list of details about the current state of all steps that comprise an execution. An Automation runbook contains a list of steps that are run in order.
Type: Array of [StepExecution](API_StepExecution.md) objects
Required: No

 ** StepExecutionsTruncated **   <a name="systemsmanager-Type-AutomationExecution-StepExecutionsTruncated"></a>
A boolean value that indicates if the response contains the full list of the Automation step executions. If true, use the DescribeAutomationStepExecutions API operation to get the full list of step executions.
Type: Boolean
Required: No

 ** Target **   <a name="systemsmanager-Type-AutomationExecution-Target"></a>
The target of the execution.
Type: String
Required: No

 ** TargetLocations **   <a name="systemsmanager-Type-AutomationExecution-TargetLocations"></a>
The combination of AWS Regions and/or AWS accounts where you want to run the Automation.
Type: Array of [TargetLocation](API_TargetLocation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** TargetLocationsURL **   <a name="systemsmanager-Type-AutomationExecution-TargetLocationsURL"></a>
A publicly accessible URL for a file that contains the `TargetLocations` body. Currently, only files in presigned Amazon S3 buckets are supported
Type: String
Pattern: `^https:\/\/[-a-zA-Z0-9@:%._\+~#=]{1,253}\.s3(\.[a-z\d-]{9,16})?\.amazonaws\.com\/.{1,2000}`
Required: No

 ** TargetMaps **   <a name="systemsmanager-Type-AutomationExecution-TargetMaps"></a>
The specified key-value mapping of document parameters to target resources.
Type: Array of string to array of strings maps
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Map Entries: Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** TargetParameterName **   <a name="systemsmanager-Type-AutomationExecution-TargetParameterName"></a>
The parameter name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** Targets **   <a name="systemsmanager-Type-AutomationExecution-Targets"></a>
The specified targets.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** TriggeredAlarms **   <a name="systemsmanager-Type-AutomationExecution-TriggeredAlarms"></a>
The CloudWatch alarm that was invoked by the automation.
Type: Array of [AlarmStateInformation](API_AlarmStateInformation.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** Variables **   <a name="systemsmanager-Type-AutomationExecution-Variables"></a>
Variables defined for the automation.
Type: String to array of strings map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** WarningMessage **   <a name="systemsmanager-Type-AutomationExecution-WarningMessage"></a>
A message that describes a non-critical issue that occurred during the automation execution.
Type: String
Required: No

## See Also
<a name="API_AutomationExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AutomationExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AutomationExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AutomationExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
