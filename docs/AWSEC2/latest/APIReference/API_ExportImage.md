---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportImage.html
---

# ExportImage
<a name="API_ExportImage"></a>

Exports an Amazon Machine Image (AMI) to a VM file. For more information, see [Exporting a VM directly from an Amazon Machine Image (AMI)](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport_image.html) in the *VM Import/Export User Guide*.

## Request Parameters
<a name="API_ExportImage_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Token to enable idempotency for export image requests.
Type: String
Required: No

 **Description**
A description of the image being exported. The maximum length is 255 characters.
Type: String
Required: No

 **DiskImageFormat**
The disk image format.
Type: String
Valid Values: `VMDK | RAW | VHD`
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ImageId**
The ID of the image.
Type: String
Required: Yes

 **RoleName**
The name of the role that grants VM Import/Export permission to export images to your Amazon S3 bucket. If this parameter is not specified, the default role is named 'vmimport'.
Type: String
Required: No

 **S3ExportLocation**
The Amazon S3 bucket for the destination image. The destination bucket must exist.
Type: [ExportTaskS3LocationRequest](API_ExportTaskS3LocationRequest.md) object
Required: Yes

 **TagSpecification.N**
The tags to apply to the export image task during creation.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_ExportImage_ResponseElements"></a>

The following elements are returned by the service.

 **description**
A description of the image being exported.
Type: String

 **diskImageFormat**
The disk image format for the exported image.
Type: String
Valid Values: `VMDK | RAW | VHD`

 **exportImageTaskId**
The ID of the export image task.
Type: String

 **imageId**
The ID of the image.
Type: String

 **progress**
The percent complete of the export image task.
Type: String

 **requestId**
The ID of the request.
Type: String

 **roleName**
The name of the role that grants VM Import/Export permission to export images to your Amazon S3 bucket.
Type: String

 **s3ExportLocation**
Information about the destination Amazon S3 bucket.
Type: [ExportTaskS3Location](API_ExportTaskS3Location.md) object

 **status**
The status of the export image task. The possible values are `active`, `completed`, `deleting`, and `deleted`.
Type: String

 **statusMessage**
The status message for the export image task.
Type: String

 **tagSet**
Any tags assigned to the export image task.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_ExportImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ExportImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ExportImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ExportImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ExportImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ExportImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ExportImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ExportImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ExportImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ExportImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ExportImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ExportImage)
