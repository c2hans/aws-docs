---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_DescribeTask.html
---

# DescribeTask
<a name="API_DescribeTask"></a>

Provides information about a *task*, which defines where and how AWS DataSync transfers your data.

## Request Syntax
<a name="API_DescribeTask_RequestSyntax"></a>

```
{
   "TaskArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TaskArn](#API_DescribeTask_RequestSyntax) **   <a name="DataSync-DescribeTask-request-TaskArn"></a>
Specifies the Amazon Resource Name (ARN) of the transfer task that you want information about.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}$`
Required: Yes

## Response Syntax
<a name="API_DescribeTask_ResponseSyntax"></a>

```
{
   "CloudWatchLogGroupArn": "string",
   "CreationTime": number,
   "CurrentTaskExecutionArn": "string",
   "DestinationLocationArn": "string",
   "DestinationNetworkInterfaceArns": [ "string" ],
   "ErrorCode": "string",
   "ErrorDetail": "string",
   "Excludes": [
      {
         "FilterType": "string",
         "Value": "string"
      }
   ],
   "Includes": [
      {
         "FilterType": "string",
         "Value": "string"
      }
   ],
   "ManifestConfig": {
      "Action": "string",
      "Format": "string",
      "Source": {
         "S3": {
            "BucketAccessRoleArn": "string",
            "ManifestObjectPath": "string",
            "ManifestObjectVersionId": "string",
            "S3BucketArn": "string"
         }
      }
   },
   "Name": "string",
   "Options": {
      "Atime": "string",
      "BytesPerSecond": number,
      "Gid": "string",
      "LogLevel": "string",
      "Mtime": "string",
      "ObjectTags": "string",
      "OverwriteMode": "string",
      "PosixPermissions": "string",
      "PreserveDeletedFiles": "string",
      "PreserveDevices": "string",
      "SecurityDescriptorCopyFlags": "string",
      "TaskQueueing": "string",
      "TransferMode": "string",
      "Uid": "string",
      "VerifyMode": "string"
   },
   "Schedule": {
      "ScheduleExpression": "string",
      "Status": "string"
   },
   "ScheduleDetails": {
      "DisabledBy": "string",
      "DisabledReason": "string",
      "StatusUpdateTime": number
   },
   "SourceLocationArn": "string",
   "SourceNetworkInterfaceArns": [ "string" ],
   "Status": "string",
   "TaskArn": "string",
   "TaskMode": "string",
   "TaskReportConfig": {
      "Destination": {
         "S3": {
            "BucketAccessRoleArn": "string",
            "S3BucketArn": "string",
            "Subdirectory": "string"
         }
      },
      "ObjectVersionIds": "string",
      "OutputType": "string",
      "Overrides": {
         "Deleted": {
            "ReportLevel": "string"
         },
         "Skipped": {
            "ReportLevel": "string"
         },
         "Transferred": {
            "ReportLevel": "string"
         },
         "Verified": {
            "ReportLevel": "string"
         }
      },
      "ReportLevel": "string"
   }
}
```

## Response Elements
<a name="API_DescribeTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CloudWatchLogGroupArn](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-CloudWatchLogGroupArn"></a>
The Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task.
For more information, see [Monitoring data transfers with CloudWatch Logs](https://docs.aws.amazon.com/datasync/latest/userguide/configure-logging.html).
Type: String
Length Constraints: Maximum length of 562.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):logs:[a-z\-0-9]+:[0-9]{12}:log-group:([^:\*]*)(:\*)?$`

 ** [CreationTime](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-CreationTime"></a>
The time that the task was created.
Type: Timestamp

 ** [CurrentTaskExecutionArn](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-CurrentTaskExecutionArn"></a>
The ARN of the most recent task execution.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}/execution/exec-[0-9a-f]{17}$`

 ** [DestinationLocationArn](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-DestinationLocationArn"></a>
The ARN of your transfer's destination location.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

 ** [DestinationNetworkInterfaceArns](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-DestinationNetworkInterfaceArns"></a>
The ARNs of the [network interfaces](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html#required-network-interfaces) that DataSync created for your destination location.
Type: Array of strings
Length Constraints: Maximum length of 128.
Pattern: `^arn:aws[\-a-z]{0,}:ec2:[a-z\-0-9]*:[0-9]{12}:network-interface/eni-[0-9a-f]+$`

 ** [ErrorCode](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-ErrorCode"></a>
If there's an issue with your task, you can use the error code to help you troubleshoot the problem. For more information, see [Troubleshooting issues with DataSync transfers](https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html).
Type: String

 ** [ErrorDetail](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-ErrorDetail"></a>
If there's an issue with your task, you can use the error details to help you troubleshoot the problem. For more information, see [Troubleshooting issues with DataSync transfers](https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html).
Type: String

 ** [Excludes](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-Excludes"></a>
The exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer. For more information and examples, see [Specifying what DataSync transfers by using filters](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html).
Type: Array of [FilterRule](API_FilterRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [Includes](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-Includes"></a>
The include filters that define the files, objects, and folders in your source location that you want DataSync to transfer. For more information and examples, see [Specifying what DataSync transfers by using filters](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html).
Type: Array of [FilterRule](API_FilterRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [ManifestConfig](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-ManifestConfig"></a>
The configuration of the manifest that lists the files or objects that you want DataSync to transfer. For more information, see [Specifying what DataSync transfers by using a manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html).
Type: [ManifestConfig](API_ManifestConfig.md) object

 ** [Name](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-Name"></a>
The name of your task.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9\s+=._:@/-]+$`

 ** [Options](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-Options"></a>
The task's settings. For example, what file metadata gets preserved, how data integrity gets verified at the end of your transfer, bandwidth limits, among other options.
Type: [Options](API_Options.md) object

 ** [Schedule](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-Schedule"></a>
The schedule for when you want your task to run. For more information, see [Scheduling your task](https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html).
Type: [TaskSchedule](API_TaskSchedule.md) object

 ** [ScheduleDetails](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-ScheduleDetails"></a>
The details about your [task schedule](https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html).
Type: [TaskScheduleDetails](API_TaskScheduleDetails.md) object

 ** [SourceLocationArn](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-SourceLocationArn"></a>
The ARN of your transfer's source location.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

 ** [SourceNetworkInterfaceArns](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-SourceNetworkInterfaceArns"></a>
The ARNs of the [network interfaces](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html#required-network-interfaces) that DataSync created for your source location.
Type: Array of strings
Length Constraints: Maximum length of 128.
Pattern: `^arn:aws[\-a-z]{0,}:ec2:[a-z\-0-9]*:[0-9]{12}:network-interface/eni-[0-9a-f]+$`

 ** [Status](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-Status"></a>
The status of your task. For information about what each status means, see [Task statuses](https://docs.aws.amazon.com/datasync/latest/userguide/create-task-how-to.html#understand-task-creation-statuses).
Type: String
Valid Values: `AVAILABLE | CREATING | QUEUED | RUNNING | UNAVAILABLE`

 ** [TaskArn](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-TaskArn"></a>
The ARN of your task.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}$`

 ** [TaskMode](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-TaskMode"></a>
The task mode that you're using. For more information, see [Choosing a task mode for your data transfer](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html).
Type: String
Valid Values: `BASIC | ENHANCED`

 ** [TaskReportConfig](#API_DescribeTask_ResponseSyntax) **   <a name="DataSync-DescribeTask-response-TaskReportConfig"></a>
The configuration of your task report, which provides detailed information about your DataSync transfer. For more information, see [Monitoring your DataSync transfers with task reports](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html).
Type: [TaskReportConfig](API_TaskReportConfig.md) object

## Errors
<a name="API_DescribeTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## Examples
<a name="API_DescribeTask_Examples"></a>

### Sample Request
<a name="API_DescribeTask_Example_1"></a>

The following example specifies the ARN of a DataSync task to get information about.

```
{
  "TaskArn": "arn:aws:datasync:us-east-2:111222333444:task/task-08de6e6697796f026"
}
```

### Sample Response
<a name="API_DescribeTask_Example_2"></a>

The following example shows a `DescribeTask` response.

```
{
  "TaskArn": "arn:aws:datasync:us-east-2:111222333444:task/task-08de6e6697796f026",
  "Name": "MyTask",
  "TaskMode": "BASIC",
  "Status": "RUNNING",
  "SourceLocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-1111aaaa2222bbbb3",
  "DestinationLocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-0000zzzz1111yyyy2",
  "CurrentTaskExecutionArn": "arn:aws:datasync:us-east-2:111222333444:task/task-08de6e6697796f026/execution/exec-04ce9d516d69bd52f",
  "CreationTime": 1532660733.39,
  "Options": {
    "Atime": "BEST_EFFORT",
    "BytesPerSecond": 1000,
    "Gid": "NONE",
    "Mtime": "PRESERVE",
    "PosixPermissions": "PRESERVE",
    "PreserveDevices": "NONE",
    "PreserveDeletedFiles": "PRESERVE",
    "Uid": "NONE",
    "VerifyMode": "POINT_IN_TIME_CONSISTENT"
  },
  "CloudWatchLogGroupArn": "arn:aws:logs:us-east-2:111222333444:log-group:/log-group-name:*"
}
```

## See Also
<a name="API_DescribeTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/DescribeTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/DescribeTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/DescribeTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/DescribeTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/DescribeTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/DescribeTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/DescribeTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/DescribeTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/DescribeTask)
