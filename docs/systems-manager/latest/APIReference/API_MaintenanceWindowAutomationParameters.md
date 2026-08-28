---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowAutomationParameters.html
---

# MaintenanceWindowAutomationParameters
<a name="API_MaintenanceWindowAutomationParameters"></a>

The parameters for an `AUTOMATION` task type.

## Contents
<a name="API_MaintenanceWindowAutomationParameters_Contents"></a>

 ** DocumentVersion **   <a name="systemsmanager-Type-MaintenanceWindowAutomationParameters-DocumentVersion"></a>
The version of an Automation runbook to use during task execution.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** Parameters **   <a name="systemsmanager-Type-MaintenanceWindowAutomationParameters-Parameters"></a>
The parameters for the `AUTOMATION` task.
For information about specifying and updating task parameters, see [RegisterTaskWithMaintenanceWindow](API_RegisterTaskWithMaintenanceWindow.md) and [UpdateMaintenanceWindowTask](API_UpdateMaintenanceWindowTask.md).
 `LoggingInfo` has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the `TaskInvocationParameters` structure. For information about how AWS Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
 `TaskParameters` has been deprecated. To specify parameters to pass to a task when it runs, instead use the `Parameters` option in the `TaskInvocationParameters` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
For `AUTOMATION` task types, AWS Systems Manager ignores any values specified for these parameters.
Type: String to array of strings map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_MaintenanceWindowAutomationParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/MaintenanceWindowAutomationParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/MaintenanceWindowAutomationParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/MaintenanceWindowAutomationParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
