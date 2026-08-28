---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowStepFunctionsParameters.html
---

# MaintenanceWindowStepFunctionsParameters
<a name="API_MaintenanceWindowStepFunctionsParameters"></a>

The parameters for a `STEP_FUNCTIONS` task.

For information about specifying and updating task parameters, see [RegisterTaskWithMaintenanceWindow](API_RegisterTaskWithMaintenanceWindow.md) and [UpdateMaintenanceWindowTask](API_UpdateMaintenanceWindowTask.md).

**Note**
 `LoggingInfo` has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the `TaskInvocationParameters` structure. For information about how AWS Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
 `TaskParameters` has been deprecated. To specify parameters to pass to a task when it runs, instead use the `Parameters` option in the `TaskInvocationParameters` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
For Step Functions tasks, Systems Manager ignores any values specified for `TaskParameters` and `LoggingInfo`.

## Contents
<a name="API_MaintenanceWindowStepFunctionsParameters_Contents"></a>

 ** Input **   <a name="systemsmanager-Type-MaintenanceWindowStepFunctionsParameters-Input"></a>
The inputs for the `STEP_FUNCTIONS` task.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** Name **   <a name="systemsmanager-Type-MaintenanceWindowStepFunctionsParameters-Name"></a>
The name of the `STEP_FUNCTIONS` task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: No

## See Also
<a name="API_MaintenanceWindowStepFunctionsParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/MaintenanceWindowStepFunctionsParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/MaintenanceWindowStepFunctionsParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/MaintenanceWindowStepFunctionsParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
