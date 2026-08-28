---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowLambdaParameters.html
---

# MaintenanceWindowLambdaParameters
<a name="API_MaintenanceWindowLambdaParameters"></a>

The parameters for a `LAMBDA` task type.

For information about specifying and updating task parameters, see [RegisterTaskWithMaintenanceWindow](API_RegisterTaskWithMaintenanceWindow.md) and [UpdateMaintenanceWindowTask](API_UpdateMaintenanceWindowTask.md).

**Note**
 `LoggingInfo` has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the `TaskInvocationParameters` structure. For information about how AWS Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
 `TaskParameters` has been deprecated. To specify parameters to pass to a task when it runs, instead use the `Parameters` option in the `TaskInvocationParameters` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
For Lambda tasks, Systems Manager ignores any values specified for TaskParameters and LoggingInfo.

## Contents
<a name="API_MaintenanceWindowLambdaParameters_Contents"></a>

 ** ClientContext **   <a name="systemsmanager-Type-MaintenanceWindowLambdaParameters-ClientContext"></a>
Pass client-specific information to the AWS Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8000.
Required: No

 ** Payload **   <a name="systemsmanager-Type-MaintenanceWindowLambdaParameters-Payload"></a>
JSON to provide to your Lambda function as input.
Type: Base64-encoded binary data object
Length Constraints: Maximum length of 4096.
Required: No

 ** Qualifier **   <a name="systemsmanager-Type-MaintenanceWindowLambdaParameters-Qualifier"></a>
(Optional) Specify an Lambda function version or alias name. If you specify a function version, the operation uses the qualified function Amazon Resource Name (ARN) to invoke a specific Lambda function. If you specify an alias name, the operation uses the alias ARN to invoke the Lambda function version to which the alias points.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_MaintenanceWindowLambdaParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/MaintenanceWindowLambdaParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/MaintenanceWindowLambdaParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/MaintenanceWindowLambdaParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
