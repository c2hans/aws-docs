---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListCommands.html
---

# ListCommands
<a name="API_ListCommands"></a>

Lists the commands requested by users of the AWS account.

## Request Syntax
<a name="API_ListCommands_RequestSyntax"></a>

```
{
   "CommandId": "{{string}}",
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
<a name="API_ListCommands_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CommandId](#API_ListCommands_RequestSyntax) **   <a name="systemsmanager-ListCommands-request-CommandId"></a>
(Optional) If provided, lists only the specified command.
Type: String
Length Constraints: Fixed length of 36.
Required: No

 ** [Filters](#API_ListCommands_RequestSyntax) **   <a name="systemsmanager-ListCommands-request-Filters"></a>
(Optional) One or more filters. Use a filter to return a more specific list of results.
Type: Array of [CommandFilter](API_CommandFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [InstanceId](#API_ListCommands_RequestSyntax) **   <a name="systemsmanager-ListCommands-request-InstanceId"></a>
(Optional) Lists commands issued against this managed node ID.
You can't specify a managed node ID in the same command that you specify `Status` = `Pending`. This is because the command hasn't reached the managed node yet.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

 ** [MaxResults](#API_ListCommands_RequestSyntax) **   <a name="systemsmanager-ListCommands-request-MaxResults"></a>
(Optional) The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListCommands_RequestSyntax) **   <a name="systemsmanager-ListCommands-request-NextToken"></a>
(Optional) The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_ListCommands_ResponseSyntax"></a>

```
{
   "Commands": [
      {
         "AlarmConfiguration": {
            "Alarms": [
               {
                  "Name": "string"
               }
            ],
            "IgnorePollAlarmFailure": boolean
         },
         "CloudWatchOutputConfig": {
            "CloudWatchLogGroupName": "string",
            "CloudWatchOutputEnabled": boolean
         },
         "CommandId": "string",
         "Comment": "string",
         "CompletedCount": number,
         "DeliveryTimedOutCount": number,
         "DocumentName": "string",
         "DocumentVersion": "string",
         "ErrorCount": number,
         "ExpiresAfter": number,
         "InstanceIds": [ "string" ],
         "MaxConcurrency": "string",
         "MaxErrors": "string",
         "NotificationConfig": {
            "NotificationArn": "string",
            "NotificationEvents": [ "string" ],
            "NotificationType": "string"
         },
         "OutputS3BucketName": "string",
         "OutputS3KeyPrefix": "string",
         "OutputS3Region": "string",
         "Parameters": {
            "string" : [ "string" ]
         },
         "RequestedDateTime": number,
         "ServiceRole": "string",
         "Status": "string",
         "StatusDetails": "string",
         "TargetCount": number,
         "Targets": [
            {
               "Key": "string",
               "Values": [ "string" ]
            }
         ],
         "TimeoutSeconds": number,
         "TriggeredAlarms": [
            {
               "Name": "string",
               "State": "string"
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCommands_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Commands](#API_ListCommands_ResponseSyntax) **   <a name="systemsmanager-ListCommands-response-Commands"></a>
(Optional) The list of commands requested by the user.
Type: Array of [Command](API_Command.md) objects

 ** [NextToken](#API_ListCommands_ResponseSyntax) **   <a name="systemsmanager-ListCommands-response-NextToken"></a>
(Optional) The token for the next set of items to return. (You received this token from a previous call.)
Type: String

## Errors
<a name="API_ListCommands_Errors"></a>

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
<a name="API_ListCommands_Examples"></a>

### Example
<a name="API_ListCommands_Example_1"></a>

This example illustrates one usage of ListCommands.

#### Sample Request
<a name="API_ListCommands_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListCommands
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240221T002657Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240221/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 53

{
    "CommandId": "088e4813-f292-48b3-8180-d8be9EXAMPLE"
}
```

#### Sample Response
<a name="API_ListCommands_Example_1_Response"></a>

```
{
    "Commands": [
        {
            "CloudWatchOutputConfig": {
                "CloudWatchLogGroupName": "my-log-group",
                "CloudWatchOutputEnabled": true
            },
            "CommandId": "088e4813-f292-48b3-8180-d8be9EXAMPLE",
            "Comment": "",
            "CompletedCount": 0,
            "DeliveryTimedOutCount": 0,
            "DocumentName": "AWS-InstallMissingWindowsUpdates",
            "DocumentVersion": "1",
            "ErrorCount": 0,
            "ExpiresAfter": 1582248743.188,
            "InstanceIds": [],
            "Interactive": false,
            "MaxConcurrency": "2",
            "MaxErrors": "3",
            "NotificationConfig": {
                "NotificationArn": "arn:aws:sns:us-east-2:111122223333:my-us-east-2-notification-arn",
                "NotificationEvents": [
                    "All"
                ],
                "NotificationType": "Command"
            },
            "OutputS3BucketName": "amzn-s3-demo-bucket",
            "OutputS3KeyPrefix": "my-prefix",
            "Parameters": {
                "ExcludeKbArticleIds": [
                    ""
                ],
                "UpdateLevel": [
                    "All"
                ]
            },
            "RequestedDateTime": 1582244543.188,
            "ServiceRole": "arn:aws:iam::111122223333:role/my-SNS-notifications-role",
            "Status": "InProgress",
            "StatusDetails": "InProgress",
            "TargetCount": 5,
            "Targets": [
                {
                    "Key": "InstanceIds",
                    "Values": [
                        "i-09c350ed76EXAMPLE",
                        "i-07be1baa4aEXAMPLE",
                        "i-00ec29b21eEXAMPLE",
                        "i-09911ddd90EXAMPLE",
                        "i-017431b35cEXAMPLE"
                    ]
                }
            ]
        }
    ]
}
```

## See Also
<a name="API_ListCommands_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListCommands)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListCommands)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListCommands)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListCommands)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListCommands)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListCommands)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListCommands)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListCommands)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListCommands)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListCommands)
