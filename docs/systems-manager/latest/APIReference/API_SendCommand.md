---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SendCommand.html
---

# SendCommand
<a name="API_SendCommand"></a>

Runs commands on one or more managed nodes.

## Request Syntax
<a name="API_SendCommand_RequestSyntax"></a>

```
{
   "AlarmConfiguration": {
      "Alarms": [
         {
            "Name": "{{string}}"
         }
      ],
      "IgnorePollAlarmFailure": {{boolean}}
   },
   "CloudWatchOutputConfig": {
      "CloudWatchLogGroupName": "{{string}}",
      "CloudWatchOutputEnabled": {{boolean}}
   },
   "Comment": "{{string}}",
   "DocumentHash": "{{string}}",
   "DocumentHashType": "{{string}}",
   "DocumentName": "{{string}}",
   "DocumentVersion": "{{string}}",
   "InstanceIds": [ "{{string}}" ],
   "MaxConcurrency": "{{string}}",
   "MaxErrors": "{{string}}",
   "NotificationConfig": {
      "NotificationArn": "{{string}}",
      "NotificationEvents": [ "{{string}}" ],
      "NotificationType": "{{string}}"
   },
   "OutputS3BucketName": "{{string}}",
   "OutputS3KeyPrefix": "{{string}}",
   "OutputS3Region": "{{string}}",
   "Parameters": {
      "{{string}}" : [ "{{string}}" ]
   },
   "ServiceRoleArn": "{{string}}",
   "Targets": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "TimeoutSeconds": {{number}}
}
```

## Request Parameters
<a name="API_SendCommand_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AlarmConfiguration](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-AlarmConfiguration"></a>
The CloudWatch alarm you want to apply to your command.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** [CloudWatchOutputConfig](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-CloudWatchOutputConfig"></a>
Enables AWS Systems Manager to send Run Command output to Amazon CloudWatch Logs. Run Command is a tool in AWS Systems Manager.
Type: [CloudWatchOutputConfig](API_CloudWatchOutputConfig.md) object
Required: No

 ** [Comment](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-Comment"></a>
User-specified information about the command, such as a brief description of what the command should do.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [DocumentHash](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-DocumentHash"></a>
The Sha256 or Sha1 hash created by the system when the document was created.
Sha1 hashes have been deprecated.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [DocumentHashType](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-DocumentHashType"></a>
Sha256 or Sha1.
Sha1 hashes have been deprecated.
Type: String
Valid Values: `Sha256 | Sha1`
Required: No

 ** [DocumentName](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-DocumentName"></a>
The name of the AWS Systems Manager document (SSM document) to run. This can be a public document or a custom document. To run a shared document belonging to another account, specify the document Amazon Resource Name (ARN). For more information about how to use shared documents, see [Sharing SSM documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-using-shared.html) in the * AWS Systems Manager User Guide*.
If you specify a document name or ARN that hasn't been shared with your account, you receive an `InvalidDocument` error.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: Yes

 ** [DocumentVersion](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-DocumentVersion"></a>
The SSM document version to use in the request. You can specify $DEFAULT, $LATEST, or a specific version number. If you run commands by using the AWS Command Line Interface (AWS CLI), then you must escape the first two options by using a backslash. If you specify a version number, then you don't need to use the backslash. For example:
--document-version "\\$DEFAULT"
--document-version "\\$LATEST"
--document-version "3"
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** [InstanceIds](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-InstanceIds"></a>
The IDs of the managed nodes where the command should run. Specifying managed node IDs is most useful when you are targeting a limited number of managed nodes, though you can specify up to 50 IDs.
To target a larger number of managed nodes, or if you prefer not to list individual node IDs, we recommend using the `Targets` option instead. Using `Targets`, which accepts tag key-value pairs to identify the managed nodes to send commands to, you can a send command to tens, hundreds, or thousands of nodes at once.
For more information about how to use targets, see [Run commands at scale](https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html) in the * AWS Systems Manager User Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

 ** [MaxConcurrency](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-MaxConcurrency"></a>
(Optional) The maximum number of managed nodes that are allowed to run the command at the same time. You can specify a number such as 10 or a percentage such as 10%. The default value is `50`. For more information about how to use `MaxConcurrency`, see [Using concurrency controls](https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-velocity) in the * AWS Systems Manager User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`
Required: No

 ** [MaxErrors](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-MaxErrors"></a>
The maximum number of errors allowed without the command failing. When the command fails one more time beyond the value of `MaxErrors`, the systems stops sending the command to additional targets. You can specify a number like 10 or a percentage like 10%. The default value is `0`. For more information about how to use `MaxErrors`, see [Using error controls](https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-maxerrors) in the * AWS Systems Manager User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`
Required: No

 ** [NotificationConfig](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-NotificationConfig"></a>
Configurations for sending notifications.
Type: [NotificationConfig](API_NotificationConfig.md) object
Required: No

 ** [OutputS3BucketName](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-OutputS3BucketName"></a>
The name of the S3 bucket where command execution responses should be stored.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

 ** [OutputS3KeyPrefix](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-OutputS3KeyPrefix"></a>
The directory structure within the S3 bucket where the responses should be stored.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [OutputS3Region](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-OutputS3Region"></a>
(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the AWS Region of the S3 bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 20.
Required: No

 ** [Parameters](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-Parameters"></a>
The required and optional parameters specified in the document being run.
Type: String to array of strings map
Required: No

 ** [ServiceRoleArn](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-ServiceRoleArn"></a>
The ARN of the AWS Identity and Access Management (IAM) service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for Run Command commands.
This role must provide the `sns:Publish` permission for your notification topic. For information about creating and using this service role, see [Monitoring Systems Manager status changes using Amazon SNS notifications](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-notifications.html) in the * AWS Systems Manager User Guide*.
Type: String
Required: No

 ** [Targets](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-Targets"></a>
An array of search criteria that targets managed nodes using a `Key,Value` combination that you specify. Specifying targets is most useful when you want to send a command to a large number of managed nodes at once. Using `Targets`, which accepts tag key-value pairs to identify managed nodes, you can send a command to tens, hundreds, or thousands of nodes at once.
To send a command to a smaller number of managed nodes, you can use the `InstanceIds` option instead.
For more information about how to use targets, see [Run commands at scale](https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html) in the * AWS Systems Manager User Guide*.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [TimeoutSeconds](#API_SendCommand_RequestSyntax) **   <a name="systemsmanager-SendCommand-request-TimeoutSeconds"></a>
If this time is reached and the command hasn't already started running, it won't run.
Type: Integer
Valid Range: Minimum value of 30. Maximum value of 2592000.
Required: No

## Response Syntax
<a name="API_SendCommand_ResponseSyntax"></a>

```
{
   "Command": {
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
}
```

## Response Elements
<a name="API_SendCommand_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Command](#API_SendCommand_ResponseSyntax) **   <a name="systemsmanager-SendCommand-response-Command"></a>
The request as it was received by Systems Manager. Also provides the command ID which can be used future references to this request.
Type: [Command](API_Command.md) object

## Errors
<a name="API_SendCommand_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateInstanceId **
You can't specify a managed node ID in more than one association.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** InvalidDocumentVersion **
The document version isn't valid or doesn't exist.
HTTP Status Code: 400

 ** InvalidInstanceId **
The following problems can cause this exception:
+ You don't have permission to access the managed node.
+  AWS Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.
+ SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.
+ The managed node isn't in a valid state. Valid states are: `Running`, `Pending`, `Stopped`, and `Stopping`. Invalid states are: `Shutting-down` and `Terminated`.
HTTP Status Code: 400

 ** InvalidNotificationConfig **
One or more configuration items isn't valid. Verify that a valid Amazon Resource Name (ARN) was provided for an Amazon Simple Notification Service topic.
HTTP Status Code: 400

 ** InvalidOutputFolder **
The S3 bucket doesn't exist.
HTTP Status Code: 400

 ** InvalidParameters **
You must specify values for all required parameters in the AWS Systems Manager document (SSM document). You can only supply values to parameters defined in the SSM document.
HTTP Status Code: 400

 ** InvalidRole **
The role name can't contain invalid characters. Also verify that you specified an IAM role for notifications that includes the required trust policy. For information about configuring the IAM role for Run Command notifications, see [Monitoring Systems Manager status changes using Amazon SNS notifications](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-notifications.html) in the * AWS Systems Manager User Guide*.
HTTP Status Code: 400

 ** MaxDocumentSizeExceeded **
The size limit of a document is 64 KB.
HTTP Status Code: 400

 ** UnsupportedPlatformType **
The document doesn't support the platform type of the given managed node IDs. For example, you sent an document for a Windows managed node to a Linux node.
HTTP Status Code: 400

## Examples
<a name="API_SendCommand_Examples"></a>

### Example
<a name="API_SendCommand_Example_1"></a>

This example illustrates one usage of SendCommand.

#### Sample Request
<a name="API_SendCommand_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.SendCommand
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240221T000322Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240221/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 153

{
    "CloudWatchOutputConfig": {
        "CloudWatchLogGroupName": "my-log-group",
        "CloudWatchOutputEnabled": true
    },
    "DocumentName": "AWS-ConfigureCloudWatch",
    "DocumentVersion": "1",
    "InstanceIds": [
        "i-07be1baa4aEXAMPLE",
        "i-017431b35cEXAMPLE",
        "i-09c350ed76EXAMPLE"
    ],
    "MaxConcurrency": "2",
    "MaxErrors": "1",
    "NotificationConfig": {
        "NotificationArn": "arn:aws:sns:us-east-2:111122223333:my-us-east-2-notification-arn",
        "NotificationEvents": [
            "Failed",
            "Success"
        ],
        "NotificationType": "Command"
    },
    "OutputS3BucketName": "amzn-s3-demo-bucket",
    "OutputS3KeyPrefix": "my-prefix",
    "OutputS3Region": "us-east-2",
    "Parameters": {
        "string": []
    },
    "TimeoutSeconds": 30
}
```

#### Sample Response
<a name="API_SendCommand_Example_1_Response"></a>

```
{
    "Command": {
        "CommandId": "b94bf1dc-fe7d-4e88-851d-e85e5EXAMPLE",
        "DocumentName": "AWS-ConfigureCloudWatch",
        "DocumentVersion": "1",
        "Comment": "",
        "ExpiresAfter": 1582250177.7,
        "Parameters": {
            "properties": [
                ""
            ],
            "status": [
                "Enabled"
            ]
        },
        "InstanceIds": [],
        "Targets": [
            {
                "Key": "InstanceIds",
                "Values": [
                    "i-07be1baa4aEXAMPLE",
                    "i-017431b35cEXAMPLE",
                    "i-09c350ed76EXAMPLE"
                ]
            }
        ],
        "RequestedDateTime": 1582245977.7,
        "Status": "Pending",
        "StatusDetails": "Pending",
        "OutputS3BucketName": "amzn-s3-demo-bucket",
        "OutputS3KeyPrefix": "my-prefix",
        "MaxConcurrency": "2",
        "MaxErrors": "1",
        "TargetCount": 0,
        "CompletedCount": 0,
        "ErrorCount": 0,
        "DeliveryTimedOutCount": 0,
        "ServiceRole": "arn:aws:iam::111122223333:role/my-SNS-notifications-role",
        "NotificationConfig": {
            "NotificationArn": "arn:aws:sns:us-east-2:111122223333:my-us-east-2-notification-arn",
            "NotificationEvents": [
                "Failed",
                "Success"
            ],
            "NotificationType": "Command"
        },
        "CloudWatchOutputConfig": {
            "CloudWatchLogGroupName": "my-log-group",
            "CloudWatchOutputEnabled": true
        }
    }
}
```

## See Also
<a name="API_SendCommand_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/SendCommand)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/SendCommand)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/SendCommand)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/SendCommand)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/SendCommand)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/SendCommand)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/SendCommand)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/SendCommand)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/SendCommand)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/SendCommand)
