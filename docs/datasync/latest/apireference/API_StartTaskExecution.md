---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_StartTaskExecution.html
---

# StartTaskExecution
<a name="API_StartTaskExecution"></a>

Starts an AWS DataSync transfer task. For each task, you can only run one task execution at a time.

There are several steps to a task execution. For more information, see [Task execution statuses](https://docs.aws.amazon.com/datasync/latest/userguide/working-with-task-executions.html#understand-task-execution-statuses).

**Important**
If you're planning to transfer data to or from an Amazon S3 location, review [how DataSync can affect your S3 request charges](https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-s3-requests) and the [DataSync pricing page](http://aws.amazon.com/datasync/pricing/) before you begin.

## Request Syntax
<a name="API_StartTaskExecution_RequestSyntax"></a>

```
{
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
   "OverrideOptions": {
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
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
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
<a name="API_StartTaskExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Excludes](#API_StartTaskExecution_RequestSyntax) **   <a name="DataSync-StartTaskExecution-request-Excludes"></a>
Specifies a list of filter rules that determines which files to exclude from a task. The list contains a single filter string that consists of the patterns to exclude. The patterns are delimited by "\|" (that is, a pipe), for example, `"/folder1|/folder2"`.
Type: Array of [FilterRule](API_FilterRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [Includes](#API_StartTaskExecution_RequestSyntax) **   <a name="DataSync-StartTaskExecution-request-Includes"></a>
Specifies a list of filter rules that determines which files to include when running a task. The pattern should contain a single filter string that consists of the patterns to include. The patterns are delimited by "\|" (that is, a pipe), for example, `"/folder1|/folder2"`.
Type: Array of [FilterRule](API_FilterRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [ManifestConfig](#API_StartTaskExecution_RequestSyntax) **   <a name="DataSync-StartTaskExecution-request-ManifestConfig"></a>
Configures a manifest, which is a list of files or objects that you want DataSync to transfer. For more information and configuration examples, see [Specifying what DataSync transfers by using a manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html).
When using this parameter, your caller identity (the role that you're using DataSync with) must have the `iam:PassRole` permission. The [AWSDataSyncFullAccess](https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess) policy includes this permission.
To remove a manifest configuration, specify this parameter with an empty value.
Type: [ManifestConfig](API_ManifestConfig.md) object
Required: No

 ** [OverrideOptions](#API_StartTaskExecution_RequestSyntax) **   <a name="DataSync-StartTaskExecution-request-OverrideOptions"></a>
Indicates how your transfer task is configured. These options include how DataSync handles files, objects, and their associated metadata during your transfer. You also can specify how to verify data integrity, set bandwidth limits for your task, among other options.
Each option has a default value. Unless you need to, you don't have to configure any option before calling [StartTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_StartTaskExecution.html).
You also can override your task options for each task execution. For example, you might want to adjust the `LogLevel` for an individual execution.
Type: [Options](API_Options.md) object
Required: No

 ** [Tags](#API_StartTaskExecution_RequestSyntax) **   <a name="DataSync-StartTaskExecution-request-Tags"></a>
Specifies the tags that you want to apply to the Amazon Resource Name (ARN) representing the task execution.
 *Tags* are key-value pairs that help you manage, filter, and search for your DataSync resources.
Type: Array of [TagListEntry](API_TagListEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TaskArn](#API_StartTaskExecution_RequestSyntax) **   <a name="DataSync-StartTaskExecution-request-TaskArn"></a>
Specifies the Amazon Resource Name (ARN) of the task that you want to start.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}$`
Required: Yes

 ** [TaskReportConfig](#API_StartTaskExecution_RequestSyntax) **   <a name="DataSync-StartTaskExecution-request-TaskReportConfig"></a>
Specifies how you want to configure a task report, which provides detailed information about your DataSync transfer. For more information, see [Monitoring your DataSync transfers with task reports](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html).
When using this parameter, your caller identity (the role that you're using DataSync with) must have the `iam:PassRole` permission. The [AWSDataSyncFullAccess](https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess) policy includes this permission.
To remove a task report configuration, specify this parameter as empty.
Type: [TaskReportConfig](API_TaskReportConfig.md) object
Required: No

## Response Syntax
<a name="API_StartTaskExecution_ResponseSyntax"></a>

```
{
   "TaskExecutionArn": "string"
}
```

## Response Elements
<a name="API_StartTaskExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TaskExecutionArn](#API_StartTaskExecution_ResponseSyntax) **   <a name="DataSync-StartTaskExecution-response-TaskExecutionArn"></a>
The ARN of the running task execution.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}/execution/exec-[0-9a-f]{17}$`

## Errors
<a name="API_StartTaskExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## Examples
<a name="API_StartTaskExecution_Examples"></a>

### Sample Request
<a name="API_StartTaskExecution_Example_1"></a>

The following example starts a task execution using the default options for the specified task.

```
{
    "OverrideOptions": {
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
    "TaskArn": "arn:aws:datasync:us-east-2:111222333444:task/task-08de6e6697796f026"
}
```

### Sample Response
<a name="API_StartTaskExecution_Example_2"></a>

This example illustrates one usage of StartTaskExecution.

```
{
  "TaskExecutionArn": "arn:aws:datasync:us-east-2:111222333444:task/task-08de6e6697796f026/execution/exec-04ce9d516d69bd52f"
}
```

## See Also
<a name="API_StartTaskExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/StartTaskExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/StartTaskExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/StartTaskExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/StartTaskExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/StartTaskExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/StartTaskExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/StartTaskExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/StartTaskExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/StartTaskExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/StartTaskExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
