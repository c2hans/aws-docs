---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CommandInvocation.html
---

# CommandInvocation
<a name="API_CommandInvocation"></a>

An invocation is a copy of a command sent to a specific managed node. A command can apply to one or more managed nodes. A command invocation applies to one managed node. For example, if a user runs `SendCommand` against three managed nodes, then a command invocation is created for each requested managed node ID. A command invocation returns status and detail information about a command you ran.

## Contents
<a name="API_CommandInvocation_Contents"></a>

 ** CloudWatchOutputConfig **   <a name="systemsmanager-Type-CommandInvocation-CloudWatchOutputConfig"></a>
Amazon CloudWatch Logs information where you want AWS Systems Manager to send the command output.
Type: [CloudWatchOutputConfig](API_CloudWatchOutputConfig.md) object
Required: No

 ** CommandId **   <a name="systemsmanager-Type-CommandInvocation-CommandId"></a>
The command against which this invocation was requested.
Type: String
Length Constraints: Fixed length of 36.
Required: No

 ** CommandPlugins **   <a name="systemsmanager-Type-CommandInvocation-CommandPlugins"></a>
Plugins processed by the command.
Type: Array of [CommandPlugin](API_CommandPlugin.md) objects
Required: No

 ** Comment **   <a name="systemsmanager-Type-CommandInvocation-Comment"></a>
User-specified information about the command, such as a brief description of what the command should do.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** DocumentName **   <a name="systemsmanager-Type-CommandInvocation-DocumentName"></a>
The document name that was requested for execution.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** DocumentVersion **   <a name="systemsmanager-Type-CommandInvocation-DocumentVersion"></a>
The Systems Manager document (SSM document) version.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** InstanceId **   <a name="systemsmanager-Type-CommandInvocation-InstanceId"></a>
The managed node ID in which this invocation was requested.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

 ** InstanceName **   <a name="systemsmanager-Type-CommandInvocation-InstanceName"></a>
The fully qualified host name of the managed node.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** NotificationConfig **   <a name="systemsmanager-Type-CommandInvocation-NotificationConfig"></a>
Configurations for sending notifications about command status changes on a per managed node basis.
Type: [NotificationConfig](API_NotificationConfig.md) object
Required: No

 ** RequestedDateTime **   <a name="systemsmanager-Type-CommandInvocation-RequestedDateTime"></a>
The time and date the request was sent to this managed node.
Type: Timestamp
Required: No

 ** ServiceRole **   <a name="systemsmanager-Type-CommandInvocation-ServiceRole"></a>
The AWS Identity and Access Management (IAM) service role that Run Command, a tool in AWS Systems Manager, uses to act on your behalf when sending notifications about command status changes on a per managed node basis.
Type: String
Required: No

 ** StandardErrorUrl **   <a name="systemsmanager-Type-CommandInvocation-StandardErrorUrl"></a>
The URL to the plugin's StdErr file in Amazon Simple Storage Service (Amazon S3), if the S3 bucket was defined for the parent command. For an invocation, `StandardErrorUrl` is populated if there is just one plugin defined for the command, and the S3 bucket was defined for the command.
Type: String
Required: No

 ** StandardOutputUrl **   <a name="systemsmanager-Type-CommandInvocation-StandardOutputUrl"></a>
The URL to the plugin's StdOut file in Amazon Simple Storage Service (Amazon S3), if the S3 bucket was defined for the parent command. For an invocation, `StandardOutputUrl` is populated if there is just one plugin defined for the command, and the S3 bucket was defined for the command.
Type: String
Required: No

 ** Status **   <a name="systemsmanager-Type-CommandInvocation-Status"></a>
Whether or not the invocation succeeded, failed, or is pending.
Type: String
Valid Values: `Pending | InProgress | Delayed | Success | Cancelled | TimedOut | Failed | Cancelling`
Required: No

 ** StatusDetails **   <a name="systemsmanager-Type-CommandInvocation-StatusDetails"></a>
A detailed status of the command execution for each invocation (each managed node targeted by the command). StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see [Understanding command statuses](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html) in the * AWS Systems Manager User Guide*. StatusDetails can be one of the following values:
+ Pending: The command hasn't been sent to the managed node.
+ In Progress: The command has been sent to the managed node but hasn't reached a terminal state.
+ Success: The execution of the command or plugin was successfully completed. This is a terminal state.
+ Delivery Timed Out: The command wasn't delivered to the managed node before the delivery timeout expired. Delivery timeouts don't count against the parent command's `MaxErrors` limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
+ Execution Timed Out: Command execution started on the managed node, but the execution wasn't complete before the execution timeout expired. Execution timeouts count against the `MaxErrors` limit of the parent command. This is a terminal state.
+ Failed: The command wasn't successful on the managed node. For a plugin, this indicates that the result code wasn't zero. For a command invocation, this indicates that the result code for one or more plugins wasn't zero. Invocation failures count against the `MaxErrors` limit of the parent command. This is a terminal state.
+ Cancelled: The command was terminated before it was completed. This is a terminal state.
+ Undeliverable: The command can't be delivered to the managed node. The managed node might not exist or might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit and don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
+ Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.
+ Delayed: The system attempted to send the command to the managed node but wasn't successful. The system retries again.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** TraceOutput **   <a name="systemsmanager-Type-CommandInvocation-TraceOutput"></a>
 Gets the trace output sent by the agent.
Type: String
Length Constraints: Maximum length of 2500.
Required: No

## See Also
<a name="API_CommandInvocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CommandInvocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CommandInvocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CommandInvocation)
