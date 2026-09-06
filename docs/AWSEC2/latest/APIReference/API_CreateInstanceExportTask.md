---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateInstanceExportTask.html
---

# CreateInstanceExportTask
<a name="API_CreateInstanceExportTask"></a>

Exports a running or stopped instance to an Amazon S3 bucket.

For information about the prerequisites for your Amazon S3 bucket, supported operating systems, image formats, and known limitations for the types of instances you can export, see [Exporting an instance as a VM Using VM Import/Export](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html) in the *VM Import/Export User Guide*.

## Request Parameters
<a name="API_CreateInstanceExportTask_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Description**
A description for the conversion task or the resource being exported. The maximum length is 255 characters.
Type: String
Required: No

 **ExportToS3**
The format and location for an export instance task.
Type: [ExportToS3TaskSpecification](API_ExportToS3TaskSpecification.md) object
Required: Yes

 **InstanceId**
The ID of the instance.
Type: String
Required: Yes

 **TagSpecification.N**
The tags to apply to the export instance task during creation.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **TargetEnvironment**
The target virtualization environment.
Type: String
Valid Values: `citrix | vmware | microsoft`
Required: Yes

## Response Elements
<a name="API_CreateInstanceExportTask_ResponseElements"></a>

The following elements are returned by the service.

 **exportTask**
Information about the export instance task.
Type: [ExportTask](API_ExportTask.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateInstanceExportTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateInstanceExportTask_Examples"></a>

### Example
<a name="API_CreateInstanceExportTask_Example_1"></a>

This example request creates an Export VM task that makes a Windows instance available as an OVA.

#### Sample Request
<a name="API_CreateInstanceExportTask_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateInstanceExportTask
&Description=Example%20for%20docs
&InstanceId=i-1234567890abcdef0
&TargetEnvironment=VMWare
&ExportToS3.DiskImageFormat=VMDK
&ExportToS3.ContainerFormat=OVA
&ExportToS3.S3bucket=amzn-s3-demo-for-exported-vm
&ExportToS3.S3prefix=my-exports/
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateInstanceExportTask_Example_1_Response"></a>

```
<CreateInstanceExportTaskResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
<requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <exportTask>
   <exportTaskId>export-i-1234wxyz</exportTaskId>
   <description>Example for docs</description>
   <state>active</state>
   <statusMessage>Running</statusMessage>
    <instanceExport>
     <instanceId>i-1234567890abcdef0</instanceId>
     <targetEnvironment>VMWare</targetEnvironment>
    </instanceExport>
    <exportToS3>
     <diskImageFormat>VMDK</diskImageFormat>
     <containerFormat>OVA</containerFormat>
     <s3Bucket>amzn-s3-demo-for-exported-vm</s3Bucket>
     <s3Key>my-exports/ export-i-1234wxyz.ova</s3Key>
    </exportToS3>
  </exportTask>
</CreateInstanceExportTaskResponse>
```

## See Also
<a name="API_CreateInstanceExportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateInstanceExportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateInstanceExportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateInstanceExportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateInstanceExportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateInstanceExportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateInstanceExportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateInstanceExportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateInstanceExportTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateInstanceExportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateInstanceExportTask)
