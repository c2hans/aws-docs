---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateBlockDeviceMapping.html
---

# LaunchTemplateBlockDeviceMapping
<a name="API_LaunchTemplateBlockDeviceMapping"></a>

Describes a block device mapping.

## Contents
<a name="API_LaunchTemplateBlockDeviceMapping_Contents"></a>

 ** deviceName **
The device name.
Type: String
Required: No

 ** ebs **
Information about the block device for an EBS volume.
Type: [LaunchTemplateEbsBlockDevice](API_LaunchTemplateEbsBlockDevice.md) object
Required: No

 ** noDevice **
To omit the device from the block device mapping, specify an empty string.
Type: String
Required: No

 ** virtualName **
The virtual device name (ephemeralN).
Type: String
Required: No

## See Also
<a name="API_LaunchTemplateBlockDeviceMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateBlockDeviceMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateBlockDeviceMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateBlockDeviceMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
