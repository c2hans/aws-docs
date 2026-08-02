---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_DeleteTask.html
---

# DeleteTask
<a name="API_DeleteTask"></a>

Deletes a transfer task resource from AWS DataSync.

## Request Syntax
<a name="API_DeleteTask_RequestSyntax"></a>

```
{
   "TaskArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TaskArn](#API_DeleteTask_RequestSyntax) **   <a name="DataSync-DeleteTask-request-TaskArn"></a>
Specifies the Amazon Resource Name (ARN) of the task that you want to delete.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}$`
Required: Yes

## Response Elements
<a name="API_DeleteTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_DeleteTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/DeleteTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/DeleteTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/DeleteTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/DeleteTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/DeleteTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/DeleteTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/DeleteTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/DeleteTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/DeleteTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/DeleteTask)
