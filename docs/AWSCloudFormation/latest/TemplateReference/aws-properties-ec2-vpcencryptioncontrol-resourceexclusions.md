---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-vpcencryptioncontrol-resourceexclusions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPCEncryptionControl ResourceExclusions
<a name="aws-properties-ec2-vpcencryptioncontrol-resourceexclusions"></a>

Information about resource exclusions for the VPC Encryption Control configuration.

## Syntax
<a name="aws-properties-ec2-vpcencryptioncontrol-resourceexclusions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-vpcencryptioncontrol-resourceexclusions-syntax.json"></a>

```
{
  "[EgressOnlyInternetGateway](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-egressonlyinternetgateway)" : {{VpcEncryptionControlExclusion}},
  "[ElasticFileSystem](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-elasticfilesystem)" : {{VpcEncryptionControlExclusion}},
  "[InternetGateway](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-internetgateway)" : {{VpcEncryptionControlExclusion}},
  "[Lambda](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-lambda)" : {{VpcEncryptionControlExclusion}},
  "[NatGateway](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-natgateway)" : {{VpcEncryptionControlExclusion}},
  "[VirtualPrivateGateway](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-virtualprivategateway)" : {{VpcEncryptionControlExclusion}},
  "[VpcLattice](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-vpclattice)" : {{VpcEncryptionControlExclusion}},
  "[VpcPeering](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-vpcpeering)" : {{VpcEncryptionControlExclusion}}
}
```

### YAML
<a name="aws-properties-ec2-vpcencryptioncontrol-resourceexclusions-syntax.yaml"></a>

```
  [EgressOnlyInternetGateway](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-egressonlyinternetgateway): {{
    VpcEncryptionControlExclusion}}
  [ElasticFileSystem](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-elasticfilesystem): {{
    VpcEncryptionControlExclusion}}
  [InternetGateway](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-internetgateway): {{
    VpcEncryptionControlExclusion}}
  [Lambda](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-lambda): {{
    VpcEncryptionControlExclusion}}
  [NatGateway](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-natgateway): {{
    VpcEncryptionControlExclusion}}
  [VirtualPrivateGateway](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-virtualprivategateway): {{
    VpcEncryptionControlExclusion}}
  [VpcLattice](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-vpclattice): {{
    VpcEncryptionControlExclusion}}
  [VpcPeering](#cfn-ec2-vpcencryptioncontrol-resourceexclusions-vpcpeering): {{
    VpcEncryptionControlExclusion}}
```

## Properties
<a name="aws-properties-ec2-vpcencryptioncontrol-resourceexclusions-properties"></a>

`EgressOnlyInternetGateway`  <a name="cfn-ec2-vpcencryptioncontrol-resourceexclusions-egressonlyinternetgateway"></a>
Specifies whether to exclude egress-only internet gateway traffic from encryption enforcement.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion.md)
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ElasticFileSystem`  <a name="cfn-ec2-vpcencryptioncontrol-resourceexclusions-elasticfilesystem"></a>
Specifies whether to exclude Elastic File System traffic from encryption enforcement.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion.md)
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InternetGateway`  <a name="cfn-ec2-vpcencryptioncontrol-resourceexclusions-internetgateway"></a>
Specifies whether to exclude internet gateway traffic from encryption enforcement.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion.md)
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Lambda`  <a name="cfn-ec2-vpcencryptioncontrol-resourceexclusions-lambda"></a>
Specifies whether to exclude Lambda function traffic from encryption enforcement.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion.md)
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NatGateway`  <a name="cfn-ec2-vpcencryptioncontrol-resourceexclusions-natgateway"></a>
Specifies whether to exclude NAT gateway traffic from encryption enforcement.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion.md)
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VirtualPrivateGateway`  <a name="cfn-ec2-vpcencryptioncontrol-resourceexclusions-virtualprivategateway"></a>
Specifies whether to exclude virtual private gateway traffic from encryption enforcement.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion.md)
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcLattice`  <a name="cfn-ec2-vpcencryptioncontrol-resourceexclusions-vpclattice"></a>
Specifies whether to exclude VPC Lattice traffic from encryption enforcement.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion.md)
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcPeering`  <a name="cfn-ec2-vpcencryptioncontrol-resourceexclusions-vpcpeering"></a>
Specifies whether to exclude VPC peering connection traffic from encryption enforcement.
*Required*: No
*Type*: [VpcEncryptionControlExclusion](aws-properties-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion.md)
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
