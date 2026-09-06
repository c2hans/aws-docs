---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListCommandInvocations.html
---

# ListCommandInvocations
<a name="API_ListCommandInvocations"></a>

An invocation is copy of a command sent to a specific managed node. A command can apply to one or more managed nodes. A command invocation applies to one managed node. For example, if a user runs `SendCommand` against three managed nodes, then a command invocation is created for each requested managed node ID. `ListCommandInvocations` provide status about command execution.

## Request Syntax
<a name="API_ListCommandInvocations_RequestSyntax"></a>

```
{
   "CommandId": "{{string}}",
   "Details": {{boolean}},
   "Filters": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCommandInvocations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CommandId](#API_ListCommandInvocations_RequestSyntax) **   <a name="systemsmanager-ListCommandInvocations-request-CommandId"></a>
(Optional) The invocations for a specific command ID.
Type: String
Length Constraints: Fixed length of 36.
Required: No

 ** [Details](#API_ListCommandInvocations_RequestSyntax) **   <a name="systemsmanager-ListCommandInvocations-request-Details"></a>
(Optional) If set this returns the response of the command executions and any command output. The default value is `false`.
Type: Boolean
Required: No

 ** [Filters](#API_ListCommandInvocations_RequestSyntax) **   <a name="systemsmanager-ListCommandInvocations-request-Filters"></a>
(Optional) One or more filters. Use a filter to return a more specific list of results.
Type: Array of [CommandFilter](API_CommandFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [InstanceId](#API_ListCommandInvocations_RequestSyntax) **   <a name="systemsmanager-ListCommandInvocations-request-InstanceId"></a>
(Optional) The command execution details for a specific managed node ID.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

 ** [MaxResults](#API_ListCommandInvocations_RequestSyntax) **   <a name="systemsmanager-ListCommandInvocations-request-MaxResults"></a>
(Optional) The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListCommandInvocations_RequestSyntax) **   <a name="systemsmanager-ListCommandInvocations-request-NextToken"></a>
(Optional) The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_ListCommandInvocations_ResponseSyntax"></a>

```
{
   "CommandInvocations": [
      {
         "CloudWatchOutputConfig": {
            "CloudWatchLogGroupName": "string",
            "CloudWatchOutputEnabled": boolean
         },
         "CommandId": "string",
         "CommandPlugins": [
            {
               "Name": "string",
               "Output": "string",
               "OutputS3BucketName": "string",
               "OutputS3KeyPrefix": "string",
               "OutputS3Region": "string",
               "ResponseCode": number,
               "ResponseFinishDateTime": number,
               "ResponseStartDateTime": number,
               "StandardErrorUrl": "string",
               "StandardOutputUrl": "string",
               "Status": "string",
               "StatusDetails": "string"
            }
         ],
         "Comment": "string",
         "DocumentName": "string",
         "DocumentVersion": "string",
         "InstanceId": "string",
         "InstanceName": "string",
         "NotificationConfig": {
            "NotificationArn": "string",
            "NotificationEvents": [ "string" ],
            "NotificationType": "string"
         },
         "RequestedDateTime": number,
         "ServiceRole": "string",
         "StandardErrorUrl": "string",
         "StandardOutputUrl": "string",
         "Status": "string",
         "StatusDetails": "string",
         "TraceOutput": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCommandInvocations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CommandInvocations](#API_ListCommandInvocations_ResponseSyntax) **   <a name="systemsmanager-ListCommandInvocations-response-CommandInvocations"></a>
(Optional) A list of all invocations.
Type: Array of [CommandInvocation](API_CommandInvocation.md) objects

 ** [NextToken](#API_ListCommandInvocations_ResponseSyntax) **   <a name="systemsmanager-ListCommandInvocations-response-NextToken"></a>
(Optional) The token for the next set of items to return. (You received this token from a previous call.)
Type: String

## Errors
<a name="API_ListCommandInvocations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidCommandId **
The specified command ID isn't valid. Verify the ID and try again.
HTTP Status Code: 400

 ** InvalidFilterKey **
The specified key isn't valid.
HTTP Status Code: 400

 ** InvalidInstanceId **
The following problems can cause this exception:
+ You don't have permission to access the managed node.
+  AWS Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.
+ SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.
+ The managed node isn't in a valid state. Valid states are: `Running`, `Pending`, `Stopped`, and `Stopping`. Invalid states are: `Shutting-down` and `Terminated`.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_ListCommandInvocations_Examples"></a>

### Example
<a name="API_ListCommandInvocations_Example_1"></a>

This example illustrates one usage of ListCommandInvocations.

#### Sample Request
<a name="API_ListCommandInvocations_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListCommandInvocations
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240221T000322Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240221/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 53

{
    "CommandId": "4171bb3b-fe26-48ea-94fe-d1727b4d58e5"
}
```

#### Sample Response
<a name="API_ListCommandInvocations_Example_1_Response"></a>

```
{
    "CommandInvocations": [
        {
            "CloudWatchOutputConfig": {
                "CloudWatchLogGroupName": "",
                "CloudWatchOutputEnabled": false
            },
            "CommandId": "4171bb3b-fe26-48ea-94fe-d1727EXAMPLE",
            "CommandPlugins": [],
            "Comment": "",
            "DocumentName": "AWS-FindWindowsUpdates",
            "DocumentVersion": "1",
            "InstanceId": "i-02573cafcfEXAMPLE",
            "InstanceName": "EXAMPLE-4J5FVEG.WORKGROUP",
            "NotificationConfig": {
                "NotificationArn": "arn:aws:sns:us-east-2:111122223333:my-us-east-2-notification-arn",
                "NotificationEvents": [
                    "All"
                ],
                "NotificationType": "Invocation"
            },
            "RequestedDateTime": 1579893879.775,
            "ServiceRole": "arn:aws:iam::111122223333:role/my-SNS-notifications-role",
            "StandardErrorUrl": "https://s3.us-east-2.amazonaws.com/amzn-s3-demo-bucket/my-output/1231bb3b-fe26-48ea-94fe-d1727EXAMPLE/i-02573cafcfEXAMPLE/awsrunPowerShellScript/0.awsrunPowerShellScript/stderr",
            "StandardOutputUrl": "https://s3.us-east-2.amazonaws.com/amzn-s3-demo-bucket/my-output/1231bb3b-fe26-48ea-94fe-d1727EXAMPLE/i-02573cafcfEXAMPLE/awsrunPowerShellScript/0.awsrunPowerShellScript/stdout",
            "Status": "Success",
            "StatusDetails": "Success"
        },
        {
            "CloudWatchOutputConfig": {
                "CloudWatchLogGroupName": "",
                "CloudWatchOutputEnabled": false
            },
            "CommandId": "4171bb3b-fe26-48ea-94fe-d1727EXAMPLE",
            "CommandPlugins": [],
            "Comment": "",
            "DocumentName": "AWS-FindWindowsUpdates",
            "DocumentVersion": "1",
            "InstanceId": "i-0471e04240EXAMPLE",
            "InstanceName": "EXAMPLE-A1PDOM8.WORKGROUP",
            "NotificationConfig": {
                "NotificationArn": "arn:aws:sns:us-east-2:111122223333:my-us-east-2-notification-arn",
                "NotificationEvents": [
                    "All"
                ],
                "NotificationType": "Invocation"
            },
            "RequestedDateTime": 1579893879.6,
            "ServiceRole": "arn:aws:iam::111122223333:role/my-SNS-notifications-role",
            "StandardErrorUrl": "https://s3.us-east-2.amazonaws.com/amzn-s3-demo-bucket/my-output/4171bb3b-fe26-48ea-94fe-d1727EXAMPLE/i-0471e04240EXAMPLE/awsrunPowerShellScript/0.awsrunPowerShellScript/stderr",
            "StandardOutputUrl": "https://s3.us-east-2.amazonaws.com/amzn-s3-demo-bucket/my-output/4171bb3b-fe26-48ea-94fe-d1727EXAMPLE/i-0471e04240EXAMPLE/awsrunPowerShellScript/0.awsrunPowerShellScript/stdout",
            "Status": "Success",
            "StatusDetails": "Success"
        }
    ]
}
```

## See Also
<a name="API_ListCommandInvocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListCommandInvocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListCommandInvocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListCommandInvocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListCommandInvocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListCommandInvocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListCommandInvocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListCommandInvocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListCommandInvocations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListCommandInvocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListCommandInvocations)
