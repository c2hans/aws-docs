---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpcBlockPublicAccessOptions.html
---

# VpcBlockPublicAccessOptions
<a name="API_VpcBlockPublicAccessOptions"></a>

VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. To learn more about VPC BPA, see [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) in the *Amazon VPC User Guide*.

## Contents
<a name="API_VpcBlockPublicAccessOptions_Contents"></a>

 ** awsAccountId **
An AWS account ID.
Type: String
Required: No

 ** awsRegion **
An AWS Region.
Type: String
Required: No

 ** exclusionsAllowed **
Determines if exclusions are allowed. If you have [enabled VPC BPA at the Organization level](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html#security-vpc-bpa-exclusions-orgs), exclusions may be `not-allowed`. Otherwise, they are `allowed`.
Type: String
Valid Values: `allowed | not-allowed`
Required: No

 ** internetGatewayBlockMode **
The current mode of VPC BPA.
+  `off`: VPC BPA is not enabled and traffic is allowed to and from internet gateways and egress-only internet gateways in this Region.
+  `block-bidirectional`: Block all traffic to and from internet gateways and egress-only internet gateways in this Region (except for excluded VPCs and subnets).
+  `block-ingress`: Block all internet traffic to the VPCs in this Region (except for VPCs or subnets which are excluded). Only traffic to and from NAT gateways and egress-only internet gateways is allowed because these gateways only allow outbound connections to be established.
Type: String
Valid Values: `off | block-bidirectional | block-ingress`
Required: No

 ** lastUpdateTimestamp **
The last time the VPC BPA mode was updated.
Type: Timestamp
Required: No

 ** managedBy **
The entity that manages the state of VPC BPA. Possible values include:
+  `account` - The state is managed by the account.
+  `declarative-policy` - The state is managed by a declarative policy and can't be modified by the account.
Type: String
Valid Values: `account | declarative-policy`
Required: No

 ** reason **
The reason for the current state.
Type: String
Required: No

 ** state **
The current state of VPC BPA.
Type: String
Valid Values: `default-state | update-in-progress | update-complete`
Required: No

## See Also
<a name="API_VpcBlockPublicAccessOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpcBlockPublicAccessOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpcBlockPublicAccessOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpcBlockPublicAccessOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
