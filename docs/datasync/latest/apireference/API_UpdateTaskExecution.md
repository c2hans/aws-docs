---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_UpdateTaskExecution.html
---

# UpdateTaskExecution
<a name="API_UpdateTaskExecution"></a>

Updates the configuration of a running AWS DataSync task execution.

**Note**
Currently, the only `Option` that you can modify with `UpdateTaskExecution` is ` [BytesPerSecond](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-BytesPerSecond) `, which throttles bandwidth for a running or queued task execution.

## Request Syntax
<a name="API_UpdateTaskExecution_RequestSyntax"></a>

```
{
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
   "TaskExecutionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateTaskExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Options](#API_UpdateTaskExecution_RequestSyntax) **   <a name="DataSync-UpdateTaskExecution-request-Options"></a>
Indicates how your transfer task is configured. These options include how DataSync handles files, objects, and their associated metadata during your transfer. You also can specify how to verify data integrity, set bandwidth limits for your task, among other options.
Each option has a default value. Unless you need to, you don't have to configure any option before calling [StartTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_StartTaskExecution.html).
You also can override your task options for each task execution. For example, you might want to adjust the `LogLevel` for an individual execution.
Type: [Options](API_Options.md) object
Required: Yes

 ** [TaskExecutionArn](#API_UpdateTaskExecution_RequestSyntax) **   <a name="DataSync-UpdateTaskExecution-request-TaskExecutionArn"></a>
Specifies the Amazon Resource Name (ARN) of the task execution that you're updating.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}/execution/exec-[0-9a-f]{17}$`
Required: Yes

## Response Elements
<a name="API_UpdateTaskExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateTaskExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTaskExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/UpdateTaskExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/UpdateTaskExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/UpdateTaskExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/UpdateTaskExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/UpdateTaskExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateTaskExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/UpdateTaskExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/UpdateTaskExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/UpdateTaskExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/UpdateTaskExecution)
