---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpcEncryptionControlConfiguration.html
---

# VpcEncryptionControlConfiguration
<a name="API_VpcEncryptionControlConfiguration"></a>

Describes the configuration settings for VPC Encryption Control.

For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.

## Contents
<a name="API_VpcEncryptionControlConfiguration_Contents"></a>

 ** Mode **
The encryption mode for the VPC Encryption Control configuration.
Type: String
Valid Values: `monitor | enforce`
Required: Yes

 ** EgressOnlyInternetGatewayExclusion **
Specifies whether to exclude egress-only internet gateway traffic from encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

 ** ElasticFileSystemExclusion **
Specifies whether to exclude Elastic File System traffic from encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

 ** InternetGatewayExclusion **
Specifies whether to exclude internet gateway traffic from encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

 ** LambdaExclusion **
Specifies whether to exclude Lambda function traffic from encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

 ** NatGatewayExclusion **
Specifies whether to exclude NAT gateway traffic from encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

 ** VirtualPrivateGatewayExclusion **
Specifies whether to exclude virtual private gateway traffic from encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

 ** VpcLatticeExclusion **
Specifies whether to exclude VPC Lattice traffic from encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

 ** VpcPeeringExclusion **
Specifies whether to exclude VPC peering connection traffic from encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

## See Also
<a name="API_VpcEncryptionControlConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpcEncryptionControlConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpcEncryptionControlConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpcEncryptionControlConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
