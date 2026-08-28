---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockPublicAccessStates.html
---

# BlockPublicAccessStates
<a name="API_BlockPublicAccessStates"></a>

The state of VPC Block Public Access (BPA).

## Contents
<a name="API_BlockPublicAccessStates_Contents"></a>

 ** internetGatewayBlockMode **
The mode of VPC BPA.
+  `off`: VPC BPA is not enabled and traffic is allowed to and from internet gateways and egress-only internet gateways in this Region.
+  `block-bidirectional`: Block all traffic to and from internet gateways and egress-only internet gateways in this Region (except for excluded VPCs and subnets).
+  `block-ingress`: Block all internet traffic to the VPCs in this Region (except for VPCs or subnets which are excluded). Only traffic to and from NAT gateways and egress-only internet gateways is allowed because these gateways only allow outbound connections to be established.
Type: String
Valid Values: `off | block-bidirectional | block-ingress`
Required: No

## See Also
<a name="API_BlockPublicAccessStates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/BlockPublicAccessStates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/BlockPublicAccessStates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/BlockPublicAccessStates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
