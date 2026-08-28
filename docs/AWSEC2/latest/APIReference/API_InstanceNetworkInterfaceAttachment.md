---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceNetworkInterfaceAttachment.html
---

# InstanceNetworkInterfaceAttachment
<a name="API_InstanceNetworkInterfaceAttachment"></a>

Describes a network interface attachment.

## Contents
<a name="API_InstanceNetworkInterfaceAttachment_Contents"></a>

 ** attachmentId **
The ID of the network interface attachment.
Type: String
Required: No

 ** attachTime **
The time stamp when the attachment initiated.
Type: Timestamp
Required: No

 ** deleteOnTermination **
Indicates whether the network interface is deleted when the instance is terminated.
Type: Boolean
Required: No

 ** deviceIndex **
The index of the device on the instance for the network interface attachment.
Type: Integer
Required: No

 ** enaQueueCount **
The number of ENA queues created with the instance.
Type: Integer
Required: No

 ** enaSrdSpecification **
Contains the ENA Express settings for the network interface that's attached to the instance.
Type: [InstanceAttachmentEnaSrdSpecification](API_InstanceAttachmentEnaSrdSpecification.md) object
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
<a name="API_InstanceNetworkInterfaceAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceNetworkInterfaceAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceNetworkInterfaceAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceNetworkInterfaceAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
