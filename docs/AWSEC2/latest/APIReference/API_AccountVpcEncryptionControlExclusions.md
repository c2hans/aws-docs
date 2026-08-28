---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AccountVpcEncryptionControlExclusions.html
---

# AccountVpcEncryptionControlExclusions
<a name="API_AccountVpcEncryptionControlExclusions"></a>

Describes the exclusion configurations for the various resource types in the account-level VPC Encryption Control configuration.

For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.

## Contents
<a name="API_AccountVpcEncryptionControlExclusions_Contents"></a>

 ** egressOnlyInternetGateway **
The exclusion configuration for egress-only internet gateway resource.
Type: String
Valid Values: `enabling | enabled | disabling | disabled`
Required: No

 ** elasticFileSystem **
The exclusion configuration for Elastic File System service.
Type: String
Valid Values: `enabling | enabled | disabling | disabled`
Required: No

 ** internetGateway **
The exclusion configuration for internet gateway resource.
Type: String
Valid Values: `enabling | enabled | disabling | disabled`
Required: No

 ** lambda **
The exclusion configuration for Lambda service.
Type: String
Valid Values: `enabling | enabled | disabling | disabled`
Required: No

 ** natGateway **
The exclusion configuration for NAT gateway resource.
Type: String
Valid Values: `enabling | enabled | disabling | disabled`
Required: No

 ** virtualPrivateGateway **
The exclusion configuration for virtual private gateway resource.
Type: String
Valid Values: `enabling | enabled | disabling | disabled`
Required: No

 ** vpcLattice **
The exclusion configuration for VPC Lattice service.
Type: String
Valid Values: `enabling | enabled | disabling | disabled`
Required: No

 ** vpcPeering **
The exclusion configuration for VPC peering connection resource.
Type: String
Valid Values: `enabling | enabled | disabling | disabled`
Required: No

## See Also
<a name="API_AccountVpcEncryptionControlExclusions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AccountVpcEncryptionControlExclusions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AccountVpcEncryptionControlExclusions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AccountVpcEncryptionControlExclusions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
