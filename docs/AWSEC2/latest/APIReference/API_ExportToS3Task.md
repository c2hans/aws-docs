---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportToS3Task.html
---

# ExportToS3Task
<a name="API_ExportToS3Task"></a>

Describes the format and location for the export task.

## Contents
<a name="API_ExportToS3Task_Contents"></a>

 ** containerFormat **
The container format used to combine disk images with metadata (such as OVF). If absent, only the disk image is exported.
Type: String
Valid Values: `ova`
Required: No

 ** diskImageFormat **
The format for the exported image.
Type: String
Valid Values: `VMDK | RAW | VHD`
Required: No

 ** s3Bucket **
The Amazon S3 bucket for the destination image. The destination bucket must exist and have an access control list (ACL) attached that specifies the Region-specific canonical account ID for the `Grantee`. For more information about the ACL to your S3 bucket, see [Prerequisites](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html#vmexport-prerequisites) in the VM Import/Export User Guide.
Type: String
Required: No

 ** s3Key **
The encryption key for your S3 bucket.
Type: String
Required: No

## See Also
<a name="API_ExportToS3Task_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ExportToS3Task)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ExportToS3Task)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ExportToS3Task)
