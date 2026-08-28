---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-vpc-vpcencryptioncontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPC VpcEncryptionControl
<a name="aws-properties-ec2-vpc-vpcencryptioncontrol"></a>

Describes the configuration and state of VPC encryption controls.

For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.

## Syntax
<a name="aws-properties-ec2-vpc-vpcencryptioncontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-vpc-vpcencryptioncontrol-syntax.json"></a>

```
{
  "[EgressOnlyInternetGatewayExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-egressonlyinternetgatewayexclusion)" : {{String}},
  "[ElasticFileSystemExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-elasticfilesystemexclusion)" : {{String}},
  "[InternetGatewayExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-internetgatewayexclusion)" : {{String}},
  "[LambdaExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-lambdaexclusion)" : {{String}},
  "[Mode](#cfn-ec2-vpc-vpcencryptioncontrol-mode)" : {{String}},
  "[NatGatewayExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-natgatewayexclusion)" : {{String}},
  "[ResourceExclusions](#cfn-ec2-vpc-vpcencryptioncontrol-resourceexclusions)" : {{VpcEncryptionControlExclusions}},
  "[State](#cfn-ec2-vpc-vpcencryptioncontrol-state)" : {{String}},
  "[StateMessage](#cfn-ec2-vpc-vpcencryptioncontrol-statemessage)" : {{String}},
  "[VirtualPrivateGatewayExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-virtualprivategatewayexclusion)" : {{String}},
  "[VpcEncryptionControlId](#cfn-ec2-vpc-vpcencryptioncontrol-vpcencryptioncontrolid)" : {{String}},
  "[VpcId](#cfn-ec2-vpc-vpcencryptioncontrol-vpcid)" : {{String}},
  "[VpcLatticeExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-vpclatticeexclusion)" : {{String}},
  "[VpcPeeringExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-vpcpeeringexclusion)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-vpc-vpcencryptioncontrol-syntax.yaml"></a>

```
  [EgressOnlyInternetGatewayExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-egressonlyinternetgatewayexclusion): {{String}}
  [ElasticFileSystemExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-elasticfilesystemexclusion): {{String}}
  [InternetGatewayExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-internetgatewayexclusion): {{String}}
  [LambdaExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-lambdaexclusion): {{String}}
  [Mode](#cfn-ec2-vpc-vpcencryptioncontrol-mode): {{String}}
  [NatGatewayExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-natgatewayexclusion): {{String}}
  [ResourceExclusions](#cfn-ec2-vpc-vpcencryptioncontrol-resourceexclusions): {{
    VpcEncryptionControlExclusions}}
  [State](#cfn-ec2-vpc-vpcencryptioncontrol-state): {{String}}
  [StateMessage](#cfn-ec2-vpc-vpcencryptioncontrol-statemessage): {{String}}
  [VirtualPrivateGatewayExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-virtualprivategatewayexclusion): {{String}}
  [VpcEncryptionControlId](#cfn-ec2-vpc-vpcencryptioncontrol-vpcencryptioncontrolid): {{String}}
  [VpcId](#cfn-ec2-vpc-vpcencryptioncontrol-vpcid): {{String}}
  [VpcLatticeExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-vpclatticeexclusion): {{String}}
  [VpcPeeringExclusion](#cfn-ec2-vpc-vpcencryptioncontrol-vpcpeeringexclusion): {{String}}
```

## Properties
<a name="aws-properties-ec2-vpc-vpcencryptioncontrol-properties"></a>

`EgressOnlyInternetGatewayExclusion`  <a name="cfn-ec2-vpc-vpcencryptioncontrol-egressonlyinternetgatewayexclusion"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ElasticFileSystemExclusion`  <a name="cfn-ec2-vpc-vpcencryptioncontrol-elasticfilesystemexclusion"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InternetGatewayExclusion`  <a name="cfn-ec2-vpc-vpcencryptioncontrol-internetgatewayexclusion"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LambdaExclusion`  <a name="cfn-ec2-vpc-vpcencryptioncontrol-lambdaexclusion"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Mode`  <a name="cfn-ec2-vpc-vpcencryptioncontrol-mode"></a>
The encryption mode for the VPC Encryption Control configuration.
*Required*: No
*Type*: String
*Allowed values*: `monitor | enforce`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NatGatewayExclusion`  <a name="cfn-ec2-vpc-vpcencryptioncontrol-natgatewayexclusion"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceExclusions`  <a name="cfn-ec2-vpc-vpcencryptioncontrol-resourceexclusions"></a>
Information about resource exclusions for the VPC Encryption Control configuration.
*Required*: No
*Type*: [VpcEncryptionControlExclusions](aws-properties-ec2-vpc-vpcencryptioncontrolexclusions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`State`  <a name="cfn-ec2-vpc-vpcencryptioncontrol-state"></a>
The current state of the VPC Encryption Control configuration.
*Required*: No
*Type*: String
*Allowed values*: `enforce-in-progress | monitor-in-progress | enforce-failed | monitor-failed | deleting | deleted | available | creating | delete-failed`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StateMessage`  <a name="cfn-ec2-vpc-vpcencryptioncontrol-statemessage"></a>
A message providing additional information about the encryption control state.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VirtualPrivateGatewayExclusion`  <a name="cfn-ec2-vpc-vpcencryptioncontrol-virtualprivategatewayexclusion"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcEncryptionControlId`  <a name="cfn-ec2-vpc-vpcencryptioncontrol-vpcencryptioncontrolid"></a>
The ID of the VPC Encryption Control configuration.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-ec2-vpc-vpcencryptioncontrol-vpcid"></a>
The ID of the VPC associated with the encryption control configuration.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcLatticeExclusion`  <a name="cfn-ec2-vpc-vpcencryptioncontrol-vpclatticeexclusion"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcPeeringExclusion`  <a name="cfn-ec2-vpc-vpcencryptioncontrol-vpcpeeringexclusion"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
