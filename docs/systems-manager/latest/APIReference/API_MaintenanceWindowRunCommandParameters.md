---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowRunCommandParameters.html
---

# MaintenanceWindowRunCommandParameters
<a name="API_MaintenanceWindowRunCommandParameters"></a>

The parameters for a `RUN_COMMAND` task type.

For information about specifying and updating task parameters, see [RegisterTaskWithMaintenanceWindow](API_RegisterTaskWithMaintenanceWindow.md) and [UpdateMaintenanceWindowTask](API_UpdateMaintenanceWindowTask.md).

**Note**
 `LoggingInfo` has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the `TaskInvocationParameters` structure. For information about how AWS Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
 `TaskParameters` has been deprecated. To specify parameters to pass to a task when it runs, instead use the `Parameters` option in the `TaskInvocationParameters` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).
For `RUN_COMMAND` tasks, Systems Manager uses specified values for `TaskParameters` and `LoggingInfo` only if no values are specified for `TaskInvocationParameters`.

## Contents
<a name="API_MaintenanceWindowRunCommandParameters_Contents"></a>

 ** CloudWatchOutputConfig **   <a name="systemsmanager-Type-MaintenanceWindowRunCommandParameters-CloudWatchOutputConfig"></a>
Configuration options for sending command output to Amazon CloudWatch Logs.
Type: [CloudWatchOutputConfig](API_CloudWatchOutputConfig.md) object
Required: No

 ** Comment **   <a name="systemsmanager-Type-MaintenanceWindowRunCommandParameters-Comment"></a>
Information about the commands to run.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** DocumentHash **   <a name="systemsmanager-Type-MaintenanceWindowRunCommandParameters-DocumentHash"></a>
The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** DocumentHashType **   <a name="systemsmanager-Type-MaintenanceWindowRunCommandParameters-DocumentHashType"></a>
SHA-256 or SHA-1. SHA-1 hashes have been deprecated.
Type: String
Valid Values: `Sha256 | Sha1`
Required: No

 ** DocumentVersion **   <a name="systemsmanager-Type-MaintenanceWindowRunCommandParameters-DocumentVersion"></a>
The AWS Systems Manager document (SSM document) version to use in the request. You can specify `$DEFAULT`, `$LATEST`, or a specific version number. If you run commands by using the AWS CLI, then you must escape the first two options by using a backslash. If you specify a version number, then you don't need to use the backslash. For example:
 `--document-version "\$DEFAULT"`
 `--document-version "\$LATEST"`
 `--document-version "3"`
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** NotificationConfig **   <a name="systemsmanager-Type-MaintenanceWindowRunCommandParameters-NotificationConfig"></a>
Configurations for sending notifications about command status changes on a per-managed node basis.
Type: [NotificationConfig](API_NotificationConfig.md) object
Required: No

 ** OutputS3BucketName **   <a name="systemsmanager-Type-MaintenanceWindowRunCommandParameters-OutputS3BucketName"></a>
The name of the Amazon Simple Storage Service (Amazon S3) bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

 ** OutputS3KeyPrefix **   <a name="systemsmanager-Type-MaintenanceWindowRunCommandParameters-OutputS3KeyPrefix"></a>
The S3 bucket subfolder.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** Parameters **   <a name="systemsmanager-Type-MaintenanceWindowRunCommandParameters-Parameters"></a>
The parameters for the `RUN_COMMAND` task execution.
Type: String to array of strings map
Required: No

 ** ServiceRoleArn **   <a name="systemsmanager-Type-MaintenanceWindowRunCommandParameters-ServiceRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role for AWS Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run `RegisterTaskWithMaintenanceWindow`.
However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see [Setting up Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html) in the in the * AWS Systems Manager User Guide*.
Type: String
Required: No

 ** TimeoutSeconds **   <a name="systemsmanager-Type-MaintenanceWindowRunCommandParameters-TimeoutSeconds"></a>
If this time is reached and the command hasn't already started running, it doesn't run.
Type: Integer
Valid Range: Minimum value of 30. Maximum value of 2592000.
Required: No

## See Also
<a name="API_MaintenanceWindowRunCommandParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/MaintenanceWindowRunCommandParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/MaintenanceWindowRunCommandParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/MaintenanceWindowRunCommandParameters)
