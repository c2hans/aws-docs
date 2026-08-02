---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsInstanceBlockDevice.html
---

# EbsInstanceBlockDevice
<a name="API_EbsInstanceBlockDevice"></a>

Describes a parameter used to set up an EBS volume in a block device mapping.

## Contents
<a name="API_EbsInstanceBlockDevice_Contents"></a>

 ** associatedResource **
The ARN of the AWS-managed resource to which the volume is attached.
Type: String
Required: No

 ** attachTime **
The time stamp when the attachment initiated.
Type: Timestamp
Required: No

 ** deleteOnTermination **
Indicates whether the volume is deleted on instance termination.
Type: Boolean
Required: No

 ** ebsCardIndex **
The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.
Type: Integer
Required: No

 ** operator **
The service provider that manages the EBS volume.
Type: [OperatorResponse](API_OperatorResponse.md) object
Required: No

 ** status **
The attachment state.
Type: String
Valid Values: `attaching | attached | detaching | detached`
Required: No

 ** volumeId **
The ID of the EBS volume.
Type: String
Required: No

 ** volumeOwnerId **
The ID of the AWS account that owns the volume.
This parameter is returned only for volumes that are attached to AWS-managed resources.
Type: String
Required: No

## See Also
<a name="API_EbsInstanceBlockDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EbsInstanceBlockDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EbsInstanceBlockDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EbsInstanceBlockDevice)
