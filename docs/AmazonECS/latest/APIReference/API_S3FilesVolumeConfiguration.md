---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_S3FilesVolumeConfiguration.html
---

# S3FilesVolumeConfiguration
<a name="API_S3FilesVolumeConfiguration"></a>

This parameter is specified when you're using an Amazon S3 Files file system for task storage. For more information, see [Amazon S3 Files volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/s3files-volumes.html) in the *Amazon Elastic Container Service Developer Guide*.

**Important**
Your task definition must include a Task IAM Role. See [ IAM role for attaching your file system to AWS compute resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-prereq-policies.html#s3-files-prereq-iam-compute-role) for required permissions.

## Contents
<a name="API_S3FilesVolumeConfiguration_Contents"></a>

 ** fileSystemArn **   <a name="ECS-Type-S3FilesVolumeConfiguration-fileSystemArn"></a>
The full ARN of the S3 Files file system to mount.
Type: String
Required: Yes

 ** accessPointArn **   <a name="ECS-Type-S3FilesVolumeConfiguration-accessPointArn"></a>
The full ARN of the S3 Files access point to use. If an access point is specified, the root directory value specified in the `S3FilesVolumeConfiguration` must either be omitted or set to `/` which will enforce the path set on the S3 Files access point. For more information, see [Creating S3 Files access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-access-points-creating.html).
Type: String
Required: No

 ** rootDirectory **   <a name="ECS-Type-S3FilesVolumeConfiguration-rootDirectory"></a>
The directory within the Amazon S3 Files file system to mount as the root directory. If this parameter is omitted, the root of the Amazon S3 Files file system will be used. Specifying `/` will have the same effect as omitting this parameter.
If a S3 Files access point is specified in the `accessPointArn`, the root directory parameter must either be omitted or set to `/` which will enforce the path set on the S3 Files access point.
Type: String
Required: No

 ** transitEncryptionPort **   <a name="ECS-Type-S3FilesVolumeConfiguration-transitEncryptionPort"></a>
The port to use for sending encrypted data between the ECS host and the S3 Files file system. If you do not specify a transit encryption port, it will use the port selection strategy that the Amazon S3 Files mount helper uses. For more information, see [S3 Files mount helper](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-mounting.html).
Type: Integer
Required: No

## See Also
<a name="API_S3FilesVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/S3FilesVolumeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/S3FilesVolumeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/S3FilesVolumeConfiguration)
