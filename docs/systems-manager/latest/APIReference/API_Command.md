---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_Command.html
---

# Command
<a name="API_Command"></a>

Describes a command request.

## Contents
<a name="API_Command_Contents"></a>

 ** AlarmConfiguration **   <a name="systemsmanager-Type-Command-AlarmConfiguration"></a>
The details for the CloudWatch alarm applied to your command.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** CloudWatchOutputConfig **   <a name="systemsmanager-Type-Command-CloudWatchOutputConfig"></a>
Amazon CloudWatch Logs information where you want AWS Systems Manager to send the command output.
Type: [CloudWatchOutputConfig](API_CloudWatchOutputConfig.md) object
Required: No

 ** CommandId **   <a name="systemsmanager-Type-Command-CommandId"></a>
A unique identifier for this command.
Type: String
Length Constraints: Fixed length of 36.
Required: No

 ** Comment **   <a name="systemsmanager-Type-Command-Comment"></a>
User-specified information about the command, such as a brief description of what the command should do.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** CompletedCount **   <a name="systemsmanager-Type-Command-CompletedCount"></a>
The number of targets for which the command invocation reached a terminal state. Terminal states include the following: Success, Failed, Execution Timed Out, Delivery Timed Out, Cancelled, Terminated, or Undeliverable.
Type: Integer
Required: No

 ** DeliveryTimedOutCount **   <a name="systemsmanager-Type-Command-DeliveryTimedOutCount"></a>
The number of targets for which the status is Delivery Timed Out.
Type: Integer
Required: No

 ** DocumentName **   <a name="systemsmanager-Type-Command-DocumentName"></a>
The name of the document requested for execution.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** DocumentVersion **   <a name="systemsmanager-Type-Command-DocumentVersion"></a>
The Systems Manager document (SSM document) version.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** ErrorCount **   <a name="systemsmanager-Type-Command-ErrorCount"></a>
The number of targets for which the status is Failed or Execution Timed Out.
Type: Integer
Required: No

 ** ExpiresAfter **   <a name="systemsmanager-Type-Command-ExpiresAfter"></a>
If a command expires, it changes status to `DeliveryTimedOut` for all invocations that have the status `InProgress`, `Pending`, or `Delayed`. `ExpiresAfter` is calculated based on the total timeout for the overall command. For more information, see [Understanding command timeout values](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html?icmpid=docs_ec2_console#monitor-about-status-timeouts) in the * AWS Systems Manager User Guide*.
Type: Timestamp
Required: No

 ** InstanceIds **   <a name="systemsmanager-Type-Command-InstanceIds"></a>
The managed node IDs against which this command was requested.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

 ** MaxConcurrency **   <a name="systemsmanager-Type-Command-MaxConcurrency"></a>
The maximum number of managed nodes that are allowed to run the command at the same time. You can specify a number of managed nodes, such as 10, or a percentage of nodes, such as 10%. The default value is 50. For more information about how to use `MaxConcurrency`, see [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) in the * AWS Systems Manager User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`
Required: No

 ** MaxErrors **   <a name="systemsmanager-Type-Command-MaxErrors"></a>
The maximum number of errors allowed before the system stops sending the command to additional targets. You can specify a number of errors, such as 10, or a percentage or errors, such as 10%. The default value is `0`. For more information about how to use `MaxErrors`, see [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) in the * AWS Systems Manager User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`
Required: No

 ** NotificationConfig **   <a name="systemsmanager-Type-Command-NotificationConfig"></a>
Configurations for sending notifications about command status changes.
Type: [NotificationConfig](API_NotificationConfig.md) object
Required: No

 ** OutputS3BucketName **   <a name="systemsmanager-Type-Command-OutputS3BucketName"></a>
The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

 ** OutputS3KeyPrefix **   <a name="systemsmanager-Type-Command-OutputS3KeyPrefix"></a>
The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** OutputS3Region **   <a name="systemsmanager-Type-Command-OutputS3Region"></a>
(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the AWS Region of the S3 bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 20.
Required: No

 ** Parameters **   <a name="systemsmanager-Type-Command-Parameters"></a>
The parameter values to be inserted in the document when running the command.
Type: String to array of strings map
Required: No

 ** RequestedDateTime **   <a name="systemsmanager-Type-Command-RequestedDateTime"></a>
The date and time the command was requested.
Type: Timestamp
Required: No

 ** ServiceRole **   <a name="systemsmanager-Type-Command-ServiceRole"></a>
The AWS Identity and Access Management (IAM) service role that Run Command, a tool in AWS Systems Manager, uses to act on your behalf when sending notifications about command status changes.
Type: String
Required: No

 ** Status **   <a name="systemsmanager-Type-Command-Status"></a>
The status of the command.
Type: String
Valid Values: `Pending | InProgress | Success | Cancelled | Failed | TimedOut | Cancelling`
Required: No

 ** StatusDetails **   <a name="systemsmanager-Type-Command-StatusDetails"></a>
A detailed status of the command execution. `StatusDetails` includes more information than `Status` because it includes states resulting from error and concurrency control parameters. `StatusDetails` can show different results than Status. For more information about these statuses, see [Understanding command statuses](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html) in the * AWS Systems Manager User Guide*. StatusDetails can be one of the following values:
+ Pending: The command hasn't been sent to any managed nodes.
+ In Progress: The command has been sent to at least one managed node but hasn't reached a final state on all managed nodes.
+ Success: The command successfully ran on all invocations. This is a terminal state.
+ Delivery Timed Out: The value of MaxErrors or more command invocations shows a status of Delivery Timed Out. This is a terminal state.
+ Execution Timed Out: The value of MaxErrors or more command invocations shows a status of Execution Timed Out. This is a terminal state.
+ Failed: The value of MaxErrors or more command invocations shows a status of Failed. This is a terminal state.
+ Incomplete: The command was attempted on all managed nodes and one or more invocations doesn't have a value of Success but not enough invocations failed for the status to be Failed. This is a terminal state.
+ Cancelled: The command was terminated before it was completed. This is a terminal state.
+ Rate Exceeded: The number of managed nodes targeted by the command exceeded the account limit for pending invocations. The system has canceled the command before running it on any managed node. This is a terminal state.
+ Delayed: The system attempted to send the command to the managed node but wasn't successful. The system retries again.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** TargetCount **   <a name="systemsmanager-Type-Command-TargetCount"></a>
The number of targets for the command.
Type: Integer
Required: No

 ** Targets **   <a name="systemsmanager-Type-Command-Targets"></a>
An array of search criteria that targets managed nodes using a Key,Value combination that you specify. Targets is required if you don't provide one or more managed node IDs in the call.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** TimeoutSeconds **   <a name="systemsmanager-Type-Command-TimeoutSeconds"></a>
The `TimeoutSeconds` value specified for a command.
Type: Integer
Valid Range: Minimum value of 30. Maximum value of 2592000.
Required: No

 ** TriggeredAlarms **   <a name="systemsmanager-Type-Command-TriggeredAlarms"></a>
The CloudWatch alarm that was invoked by the command.
Type: Array of [AlarmStateInformation](API_AlarmStateInformation.md) objects
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_Command_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/Command)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/Command)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/Command)
