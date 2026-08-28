---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-vpc-vpcencryptioncontrolexclusions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPC VpcEncryptionControlExclusions
<a name="aws-properties-ec2-vpc-vpcencryptioncontrolexclusions"></a>

Describes the exclusion configurations for various resource types in VPC Encryption Control.

For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.

## Syntax
<a name="aws-properties-ec2-vpc-vpcencryptioncontrolexclusions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-vpc-vpcencryptioncontrolexclusions-syntax.json"></a>

```
{
  "[EgressOnlyInternetGateway](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-egressonlyinternetgateway)" : {{VpcEncryptionControlExclusion}},
  "[ElasticFileSystem](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-elasticfilesystem)" : {{VpcEncryptionControlExclusion}},
  "[InternetGateway](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-internetgateway)" : {{VpcEncryptionControlExclusion}},
  "[Lambda](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-lambda)" : {{VpcEncryptionControlExclusion}},
  "[NatGateway](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-natgateway)" : {{VpcEncryptionControlExclusion}},
  "[VirtualPrivateGateway](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-virtualprivategateway)" : {{VpcEncryptionControlExclusion}},
  "[VpcLattice](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-vpclattice)" : {{VpcEncryptionControlExclusion}},
  "[VpcPeering](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-vpcpeering)" : {{VpcEncryptionControlExclusion}}
}
```

### YAML
<a name="aws-properties-ec2-vpc-vpcencryptioncontrolexclusions-syntax.yaml"></a>

```
  [EgressOnlyInternetGateway](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-egressonlyinternetgateway): {{
    VpcEncryptionControlExclusion}}
  [ElasticFileSystem](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-elasticfilesystem): {{
    VpcEncryptionControlExclusion}}
  [InternetGateway](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-internetgateway): {{
    VpcEncryptionControlExclusion}}
  [Lambda](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-lambda): {{
    VpcEncryptionControlExclusion}}
  [NatGateway](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-natgateway): {{
    VpcEncryptionControlExclusion}}
  [VirtualPrivateGateway](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-virtualprivategateway): {{
    VpcEncryptionControlExclusion}}
  [VpcLattice](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-vpclattice): {{
    VpcEncryptionControlExclusion}}
  [VpcPeering](#cfn-ec2-vpc-vpcencryptioncontrolexclusions-vpcpeering): {{
    VpcEncryptionControlExclusion}}
```

## Properties
<a name="aws-properties-ec2-vpc-vpcencryptioncontrolexclusions-properties"></a>

`EgressOnlyInternetGateway`  <a name="cfn-ec2-vpc-vpcencryptioncontrolexclusions-egressonlyinternetgateway"></a>
The exclusion configuration for egress-only internet gateway traffic.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpc-vpcencryptioncontrolexclusion.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ElasticFileSystem`  <a name="cfn-ec2-vpc-vpcencryptioncontrolexclusions-elasticfilesystem"></a>
The exclusion configuration for Elastic File System traffic.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpc-vpcencryptioncontrolexclusion.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InternetGateway`  <a name="cfn-ec2-vpc-vpcencryptioncontrolexclusions-internetgateway"></a>
The exclusion configuration for internet gateway traffic.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpc-vpcencryptioncontrolexclusion.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Lambda`  <a name="cfn-ec2-vpc-vpcencryptioncontrolexclusions-lambda"></a>
The exclusion configuration for Lambda function traffic.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpc-vpcencryptioncontrolexclusion.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NatGateway`  <a name="cfn-ec2-vpc-vpcencryptioncontrolexclusions-natgateway"></a>
The exclusion configuration for NAT gateway traffic.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpc-vpcencryptioncontrolexclusion.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VirtualPrivateGateway`  <a name="cfn-ec2-vpc-vpcencryptioncontrolexclusions-virtualprivategateway"></a>
The exclusion configuration for virtual private gateway traffic.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpc-vpcencryptioncontrolexclusion.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcLattice`  <a name="cfn-ec2-vpc-vpcencryptioncontrolexclusions-vpclattice"></a>
The exclusion configuration for VPC Lattice traffic.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpc-vpcencryptioncontrolexclusion.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcPeering`  <a name="cfn-ec2-vpc-vpcencryptioncontrolexclusions-vpcpeering"></a>
The exclusion configuration for VPC peering connection traffic.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpc-vpcencryptioncontrolexclusion.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
