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
Use to manage Amazon EBS-specific configuration for this mapping.
Type: [EbsInstanceBlockDeviceSpecification](API_EbsInstanceBlockDeviceSpecification.md) object
Required: No

 ** noDevice **   <a name="imagebuilder-Type-InstanceBlockDeviceMapping-noDevice"></a>
Use to remove a mapping from the base image.
Type: String
Length Constraints: Fixed length of 0.
Required: No

 ** virtualName **   <a name="imagebuilder-Type-InstanceBlockDeviceMapping-virtualName"></a>
Use to manage instance ephemeral devices.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_InstanceBlockDeviceMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/InstanceBlockDeviceMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/InstanceBlockDeviceMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/InstanceBlockDeviceMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
