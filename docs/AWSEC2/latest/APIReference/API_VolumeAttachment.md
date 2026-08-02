---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VolumeAttachment.html
---

# VolumeAttachment
<a name="API_VolumeAttachment"></a>

Describes volume attachment details.

## Contents
<a name="API_VolumeAttachment_Contents"></a>

 ** associatedResource **
The ARN of the AWS-managed resource to which the volume is attached.
Type: String
Required: No

 ** attachTime **
The time stamp when the attachment initiated.
Type: Timestamp
Required: No

 ** deleteOnTermination **
Indicates whether the EBS volume is deleted on instance termination.
Type: Boolean
Required: No

 ** device **
The device name.
If the volume is attached to an AWS-managed resource, this parameter returns `null`.
Type: String
Required: No

 ** ebsCardIndex **
The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.
Type: Integer
Required: No

 ** instanceId **
The ID of the instance.
If the volume is attached to an AWS-managed resource, this parameter returns `null`.
Type: String
Required: No

 ** instanceOwningService **
The service principal of the AWS service that owns the underlying resource to which the volume is attached.
This parameter is returned only for volumes that are attached to AWS-managed resources.
Type: String
Required: No

 ** status **
The attachment state of the volume.
Type: String
Valid Values: `attaching | attached | detaching | detached | busy`
Required: No

 ** volumeId **
The ID of the volume.
Type: String
Required: No

## See Also
<a name="API_VolumeAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VolumeAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VolumeAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VolumeAttachment)
