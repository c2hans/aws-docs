---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_EFSVolumeConfiguration.html
---

# EFSVolumeConfiguration
<a name="API_EFSVolumeConfiguration"></a>

This parameter is specified when you're using an Amazon Elastic File System file system for task storage. For more information, see [Amazon EFS volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/efs-volumes.html) in the *Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_EFSVolumeConfiguration_Contents"></a>

 ** fileSystemId **   <a name="ECS-Type-EFSVolumeConfiguration-fileSystemId"></a>
The Amazon EFS file system ID to use.
Type: String
Required: Yes

 ** authorizationConfig **   <a name="ECS-Type-EFSVolumeConfiguration-authorizationConfig"></a>
The authorization configuration details for the Amazon EFS file system.
Type: [EFSAuthorizationConfig](API_EFSAuthorizationConfig.md) object
Required: No

 ** rootDirectory **   <a name="ECS-Type-EFSVolumeConfiguration-rootDirectory"></a>
The directory within the Amazon EFS file system to mount as the root directory inside the host. If this parameter is omitted, the root of the Amazon EFS volume will be used. Specifying `/` will have the same effect as omitting this parameter.
If an EFS access point is specified in the `authorizationConfig`, the root directory parameter must either be omitted or set to `/` which will enforce the path set on the EFS access point.
Type: String
Required: No

 ** transitEncryption **   <a name="ECS-Type-EFSVolumeConfiguration-transitEncryption"></a>
Determines whether to use encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server. Transit encryption must be turned on if Amazon EFS IAM authorization is used. If this parameter is omitted, the default value of `DISABLED` is used. For more information, see [Encrypting data in transit](https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html) in the *Amazon Elastic File System User Guide*.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** transitEncryptionPort **   <a name="ECS-Type-EFSVolumeConfiguration-transitEncryptionPort"></a>
The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server. If you do not specify a transit encryption port, it will use the port selection strategy that the Amazon EFS mount helper uses. For more information, see [EFS mount helper](https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html) in the *Amazon Elastic File System User Guide*.
Type: Integer
Required: No

## See Also
<a name="API_EFSVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/EFSVolumeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/EFSVolumeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/EFSVolumeConfiguration)
