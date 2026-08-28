---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMappingResponse.html
---

# BlockDeviceMappingResponse
<a name="API_BlockDeviceMappingResponse"></a>

Describes a block device mapping, which defines the EBS volumes and instance store volumes to attach to an instance at launch.

## Contents
<a name="API_BlockDeviceMappingResponse_Contents"></a>

 ** deviceName **
The device name (for example, `/dev/sdh` or `xvdh`).
Type: String
Required: No

 ** ebs **
Parameters used to automatically set up EBS volumes when the instance is launched.
Type: [EbsBlockDeviceResponse](API_EbsBlockDeviceResponse.md) object
Required: No

 ** noDevice **
Suppresses the specified device included in the block device mapping.
Type: String
Required: No

 ** virtualName **
The virtual device name.
Type: String
Required: No

## See Also
<a name="API_BlockDeviceMappingResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/BlockDeviceMappingResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/BlockDeviceMappingResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/BlockDeviceMappingResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
