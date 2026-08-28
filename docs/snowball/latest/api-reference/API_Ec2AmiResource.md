---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_Ec2AmiResource.html
---

# Ec2AmiResource
<a name="API_Ec2AmiResource"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2-compatible AMI ID and the Snow device AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

## Contents
<a name="API_Ec2AmiResource_Contents"></a>

 ** AmiId **   <a name="Snowball-Type-Ec2AmiResource-AmiId"></a>
The ID of the AMI in Amazon EC2.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `(ami-[0-9a-f]{8})|(ami-[0-9a-f]{17})`
Required: Yes

 ** SnowballAmiId **   <a name="Snowball-Type-Ec2AmiResource-SnowballAmiId"></a>
The ID of the AMI on the Snow device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## See Also
<a name="API_Ec2AmiResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/Ec2AmiResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/Ec2AmiResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/Ec2AmiResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
