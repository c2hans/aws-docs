---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetCommandInvocation.html
---

# GetCommandInvocation
<a name="API_GetCommandInvocation"></a>

Returns detailed information about command execution for an invocation or plugin. The Run Command API follows an eventual consistency model, due to the distributed nature of the system supporting the API. This means that the result of an API command you run that affects your resources might not be immediately visible to all subsequent commands you run. You should keep this in mind when you carry out an API command that immediately follows a previous API command.

 `GetCommandInvocation` only gives the execution status of a plugin in a document. To get the command execution status on a specific managed node, use [ListCommandInvocations](API_ListCommandInvocations.md). To get the command execution status across managed nodes, use [ListCommands](API_ListCommands.md).

## Request Syntax
<a name="API_GetCommandInvocation_RequestSyntax"></a>

```
{
   "CommandId": "{{string}}",
   "InstanceId": "{{string}}",
   "PluginName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCommandInvocation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CommandId](#API_GetCommandInvocation_RequestSyntax) **   <a name="systemsmanager-GetCommandInvocation-request-CommandId"></a>
(Required) The parent command ID of the invocation plugin.
Type: String
Length Constraints: Fixed length of 36.
Required: Yes

 ** [InstanceId](#API_GetCommandInvocation_RequestSyntax) **   <a name="systemsmanager-GetCommandInvocation-request-InstanceId"></a>
(Required) The ID of the managed node targeted by the command. A *managed node* can be an Amazon Elastic Compute Cloud (Amazon EC2) instance, edge device, and on-premises server or VM in your hybrid environment that is configured for AWS Systems Manager.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: Yes

 ** [PluginName](#API_GetCommandInvocation_RequestSyntax) **   <a name="systemsmanager-GetCommandInvocation-request-PluginName"></a>
The name of the step for which you want detailed results. If the document contains only one step, you can omit the name and details for that step. If the document contains more than one step, you must specify the name of the step for which you want to view details. Be sure to specify the name of the step, not the name of a plugin like `aws:RunShellScript`.
To find the `PluginName`, check the document content and find the name of the step you want details for. Alternatively, use [ListCommandInvocations](API_ListCommandInvocations.md) with the `CommandId` and `Details` parameters. The `PluginName` is the `Name` attribute of the `CommandPlugin` object in the `CommandPlugins` list.
Type: String
Length Constraints: Minimum length of 4.
Required: No

## Response Syntax
<a name="API_GetCommandInvocation_ResponseSyntax"></a>

```
{
   "CloudWatchOutputConfig": {
      "CloudWatchLogGroupName": "string",
      "CloudWatchOutputEnabled": boolean
   },
   "CommandId": "string",
   "Comment": "string",
   "DocumentName": "string",
   "DocumentVersion": "string",
   "ExecutionElapsedTime": "string",
   "ExecutionEndDateTime": "string",
   "ExecutionStartDateTime": "string",
   "InstanceId": "string",
   "PluginName": "string",
   "ResponseCode": number,
   "StandardErrorContent": "string",
   "StandardErrorUrl": "string",
   "StandardOutputContent": "string",
   "StandardOutputUrl": "string",
   "Status": "string",
   "StatusDetails": "string"
}
```

## Response Elements
<a name="API_GetCommandInvocation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CloudWatchOutputConfig](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-CloudWatchOutputConfig"></a>
Amazon CloudWatch Logs information where Systems Manager sent the command output.
Type: [CloudWatchOutputConfig](API_CloudWatchOutputConfig.md) object

 ** [CommandId](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-CommandId"></a>
The parent command ID of the invocation plugin.
Type: String
Length Constraints: Fixed length of 36.

 ** [Comment](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-Comment"></a>
The comment text for the command.
Type: String
Length Constraints: Maximum length of 100.

 ** [DocumentName](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-DocumentName"></a>
The name of the document that was run. For example, `AWS-RunShellScript`.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`

 ** [DocumentVersion](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-DocumentVersion"></a>
The Systems Manager document (SSM document) version used in the request.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`

 ** [ExecutionElapsedTime](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-ExecutionElapsedTime"></a>
Duration since `ExecutionStartDateTime`.
Type: String
Pattern: `^([\-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d(?!:))?)?(\17[0-5]\d([\.,]\d)?)?([zZ]|([\-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$`

 ** [ExecutionEndDateTime](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-ExecutionEndDateTime"></a>
The date and time the plugin finished running. Date and time are written in ISO 8601 format. For example, June 7, 2017 is represented as 2017-06-7. The following sample AWS CLI command uses the `InvokedAfter` filter.
 `aws ssm list-commands --filters key=InvokedAfter,value=2017-06-07T00:00:00Z`
If the plugin hasn't started to run, the string is empty.
Type: String
Pattern: `^([\-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d(?!:))?)?(\17[0-5]\d([\.,]\d)?)?([zZ]|([\-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$`

 ** [ExecutionStartDateTime](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-ExecutionStartDateTime"></a>
The date and time the plugin started running. Date and time are written in ISO 8601 format. For example, June 7, 2017 is represented as 2017-06-7. The following sample AWS CLI command uses the `InvokedBefore` filter.
 `aws ssm list-commands --filters key=InvokedBefore,value=2017-06-07T00:00:00Z`
If the plugin hasn't started to run, the string is empty.
Type: String
Pattern: `^([\-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d(?!:))?)?(\17[0-5]\d([\.,]\d)?)?([zZ]|([\-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$`

 ** [InstanceId](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-InstanceId"></a>
The ID of the managed node targeted by the command. A *managed node* can be an Amazon Elastic Compute Cloud (Amazon EC2) instance, edge device, or on-premises server or VM in your hybrid environment that is configured for AWS Systems Manager.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`

 ** [PluginName](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-PluginName"></a>
The name of the plugin, or *step name*, for which details are reported. For example, `aws:RunShellScript` is a plugin.
Type: String
Length Constraints: Minimum length of 4.

 ** [ResponseCode](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-ResponseCode"></a>
The error level response code for the plugin script. If the response code is `-1`, then the command hasn't started running on the managed node, or it wasn't received by the node.
Type: Integer

 ** [StandardErrorContent](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-StandardErrorContent"></a>
The first 8,000 characters written by the plugin to `stderr`. If the command hasn't finished running, then this string is empty.
Type: String
Length Constraints: Maximum length of 8000.

 ** [StandardErrorUrl](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-StandardErrorUrl"></a>
The URL for the complete text written by the plugin to `stderr`. If the command hasn't finished running, then this string is empty.
Type: String

 ** [StandardOutputContent](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-StandardOutputContent"></a>
The first 24,000 characters written by the plugin to `stdout`. If the command hasn't finished running, if `ExecutionStatus` is neither Succeeded nor Failed, then this string is empty.
Type: String
Length Constraints: Maximum length of 24000.

 ** [StandardOutputUrl](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-StandardOutputUrl"></a>
The URL for the complete text written by the plugin to `stdout` in Amazon Simple Storage Service (Amazon S3). If an S3 bucket wasn't specified, then this string is empty.
Type: String

 ** [Status](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-Status"></a>
The status of this invocation plugin. This status can be different than `StatusDetails`.
Type: String
Valid Values: `Pending | InProgress | Delayed | Success | Cancelled | TimedOut | Failed | Cancelling`

 ** [StatusDetails](#API_GetCommandInvocation_ResponseSyntax) **   <a name="systemsmanager-GetCommandInvocation-response-StatusDetails"></a>
A detailed status of the command execution for an invocation. `StatusDetails` includes more information than `Status` because it includes states resulting from error and concurrency control parameters. `StatusDetails` can show different results than `Status`. For more information about these statuses, see [Understanding command statuses](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html) in the * AWS Systems Manager User Guide*. `StatusDetails` can be one of the following values:
+ Pending: The command hasn't been sent to the managed node.
+ In Progress: The command has been sent to the managed node but hasn't reached a terminal state.
+ Delayed: The system attempted to send the command to the target, but the target wasn't available. The managed node might not be available because of network issues, because the node was stopped, or for similar reasons. The system will try to send the command again.
+ Success: The command or plugin ran successfully. This is a terminal state.
+ Delivery Timed Out: The command wasn't delivered to the managed node before the delivery timeout expired. Delivery timeouts don't count against the parent command's `MaxErrors` limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
+ Execution Timed Out: The command started to run on the managed node, but the execution wasn't complete before the timeout expired. Execution timeouts count against the `MaxErrors` limit of the parent command. This is a terminal state.
+ Failed: The command wasn't run successfully on the managed node. For a plugin, this indicates that the result code wasn't zero. For a command invocation, this indicates that the result code for one or more plugins wasn't zero. Invocation failures count against the `MaxErrors` limit of the parent command. This is a terminal state.
+ Cancelled: The command was terminated before it was completed. This is a terminal state.
+ Undeliverable: The command can't be delivered to the managed node. The node might not exist or might not be responding. Undeliverable invocations don't count against the parent command's `MaxErrors` limit and don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
+ Terminated: The parent command exceeded its `MaxErrors` limit and subsequent command invocations were canceled by the system. This is a terminal state.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.

## Errors
<a name="API_GetCommandInvocation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidCommandId **
The specified command ID isn't valid. Verify the ID and try again.
HTTP Status Code: 400

 ** InvalidInstanceId **
The following problems can cause this exception:
+ You don't have permission to access the managed node.
+  AWS Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.
+ SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.
+ The managed node isn't in a valid state. Valid states are: `Running`, `Pending`, `Stopped`, and `Stopping`. Invalid states are: `Shutting-down` and `Terminated`.
HTTP Status Code: 400

 ** InvalidPluginName **
The plugin name isn't valid.
HTTP Status Code: 400

 ** InvocationDoesNotExist **
The command ID and managed node ID you specified didn't match any invocations. Verify the command ID and the managed node ID and try again.
HTTP Status Code: 400

## Examples
<a name="API_GetCommandInvocation_Examples"></a>

### Example
<a name="API_GetCommandInvocation_Example_1"></a>

This example illustrates one usage of GetCommandInvocation.

#### Sample Request
<a name="API_GetCommandInvocation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.GetCommandInvocation
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240220T235111Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240220/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 90

{
    "CommandId": "32d70fe0-ddbc-4a4e-943f-ffcbcEXAMPLE",
    "InstanceId": "i-02573cafcfEXAMPLE"
}
```

#### Sample Response
<a name="API_GetCommandInvocation_Example_1_Response"></a>

```
{
    "CloudWatchOutputConfig": {
        "CloudWatchLogGroupName": "",
        "CloudWatchOutputEnabled": false
    },
    "CommandId": "32d70fe0-ddbc-4a4e-943f-ffcbcEXAMPLE",
    "Comment": "b48291dd-ba76-43e0-b9df-13e11ddaac26:6960febb-2907-4b59-8e1a-d6ce8EXAMPLE",
    "DocumentName": "AWS-UpdateSSMAgent",
    "DocumentVersion": "",
    "ExecutionElapsedTime": "PT44.002S",
    "ExecutionEndDateTime": "2024-02-20T23:35:26.758Z",
    "ExecutionStartDateTime": "2024-02-20T23:34:42.758Z",
    "InstanceId": "i-02573cafcfEXAMPLE",
    "PluginName": "aws:updateSsmAgent",
    "ResponseCode": 0,
    "StandardErrorContent": "",
    "StandardErrorUrl": "",
    "StandardOutputContent": "Updating amazon-ssm-agent from 2.3.842.0 to latest
        \nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/ssm-agent-manifest.json
        \nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/amazon-ssm-agent-updater/2.3.871.0/amazon-ssm-agent-updater-windows-amd64.zip
        \nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/amazon-ssm-agent/2.3.842.0/amazon-ssm-agent-windows-amd64.zip
        \nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/amazon-ssm-agent/2.3.871.0/amazon-ssm-agent-windows-amd64.zip
        \nInitiating amazon-ssm-agent update to 2.3.871.0
        \namazon-ssm-agent updated successfully to 2.3.871.0",
    "StandardOutputUrl": "",
    "Status": "Success",
    "StatusDetails": "Success"
}
```

## See Also
<a name="API_GetCommandInvocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetCommandInvocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetCommandInvocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetCommandInvocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetCommandInvocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetCommandInvocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetCommandInvocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetCommandInvocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetCommandInvocation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetCommandInvocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetCommandInvocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
