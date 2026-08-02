---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CommandPlugin.html
---

# CommandPlugin
<a name="API_CommandPlugin"></a>

Describes plugin details.

## Contents
<a name="API_CommandPlugin_Contents"></a>

 ** Name **   <a name="systemsmanager-Type-CommandPlugin-Name"></a>
The name of the plugin. Must be one of the following: `aws:updateAgent`, `aws:domainjoin`, `aws:applications`, `aws:runPowerShellScript`, `aws:psmodule`, `aws:cloudWatch`, `aws:runShellScript`, or `aws:updateSSMAgent`.
Type: String
Length Constraints: Minimum length of 4.
Required: No

 ** Output **   <a name="systemsmanager-Type-CommandPlugin-Output"></a>
Output of the plugin execution.
Type: String
Length Constraints: Maximum length of 2500.
Required: No

 ** OutputS3BucketName **   <a name="systemsmanager-Type-CommandPlugin-OutputS3BucketName"></a>
The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:
 `amzn-s3-demo-bucket/my-prefix/i-02573cafcfEXAMPLE/awsrunShellScript`
 `amzn-s3-demo-bucket` is the name of the S3 bucket;
 `my-prefix` is the name of the S3 prefix;
 `i-02573cafcfEXAMPLE` is the managed node ID;
 `awsrunShellScript` is the name of the plugin.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

 ** OutputS3KeyPrefix **   <a name="systemsmanager-Type-CommandPlugin-OutputS3KeyPrefix"></a>
The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:
 `amzn-s3-demo-bucket/my-prefix/i-02573cafcfEXAMPLE/awsrunShellScript`
 `amzn-s3-demo-bucket` is the name of the S3 bucket;
 `my-prefix` is the name of the S3 prefix;
 `i-02573cafcfEXAMPLE` is the managed node ID;
 `awsrunShellScript` is the name of the plugin.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** OutputS3Region **   <a name="systemsmanager-Type-CommandPlugin-OutputS3Region"></a>
(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, AWS Systems Manager automatically determines the S3 bucket region.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 20.
Required: No

 ** ResponseCode **   <a name="systemsmanager-Type-CommandPlugin-ResponseCode"></a>
A numeric response code generated after running the plugin.
Type: Integer
Required: No

 ** ResponseFinishDateTime **   <a name="systemsmanager-Type-CommandPlugin-ResponseFinishDateTime"></a>
The time the plugin stopped running. Could stop prematurely if, for example, a cancel command was sent.
Type: Timestamp
Required: No

 ** ResponseStartDateTime **   <a name="systemsmanager-Type-CommandPlugin-ResponseStartDateTime"></a>
The time the plugin started running.
Type: Timestamp
Required: No

 ** StandardErrorUrl **   <a name="systemsmanager-Type-CommandPlugin-StandardErrorUrl"></a>
The URL for the complete text written by the plugin to stderr. If execution isn't yet complete, then this string is empty.
Type: String
Required: No

 ** StandardOutputUrl **   <a name="systemsmanager-Type-CommandPlugin-StandardOutputUrl"></a>
The URL for the complete text written by the plugin to stdout in Amazon S3. If the S3 bucket for the command wasn't specified, then this string is empty.
Type: String
Required: No

 ** Status **   <a name="systemsmanager-Type-CommandPlugin-Status"></a>
The status of this plugin. You can run a document with multiple plugins.
Type: String
Valid Values: `Pending | InProgress | Success | TimedOut | Cancelled | Failed`
Required: No

 ** StatusDetails **   <a name="systemsmanager-Type-CommandPlugin-StatusDetails"></a>
A detailed status of the plugin execution. `StatusDetails` includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see [Understanding command statuses](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html) in the * AWS Systems Manager User Guide*. StatusDetails can be one of the following values:
+ Pending: The command hasn't been sent to the managed node.
+ In Progress: The command has been sent to the managed node but hasn't reached a terminal state.
+ Success: The execution of the command or plugin was successfully completed. This is a terminal state.
+ Delivery Timed Out: The command wasn't delivered to the managed node before the delivery timeout expired. Delivery timeouts don't count against the parent command's `MaxErrors` limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
+ Execution Timed Out: Command execution started on the managed node, but the execution wasn't complete before the execution timeout expired. Execution timeouts count against the `MaxErrors` limit of the parent command. This is a terminal state.
+ Failed: The command wasn't successful on the managed node. For a plugin, this indicates that the result code wasn't zero. For a command invocation, this indicates that the result code for one or more plugins wasn't zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.
+ Cancelled: The command was terminated before it was completed. This is a terminal state.
+ Undeliverable: The command can't be delivered to the managed node. The managed node might not exist, or it might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit, and they don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
+ Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

## See Also
<a name="API_CommandPlugin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CommandPlugin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CommandPlugin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CommandPlugin)
