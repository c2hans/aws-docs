---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InternetGateway.html
---

# InternetGateway
<a name="API_InternetGateway"></a>

Describes an internet gateway.

## Contents
<a name="API_InternetGateway_Contents"></a>

 ** AttachmentSet.N **
Any VPCs attached to the internet gateway.
Type: Array of [InternetGatewayAttachment](API_InternetGatewayAttachment.md) objects
Required: No

 ** internetGatewayId **
The ID of the internet gateway.
Type: String
Required: No

 ** ownerId **
The ID of the AWS account that owns the internet gateway.
Type: String
Required: No

 ** TagSet.N **
Any tags assigned to the internet gateway.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_InternetGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InternetGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InternetGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InternetGateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
