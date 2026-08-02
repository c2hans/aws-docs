---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_InstanceConfiguration.html
---

# InstanceConfiguration
<a name="API_InstanceConfiguration"></a>

Defines a custom base AMI and block device mapping configurations of an instance used for building and testing container images.

## Contents
<a name="API_InstanceConfiguration_Contents"></a>

 ** blockDeviceMappings **   <a name="imagebuilder-Type-InstanceConfiguration-blockDeviceMappings"></a>
Defines the block devices to attach for building an instance from this Image Builder AMI.
Type: Array of [InstanceBlockDeviceMapping](API_InstanceBlockDeviceMapping.md) objects
Required: No

 ** image **   <a name="imagebuilder-Type-InstanceConfiguration-image"></a>
The base image for a container build and test instance. This can contain an AMI ID or it can specify an AWS Systems Manager (SSM) Parameter Store Parameter, prefixed by `ssm:`, followed by the parameter name or ARN.
If not specified, Image Builder uses the appropriate ECS-optimized AMI as a base image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_InstanceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/InstanceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/InstanceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/InstanceConfiguration)
