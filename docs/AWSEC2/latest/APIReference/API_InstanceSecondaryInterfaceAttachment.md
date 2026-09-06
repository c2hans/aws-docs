---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceSecondaryInterfaceAttachment.html
---

# InstanceSecondaryInterfaceAttachment
<a name="API_InstanceSecondaryInterfaceAttachment"></a>

Describes the attachment of a secondary interface to an instance.

## Contents
<a name="API_InstanceSecondaryInterfaceAttachment_Contents"></a>

 ** attachmentId **
The ID of the attachment.
Type: String
Required: No

 ** attachTime **
The timestamp when the attachment was created.
Type: Timestamp
Required: No

 ** deleteOnTermination **
Indicates whether the secondary interface is deleted when the instance is terminated.
The only supported value for this field is `true`.
Type: Boolean
Required: No

 ** deviceIndex **
The device index of the secondary interface.
Type: Integer
Required: No

 ** networkCardIndex **
The index of the network card.
Type: Integer
Required: No

 ** status **
The attachment state.
Type: String
Valid Values: `attaching | attached | detaching | detached`
Required: No

## See Also
<a name="API_InstanceSecondaryInterfaceAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceSecondaryInterfaceAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceSecondaryInterfaceAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceSecondaryInterfaceAttachment)
