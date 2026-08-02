---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowTask.html
---

# MaintenanceWindowTask
<a name="API_MaintenanceWindowTask"></a>

Information about a task defined for a maintenance window.

## Contents
<a name="API_MaintenanceWindowTask_Contents"></a>

 ** AlarmConfiguration **   <a name="systemsmanager-Type-MaintenanceWindowTask-AlarmConfiguration"></a>
The details for the CloudWatch alarm applied to your maintenance window task.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** CutoffBehavior **   <a name="systemsmanager-Type-MaintenanceWindowTask-CutoffBehavior"></a>
The specification for whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached.
Type: String
Valid Values: `CONTINUE_TASK | CANCEL_TASK`
Required: No

 ** Description **   <a name="systemsmanager-Type-MaintenanceWindowTask-Description"></a>
A description of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** LoggingInfo **   <a name="systemsmanager-Type-MaintenanceWindowTask-LoggingInfo"></a>
Information about an S3 bucket to write task-level logs to.
 `LoggingInfo` has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the `TaskInvocationParameters` structure. For information about how AWS Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
Type: [LoggingInfo](API_LoggingInfo.md) object
Required: No

 ** MaxConcurrency **   <a name="systemsmanager-Type-MaintenanceWindowTask-MaxConcurrency"></a>
The maximum number of targets this task can be run for, in parallel.
Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a [targetless task](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) You must provide a value in all other cases.
For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of `1`. This value doesn't affect the running of your task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`
Required: No

 ** MaxErrors **   <a name="systemsmanager-Type-MaintenanceWindowTask-MaxErrors"></a>
The maximum number of errors allowed before this task stops being scheduled.
Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a [targetless task](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) You must provide a value in all other cases.
For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of `1`. This value doesn't affect the running of your task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`
Required: No

 ** Name **   <a name="systemsmanager-Type-MaintenanceWindowTask-Name"></a>
The task name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** Priority **   <a name="systemsmanager-Type-MaintenanceWindowTask-Priority"></a>
The priority of the task in the maintenance window. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** ServiceRoleArn **   <a name="systemsmanager-Type-MaintenanceWindowTask-ServiceRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role for AWS Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run `RegisterTaskWithMaintenanceWindow`.
However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see [Setting up Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html) in the in the * AWS Systems Manager User Guide*.
Type: String
Required: No

 ** Targets **   <a name="systemsmanager-Type-MaintenanceWindowTask-Targets"></a>
The targets (either managed nodes or tags). Managed nodes are specified using `Key=instanceids,Values=<instanceid1>,<instanceid2>`. Tags are specified using `Key=<tag name>,Values=<tag value>`.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** TaskArn **   <a name="systemsmanager-Type-MaintenanceWindowTask-TaskArn"></a>
The resource that the task uses during execution. For `RUN_COMMAND` and `AUTOMATION` task types, `TaskArn` is the AWS Systems Manager (SSM document) name or ARN. For `LAMBDA` tasks, it's the function name or ARN. For `STEP_FUNCTIONS` tasks, it's the state machine ARN.
Maintenance Window does not validate the TaskArn when you register a task. A successful registration does not guarantee that the TaskArn is valid.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** TaskParameters **   <a name="systemsmanager-Type-MaintenanceWindowTask-TaskParameters"></a>
The parameters that should be passed to the task when it is run.
 `TaskParameters` has been deprecated. To specify parameters to pass to a task when it runs, instead use the `Parameters` option in the `TaskInvocationParameters` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
Type: String to [MaintenanceWindowTaskParameterValueExpression](API_MaintenanceWindowTaskParameterValueExpression.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Type **   <a name="systemsmanager-Type-MaintenanceWindowTask-Type"></a>
The type of task.
Type: String
Valid Values: `RUN_COMMAND | AUTOMATION | STEP_FUNCTIONS | LAMBDA`
Required: No

 ** WindowId **   <a name="systemsmanager-Type-MaintenanceWindowTask-WindowId"></a>
The ID of the maintenance window where the task is registered.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: No

 ** WindowTaskId **   <a name="systemsmanager-Type-MaintenanceWindowTask-WindowTaskId"></a>
The task ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: No

## See Also
<a name="API_MaintenanceWindowTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/MaintenanceWindowTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/MaintenanceWindowTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/MaintenanceWindowTask)
