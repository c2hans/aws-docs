---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_UpdateTask.html
---

# UpdateTask
<a name="API_UpdateTask"></a>

Updates the configuration of a *task*, which defines where and how AWS DataSync transfers your data.

## Request Syntax
<a name="API_UpdateTask_RequestSyntax"></a>

```
{
   "CloudWatchLogGroupArn": "{{string}}",
   "Excludes": [
      {
         "FilterType": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Includes": [
      {
         "FilterType": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "ManifestConfig": {
      "Action": "{{string}}",
      "Format": "{{string}}",
      "Source": {
         "S3": {
            "BucketAccessRoleArn": "{{string}}",
            "ManifestObjectPath": "{{string}}",
            "ManifestObjectVersionId": "{{string}}",
            "S3BucketArn": "{{string}}"
         }
      }
   },
   "Name": "{{string}}",
   "Options": {
      "Atime": "{{string}}",
      "BytesPerSecond": {{number}},
      "Gid": "{{string}}",
      "LogLevel": "{{string}}",
      "Mtime": "{{string}}",
      "ObjectTags": "{{string}}",
      "OverwriteMode": "{{string}}",
      "PosixPermissions": "{{string}}",
      "PreserveDeletedFiles": "{{string}}",
      "PreserveDevices": "{{string}}",
      "SecurityDescriptorCopyFlags": "{{string}}",
      "TaskQueueing": "{{string}}",
      "TransferMode": "{{string}}",
      "Uid": "{{string}}",
      "VerifyMode": "{{string}}"
   },
   "Schedule": {
      "ScheduleExpression": "{{string}}",
      "Status": "{{string}}"
   },
   "TaskArn": "{{string}}",
   "TaskReportConfig": {
      "Destination": {
         "S3": {
            "BucketAccessRoleArn": "{{string}}",
            "S3BucketArn": "{{string}}",
            "Subdirectory": "{{string}}"
         }
      },
      "ObjectVersionIds": "{{string}}",
      "OutputType": "{{string}}",
      "Overrides": {
         "Deleted": {
            "ReportLevel": "{{string}}"
         },
         "Skipped": {
            "ReportLevel": "{{string}}"
         },
         "Transferred": {
            "ReportLevel": "{{string}}"
         },
         "Verified": {
            "ReportLevel": "{{string}}"
         }
      },
      "ReportLevel": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CloudWatchLogGroupArn](#API_UpdateTask_RequestSyntax) **   <a name="DataSync-UpdateTask-request-CloudWatchLogGroupArn"></a>
Specifies the Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task.
For Enhanced mode tasks, you must use `/aws/datasync` as your log group name. For example:
 `arn:aws:logs:us-east-1:111222333444:log-group:/aws/datasync:*`
For more information, see [Monitoring data transfers with CloudWatch Logs](https://docs.aws.amazon.com/datasync/latest/userguide/configure-logging.html).
Type: String
Length Constraints: Maximum length of 562.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):logs:[a-z\-0-9]+:[0-9]{12}:log-group:([^:\*]*)(:\*)?$`
Required: No

 ** [Excludes](#API_UpdateTask_RequestSyntax) **   <a name="DataSync-UpdateTask-request-Excludes"></a>
Specifies exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer. For more information and examples, see [Specifying what DataSync transfers by using filters](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html).
Type: Array of [FilterRule](API_FilterRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [Includes](#API_UpdateTask_RequestSyntax) **   <a name="DataSync-UpdateTask-request-Includes"></a>
Specifies include filters define the files, objects, and folders in your source location that you want DataSync to transfer. For more information and examples, see [Specifying what DataSync transfers by using filters](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html).
Type: Array of [FilterRule](API_FilterRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [ManifestConfig](#API_UpdateTask_RequestSyntax) **   <a name="DataSync-UpdateTask-request-ManifestConfig"></a>
Configures a manifest, which is a list of files or objects that you want DataSync to transfer. For more information and configuration examples, see [Specifying what DataSync transfers by using a manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html).
When using this parameter, your caller identity (the IAM role that you're using DataSync with) must have the `iam:PassRole` permission. The [AWSDataSyncFullAccess](https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess) policy includes this permission.
To remove a manifest configuration, specify this parameter as empty.
Type: [ManifestConfig](API_ManifestConfig.md) object
Required: No

 ** [Name](#API_UpdateTask_RequestSyntax) **   <a name="DataSync-UpdateTask-request-Name"></a>
Specifies the name of your task.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9\s+=._:@/-]+$`
Required: No

 ** [Options](#API_UpdateTask_RequestSyntax) **   <a name="DataSync-UpdateTask-request-Options"></a>
Indicates how your transfer task is configured. These options include how DataSync handles files, objects, and their associated metadata during your transfer. You also can specify how to verify data integrity, set bandwidth limits for your task, among other options.
Each option has a default value. Unless you need to, you don't have to configure any option before calling [StartTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_StartTaskExecution.html).
You also can override your task options for each task execution. For example, you might want to adjust the `LogLevel` for an individual execution.
Type: [Options](API_Options.md) object
Required: No

 ** [Schedule](#API_UpdateTask_RequestSyntax) **   <a name="DataSync-UpdateTask-request-Schedule"></a>
Specifies a schedule for when you want your task to run. For more information, see [Scheduling your task](https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html).
Type: [TaskSchedule](API_TaskSchedule.md) object
Required: No

 ** [TaskArn](#API_UpdateTask_RequestSyntax) **   <a name="DataSync-UpdateTask-request-TaskArn"></a>
Specifies the ARN of the task that you want to update.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}$`
Required: Yes

 ** [TaskReportConfig](#API_UpdateTask_RequestSyntax) **   <a name="DataSync-UpdateTask-request-TaskReportConfig"></a>
Specifies how you want to configure a task report, which provides detailed information about your DataSync transfer. For more information, see [Monitoring your DataSync transfers with task reports](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html).
When using this parameter, your caller identity (the IAM role that you're using DataSync with) must have the `iam:PassRole` permission. The [AWSDataSyncFullAccess](https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess) policy includes this permission.
To remove a task report configuration, specify this parameter as empty.
Type: [TaskReportConfig](API_TaskReportConfig.md) object
Required: No

## Response Elements
<a name="API_UpdateTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/UpdateTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/UpdateTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/UpdateTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/UpdateTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/UpdateTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/UpdateTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/UpdateTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/UpdateTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/UpdateTask)
