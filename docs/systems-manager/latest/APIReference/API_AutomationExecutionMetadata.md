---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AutomationExecutionMetadata.html
---

# AutomationExecutionMetadata
<a name="API_AutomationExecutionMetadata"></a>

Details about a specific Automation execution.

## Contents
<a name="API_AutomationExecutionMetadata_Contents"></a>

 ** AlarmConfiguration **   <a name="systemsmanager-Type-AutomationExecutionMetadata-AlarmConfiguration"></a>
The details for the CloudWatch alarm applied to your automation.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** AssociationId **   <a name="systemsmanager-Type-AutomationExecutionMetadata-AssociationId"></a>
The ID of a State Manager association used in the Automation operation.
Type: String
Required: No

 ** AutomationExecutionId **   <a name="systemsmanager-Type-AutomationExecutionMetadata-AutomationExecutionId"></a>
The execution ID.
Type: String
Length Constraints: Fixed length of 36.
Required: No

 ** AutomationExecutionStatus **   <a name="systemsmanager-Type-AutomationExecutionMetadata-AutomationExecutionStatus"></a>
The status of the execution.
Type: String
Valid Values: `Pending | InProgress | Waiting | Success | TimedOut | Cancelling | Cancelled | Failed | PendingApproval | Approved | Rejected | Scheduled | RunbookInProgress | PendingChangeCalendarOverride | ChangeCalendarOverrideApproved | ChangeCalendarOverrideRejected | CompletedWithSuccess | CompletedWithFailure | Exited`
Required: No

 ** AutomationSubtype **   <a name="systemsmanager-Type-AutomationExecutionMetadata-AutomationSubtype"></a>
The subtype of the Automation operation. Currently, the only supported value is `ChangeRequest`.
Type: String
Valid Values: `ChangeRequest | AccessRequest`
Required: No

 ** AutomationType **   <a name="systemsmanager-Type-AutomationExecutionMetadata-AutomationType"></a>
Use this filter with [DescribeAutomationExecutions](API_DescribeAutomationExecutions.md). Specify either Local or CrossAccount. CrossAccount is an Automation that runs in multiple AWS Regions and AWS accounts. For more information, see [Running automations in multiple AWS Regions and accounts](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation-multiple-accounts-and-regions.html) in the * AWS Systems Manager User Guide*.
Type: String
Valid Values: `CrossAccount | Local`
Required: No

 ** ChangeRequestName **   <a name="systemsmanager-Type-AutomationExecutionMetadata-ChangeRequestName"></a>
The name of the Change Manager change request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** CurrentAction **   <a name="systemsmanager-Type-AutomationExecutionMetadata-CurrentAction"></a>
The action of the step that is currently running.
Type: String
Required: No

 ** CurrentStepName **   <a name="systemsmanager-Type-AutomationExecutionMetadata-CurrentStepName"></a>
The name of the step that is currently running.
Type: String
Required: No

 ** DocumentName **   <a name="systemsmanager-Type-AutomationExecutionMetadata-DocumentName"></a>
The name of the Automation runbook used during execution.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** DocumentVersion **   <a name="systemsmanager-Type-AutomationExecutionMetadata-DocumentVersion"></a>
The document version used during the execution.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** ExecutedBy **   <a name="systemsmanager-Type-AutomationExecutionMetadata-ExecutedBy"></a>
The IAM role ARN of the user who ran the automation.
Type: String
Required: No

 ** ExecutionEndTime **   <a name="systemsmanager-Type-AutomationExecutionMetadata-ExecutionEndTime"></a>
The time the execution finished. This isn't populated if the execution is still in progress.
Type: Timestamp
Required: No

 ** ExecutionStartTime **   <a name="systemsmanager-Type-AutomationExecutionMetadata-ExecutionStartTime"></a>
The time the execution started.
Type: Timestamp
Required: No

 ** FailureMessage **   <a name="systemsmanager-Type-AutomationExecutionMetadata-FailureMessage"></a>
A message that describes a failure that occurred during the automation execution.
Type: String
Required: No

 ** LogFile **   <a name="systemsmanager-Type-AutomationExecutionMetadata-LogFile"></a>
An S3 bucket where execution information is stored.
Type: String
Required: No

 ** MaxConcurrency **   <a name="systemsmanager-Type-AutomationExecutionMetadata-MaxConcurrency"></a>
The `MaxConcurrency` value specified by the user when starting the automation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`
Required: No

 ** MaxErrors **   <a name="systemsmanager-Type-AutomationExecutionMetadata-MaxErrors"></a>
The `MaxErrors` value specified by the user when starting the automation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`
Required: No

 ** Mode **   <a name="systemsmanager-Type-AutomationExecutionMetadata-Mode"></a>
The Automation execution mode.
Type: String
Valid Values: `Auto | Interactive`
Required: No

 ** OpsItemId **   <a name="systemsmanager-Type-AutomationExecutionMetadata-OpsItemId"></a>
The ID of an OpsItem that is created to represent a Change Manager change request.
Type: String
Required: No

 ** Outputs **   <a name="systemsmanager-Type-AutomationExecutionMetadata-Outputs"></a>
The list of execution outputs as defined in the Automation runbook.
Type: String to array of strings map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** ParentAutomationExecutionId **   <a name="systemsmanager-Type-AutomationExecutionMetadata-ParentAutomationExecutionId"></a>
The execution ID of the parent automation.
Type: String
Length Constraints: Fixed length of 36.
Required: No

 ** ResolvedTargets **   <a name="systemsmanager-Type-AutomationExecutionMetadata-ResolvedTargets"></a>
A list of targets that resolved during the execution.
Type: [ResolvedTargets](API_ResolvedTargets.md) object
Required: No

 ** Runbooks **   <a name="systemsmanager-Type-AutomationExecutionMetadata-Runbooks"></a>
Information about the Automation runbooks that are run during a runbook workflow in Change Manager.
The Automation runbooks specified for the runbook workflow can't run until all required approvals for the change request have been received.
Type: Array of [Runbook](API_Runbook.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** ScheduledTime **   <a name="systemsmanager-Type-AutomationExecutionMetadata-ScheduledTime"></a>
The date and time the Automation operation is scheduled to start.
Type: Timestamp
Required: No

 ** Target **   <a name="systemsmanager-Type-AutomationExecutionMetadata-Target"></a>
The list of execution outputs as defined in the Automation runbook.
Type: String
Required: No

 ** TargetLocationsURL **   <a name="systemsmanager-Type-AutomationExecutionMetadata-TargetLocationsURL"></a>
A publicly accessible URL for a file that contains the `TargetLocations` body. Currently, only files in presigned Amazon S3 buckets are supported
Type: String
Pattern: `^https:\/\/[-a-zA-Z0-9@:%._\+~#=]{1,253}\.s3(\.[a-z\d-]{9,16})?\.amazonaws\.com\/.{1,2000}`
Required: No

 ** TargetMaps **   <a name="systemsmanager-Type-AutomationExecutionMetadata-TargetMaps"></a>
The specified key-value mapping of document parameters to target resources.
Type: Array of string to array of strings maps
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Map Entries: Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** TargetParameterName **   <a name="systemsmanager-Type-AutomationExecutionMetadata-TargetParameterName"></a>
The list of execution outputs as defined in the Automation runbook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** Targets **   <a name="systemsmanager-Type-AutomationExecutionMetadata-Targets"></a>
The targets defined by the user when starting the automation.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** TriggeredAlarms **   <a name="systemsmanager-Type-AutomationExecutionMetadata-TriggeredAlarms"></a>
The CloudWatch alarm that was invoked by the automation.
Type: Array of [AlarmStateInformation](API_AlarmStateInformation.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** WarningMessage **   <a name="systemsmanager-Type-AutomationExecutionMetadata-WarningMessage"></a>
A message that describes a non-critical issue that occurred during the automation execution.
Type: String
Required: No

## See Also
<a name="API_AutomationExecutionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AutomationExecutionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AutomationExecutionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AutomationExecutionMetadata)
