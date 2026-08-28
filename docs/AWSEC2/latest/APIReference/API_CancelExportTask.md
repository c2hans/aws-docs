---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelExportTask.html
---

# CancelExportTask
<a name="API_CancelExportTask"></a>

Cancels an active export task. The request removes all artifacts of the export, including any partially-created Amazon S3 objects. If the export task is complete or is in the process of transferring the final disk image, the command fails and returns an error.

## Request Parameters
<a name="API_CancelExportTask_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ExportTaskId**
The ID of the export task. This is the ID returned by the `CreateInstanceExportTask` and `ExportImage` operations.
Type: String
Required: Yes

## Response Elements
<a name="API_CancelExportTask_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_CancelExportTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CancelExportTask_Examples"></a>

### Example
<a name="API_CancelExportTask_Example_1"></a>

This example request cancels the export task with the ID `export-i-1234wxyz`.

#### Sample Request
<a name="API_CancelExportTask_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CancelExportTask
&exportTaskId=export-i-1234wxyz
&AUTHPARAMS
```

#### Sample Response
<a name="API_CancelExportTask_Example_1_Response"></a>

```
<CancelExportTask xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
<requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
<return>true</return>
</CancelExportTask>
```

## See Also
<a name="API_CancelExportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CancelExportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CancelExportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CancelExportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CancelExportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CancelExportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CancelExportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CancelExportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CancelExportTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CancelExportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CancelExportTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
