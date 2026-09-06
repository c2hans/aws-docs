---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowExecutionTaskIdentity.html
---

# MaintenanceWindowExecutionTaskIdentity
<a name="API_MaintenanceWindowExecutionTaskIdentity"></a>

Information about a task execution performed as part of a maintenance window execution.

## Contents
<a name="API_MaintenanceWindowExecutionTaskIdentity_Contents"></a>

 ** AlarmConfiguration **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskIdentity-AlarmConfiguration"></a>
The details for the CloudWatch alarm applied to your maintenance window task.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** EndTime **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskIdentity-EndTime"></a>
The time the task execution finished.
Type: Timestamp
Required: No

 ** StartTime **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskIdentity-StartTime"></a>
The time the task execution started.
Type: Timestamp
Required: No

 ** Status **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskIdentity-Status"></a>
The status of the task execution.
Type: String
Valid Values: `PENDING | IN_PROGRESS | SUCCESS | FAILED | TIMED_OUT | CANCELLING | CANCELLED | SKIPPED_OVERLAPPING`
Required: No

 ** StatusDetails **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskIdentity-StatusDetails"></a>
The details explaining the status of the task execution. Not available for all status values.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.
Required: No

 ** TaskArn **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskIdentity-TaskArn"></a>
The Amazon Resource Name (ARN) of the task that ran.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** TaskExecutionId **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskIdentity-TaskExecutionId"></a>
The ID of the specific task execution in the maintenance window execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: No

 ** TaskType **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskIdentity-TaskType"></a>
The type of task that ran.
Type: String
Valid Values: `RUN_COMMAND | AUTOMATION | STEP_FUNCTIONS | LAMBDA`
Required: No

 ** TriggeredAlarms **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskIdentity-TriggeredAlarms"></a>
The CloudWatch alarm that was invoked by the maintenance window task.
Type: Array of [AlarmStateInformation](API_AlarmStateInformation.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** WindowExecutionId **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskIdentity-WindowExecutionId"></a>
The ID of the maintenance window execution that ran the task.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: No

## See Also
<a name="API_MaintenanceWindowExecutionTaskIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/MaintenanceWindowExecutionTaskIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/MaintenanceWindowExecutionTaskIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/MaintenanceWindowExecutionTaskIdentity)
