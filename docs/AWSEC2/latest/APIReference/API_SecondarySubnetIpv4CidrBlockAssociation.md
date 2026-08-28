---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecondarySubnetIpv4CidrBlockAssociation.html
---

# SecondarySubnetIpv4CidrBlockAssociation
<a name="API_SecondarySubnetIpv4CidrBlockAssociation"></a>

Describes an IPv4 CIDR block associated with a secondary subnet.

## Contents
<a name="API_SecondarySubnetIpv4CidrBlockAssociation_Contents"></a>

 ** associationId **
The association ID for the IPv4 CIDR block.
Type: String
Required: No

 ** cidrBlock **
The IPv4 CIDR block.
Type: String
Required: No

 ** state **
The state of the CIDR block association.
Type: String
Valid Values: `associating | associated | association-failed | disassociating | disassociated | disassociation-failed`
Required: No

 ** stateReason **
The reason for the current state of the CIDR block association.
Type: String
Required: No

## See Also
<a name="API_SecondarySubnetIpv4CidrBlockAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SecondarySubnetIpv4CidrBlockAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SecondarySubnetIpv4CidrBlockAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SecondarySubnetIpv4CidrBlockAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
