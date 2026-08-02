---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsContainerDetails.html
---

# AwsEcsContainerDetails
<a name="API_AwsEcsContainerDetails"></a>

Provides information about an Amazon ECS container.

## Contents
<a name="API_AwsEcsContainerDetails_Contents"></a>

 ** Image **   <a name="securityhub-Type-AwsEcsContainerDetails-Image"></a>
The image used for the container.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MountPoints **   <a name="securityhub-Type-AwsEcsContainerDetails-MountPoints"></a>
The mount points for data volumes in your container.
Type: Array of [AwsMountPoint](API_AwsMountPoint.md) objects
Required: No

 ** Name **   <a name="securityhub-Type-AwsEcsContainerDetails-Name"></a>
The name of the container.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Privileged **   <a name="securityhub-Type-AwsEcsContainerDetails-Privileged"></a>
When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user).
Type: Boolean
Required: No

## See Also
<a name="API_AwsEcsContainerDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsContainerDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsContainerDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsContainerDetails)
