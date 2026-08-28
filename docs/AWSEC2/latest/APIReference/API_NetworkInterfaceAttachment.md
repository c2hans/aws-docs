---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NetworkInterfaceAttachment.html
---

# NetworkInterfaceAttachment
<a name="API_NetworkInterfaceAttachment"></a>

Describes a network interface attachment.

## Contents
<a name="API_NetworkInterfaceAttachment_Contents"></a>

 ** attachmentId **
The ID of the network interface attachment.
Type: String
Required: No

 ** attachTime **
The timestamp indicating when the attachment initiated.
Type: Timestamp
Required: No

 ** deleteOnTermination **
Indicates whether the network interface is deleted when the instance is terminated.
Type: Boolean
Required: No

 ** deviceIndex **
The device index of the network interface attachment on the instance.
Type: Integer
Required: No

 ** enaQueueCount **
The number of ENA queues created with the instance.
Type: Integer
Required: No

 ** enaSrdSpecification **
Configures ENA Express for the network interface that this action attaches to the instance.
Type: [AttachmentEnaSrdSpecification](API_AttachmentEnaSrdSpecification.md) object
Required: No

 ** instanceId **
The ID of the instance.
Type: String
Required: No

 ** instanceOwnerId **
The AWS account ID of the owner of the instance.
Type: String
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
<a name="API_NetworkInterfaceAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NetworkInterfaceAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NetworkInterfaceAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NetworkInterfaceAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
