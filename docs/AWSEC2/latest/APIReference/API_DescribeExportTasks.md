---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeExportTasks.html
---

# DescribeExportTasks
<a name="API_DescribeExportTasks"></a>

Describes the specified export instance tasks or all of your export instance tasks.

## Request Parameters
<a name="API_DescribeExportTasks_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ExportTaskId.N**
The export task IDs.
Type: Array of strings
Required: No

 **Filter.N**
the filters for the export tasks.
Type: Array of [Filter](API_Filter.md) objects
Required: No

## Response Elements
<a name="API_DescribeExportTasks_ResponseElements"></a>

The following elements are returned by the service.

 **exportTaskSet**
Information about the export tasks.
Type: Array of [ExportTask](API_ExportTask.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeExportTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeExportTasks_Examples"></a>

### Example
<a name="API_DescribeExportTasks_Example_1"></a>

This example describes a single export task.

#### Sample Request
<a name="API_DescribeExportTasks_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeExportTasks
&exportTaskId.1=export-i-1234wxyz
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeExportTasks_Example_1_Response"></a>

```
<DescribeExportTasksResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
<requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
<exportTaskSet>
  <item>
    <exportTaskId>export-i-1234wxyz</exportTaskId>
    <description>Example for docs</description>
    <state>active</state>
    <statusMessage>Running</statusMessage>
    <instanceExport>
      <instanceId>i-12345678</instanceId>
      <targetEnvironment>VMWare</targetEnvironment>
    </instanceExport>
    <exportToS3>
      <diskImageFormat>VMDK</diskImageFormat>
      <containerFormat>OVA</containerFormat>
      <s3Bucket>amzn-s3-demo-for-exported-vm</s3Bucket>
      <s3Key>my-exports/ export-i-1234wxyz.ova</s3Key>
    </exportToS3>
  </item>
</exportTaskSet>
</DescribeExportTasksResponse>
```

## See Also
<a name="API_DescribeExportTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeExportTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeExportTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeExportTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeExportTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeExportTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeExportTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeExportTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeExportTasks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeExportTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeExportTasks)
