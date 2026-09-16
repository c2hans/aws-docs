---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_InstanceBlockDeviceMapping.html
---

# InstanceBlockDeviceMapping
<a name="API_InstanceBlockDeviceMapping"></a>

Defines block device mappings for the instance used to configure your image.

## Contents
<a name="API_InstanceBlockDeviceMapping_Contents"></a>

 ** deviceName **   <a name="imagebuilder-Type-InstanceBlockDeviceMapping-deviceName"></a>
The device to which these mappings apply.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ebs **   <a name="imagebuilder-Type-InstanceBlockDeviceMapping-ebs"></a>
The Amazon EBS-specific configuration for this mapping.
Type: [EbsInstanceBlockDeviceSpecification](API_EbsInstanceBlockDeviceSpecification.md) object
Required: No

 ** noDevice **   <a name="imagebuilder-Type-InstanceBlockDeviceMapping-noDevice"></a>
Specifies a mapping to remove from the base image.
Type: String
Length Constraints: Fixed length of 0.
Required: No

 ** virtualName **   <a name="imagebuilder-Type-InstanceBlockDeviceMapping-virtualName"></a>
The virtual device name for instance ephemeral devices.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_InstanceBlockDeviceMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/InstanceBlockDeviceMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/InstanceBlockDeviceMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/InstanceBlockDeviceMapping)
