---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails.html
---

# AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails
<a name="API_AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails"></a>

Information about the Amazon Elastic File System file system that is used for task storage.

## Contents
<a name="API_AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails_Contents"></a>

 ** AuthorizationConfig **   <a name="securityhub-Type-AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails-AuthorizationConfig"></a>
The authorization configuration details for the Amazon EFS file system.
Type: [AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails](API_AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails.md) object
Required: No

 ** FilesystemId **   <a name="securityhub-Type-AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails-FilesystemId"></a>
The Amazon EFS file system identifier to use.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RootDirectory **   <a name="securityhub-Type-AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails-RootDirectory"></a>
The directory within the Amazon EFS file system to mount as the root directory inside the host.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TransitEncryption **   <a name="securityhub-Type-AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails-TransitEncryption"></a>
Whether to enable encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TransitEncryptionPort **   <a name="securityhub-Type-AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails-TransitEncryptionPort"></a>
The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server.
Type: Integer
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails)
