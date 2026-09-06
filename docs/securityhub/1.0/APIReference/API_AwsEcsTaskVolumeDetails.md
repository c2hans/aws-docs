---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskVolumeDetails.html
---

# AwsEcsTaskVolumeDetails
<a name="API_AwsEcsTaskVolumeDetails"></a>

Provides information about a data volume that's used in a task definition.

## Contents
<a name="API_AwsEcsTaskVolumeDetails_Contents"></a>

 ** Host **   <a name="securityhub-Type-AwsEcsTaskVolumeDetails-Host"></a>
This parameter is specified when you use bind mount host volumes. The contents of the `host` parameter determine whether your bind mount host volume persists on the host container instance and where it's stored.
Type: [AwsEcsTaskVolumeHostDetails](API_AwsEcsTaskVolumeHostDetails.md) object
Required: No

 ** Name **   <a name="securityhub-Type-AwsEcsTaskVolumeDetails-Name"></a>
The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. This name is referenced in the `sourceVolume` parameter of container definition `mountPoints`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskVolumeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskVolumeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskVolumeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskVolumeDetails)
