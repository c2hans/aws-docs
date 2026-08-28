---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecondaryInterfaceAttachment.html
---

# SecondaryInterfaceAttachment
<a name="API_SecondaryInterfaceAttachment"></a>

Describes the attachment of a secondary interface to an instance.

## Contents
<a name="API_SecondaryInterfaceAttachment_Contents"></a>

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

 ** instanceId **
The ID of the instance to which the secondary interface is attached.
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
<a name="API_SecondaryInterfaceAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SecondaryInterfaceAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SecondaryInterfaceAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SecondaryInterfaceAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
