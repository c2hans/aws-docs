---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowExecutionTaskInvocationIdentity.html
---

# MaintenanceWindowExecutionTaskInvocationIdentity
<a name="API_MaintenanceWindowExecutionTaskInvocationIdentity"></a>

Describes the information about a task invocation for a particular target as part of a task execution performed as part of a maintenance window execution.

## Contents
<a name="API_MaintenanceWindowExecutionTaskInvocationIdentity_Contents"></a>

 ** EndTime **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskInvocationIdentity-EndTime"></a>
The time the invocation finished.
Type: Timestamp
Required: No

 ** ExecutionId **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskInvocationIdentity-ExecutionId"></a>
The ID of the action performed in the service that actually handled the task invocation. If the task type is `RUN_COMMAND`, this value is the command ID.
Type: String
Required: No

 ** InvocationId **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskInvocationIdentity-InvocationId"></a>
The ID of the task invocation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: No

 ** OwnerInformation **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskInvocationIdentity-OwnerInformation"></a>
User-provided value that was specified when the target was registered with the maintenance window. This was also included in any Amazon CloudWatch Events events raised during the task invocation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Parameters **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskInvocationIdentity-Parameters"></a>
The parameters that were provided for the invocation when it was run.
Type: String
Required: No

 ** StartTime **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskInvocationIdentity-StartTime"></a>
The time the invocation started.
Type: Timestamp
Required: No

 ** Status **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskInvocationIdentity-Status"></a>
The status of the task invocation.
Type: String
Valid Values: `PENDING | IN_PROGRESS | SUCCESS | FAILED | TIMED_OUT | CANCELLING | CANCELLED | SKIPPED_OVERLAPPING`
Required: No

 ** StatusDetails **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskInvocationIdentity-StatusDetails"></a>
The details explaining the status of the task invocation. Not available for all status values.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.
Required: No

 ** TaskExecutionId **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskInvocationIdentity-TaskExecutionId"></a>
The ID of the specific task execution in the maintenance window execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: No

 ** TaskType **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskInvocationIdentity-TaskType"></a>
The task type.
Type: String
Valid Values: `RUN_COMMAND | AUTOMATION | STEP_FUNCTIONS | LAMBDA`
Required: No

 ** WindowExecutionId **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskInvocationIdentity-WindowExecutionId"></a>
The ID of the maintenance window execution that ran the task.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: No

 ** WindowTargetId **   <a name="systemsmanager-Type-MaintenanceWindowExecutionTaskInvocationIdentity-WindowTargetId"></a>
The ID of the target definition in this maintenance window the invocation was performed for.
Type: String
Length Constraints: Maximum length of 36.
Required: No

## See Also
<a name="API_MaintenanceWindowExecutionTaskInvocationIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/MaintenanceWindowExecutionTaskInvocationIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/MaintenanceWindowExecutionTaskInvocationIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/MaintenanceWindowExecutionTaskInvocationIdentity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
