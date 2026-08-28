---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_VpcAttachment.html
---

# VpcAttachment
<a name="API_VpcAttachment"></a>

Describes a VPC attachment.

## Contents
<a name="API_VpcAttachment_Contents"></a>

 ** Attachment **   <a name="networkmanager-Type-VpcAttachment-Attachment"></a>
Provides details about the VPC attachment.
Type: [Attachment](API_Attachment.md) object
Required: No

 ** Options **   <a name="networkmanager-Type-VpcAttachment-Options"></a>
Provides details about the VPC attachment.
Type: [VpcOptions](API_VpcOptions.md) object
Required: No

 ** SubnetArns **   <a name="networkmanager-Type-VpcAttachment-SubnetArns"></a>
The subnet ARNs.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:subnet\/subnet-[0-9a-f]{8,17}$|^$`
Required: No

## See Also
<a name="API_VpcAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/VpcAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/VpcAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/VpcAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
