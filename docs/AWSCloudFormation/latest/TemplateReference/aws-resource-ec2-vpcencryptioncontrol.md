---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpcencryptioncontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPCEncryptionControl
<a name="aws-resource-ec2-vpcencryptioncontrol"></a>

Describes the configuration and state of VPC encryption controls.

For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.

## Syntax
<a name="aws-resource-ec2-vpcencryptioncontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-vpcencryptioncontrol-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::VPCEncryptionControl",
  "Properties" : {
      "[EgressOnlyInternetGatewayExclusionInput](#cfn-ec2-vpcencryptioncontrol-egressonlyinternetgatewayexclusioninput)" : {{String}},
      "[ElasticFileSystemExclusionInput](#cfn-ec2-vpcencryptioncontrol-elasticfilesystemexclusioninput)" : {{String}},
      "[InternetGatewayExclusionInput](#cfn-ec2-vpcencryptioncontrol-internetgatewayexclusioninput)" : {{String}},
      "[LambdaExclusionInput](#cfn-ec2-vpcencryptioncontrol-lambdaexclusioninput)" : {{String}},
      "[Mode](#cfn-ec2-vpcencryptioncontrol-mode)" : {{String}},
      "[NatGatewayExclusionInput](#cfn-ec2-vpcencryptioncontrol-natgatewayexclusioninput)" : {{String}},
      "[Tags](#cfn-ec2-vpcencryptioncontrol-tags)" : {{[ Tag, ... ]}},
      "[VirtualPrivateGatewayExclusionInput](#cfn-ec2-vpcencryptioncontrol-virtualprivategatewayexclusioninput)" : {{String}},
      "[VpcId](#cfn-ec2-vpcencryptioncontrol-vpcid)" : {{String}},
      "[VpcLatticeExclusionInput](#cfn-ec2-vpcencryptioncontrol-vpclatticeexclusioninput)" : {{String}},
      "[VpcPeeringExclusionInput](#cfn-ec2-vpcencryptioncontrol-vpcpeeringexclusioninput)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-vpcencryptioncontrol-syntax.yaml"></a>

```
Type: AWS::EC2::VPCEncryptionControl
Properties:
  [EgressOnlyInternetGatewayExclusionInput](#cfn-ec2-vpcencryptioncontrol-egressonlyinternetgatewayexclusioninput): {{String}}
  [ElasticFileSystemExclusionInput](#cfn-ec2-vpcencryptioncontrol-elasticfilesystemexclusioninput): {{String}}
  [InternetGatewayExclusionInput](#cfn-ec2-vpcencryptioncontrol-internetgatewayexclusioninput): {{String}}
  [LambdaExclusionInput](#cfn-ec2-vpcencryptioncontrol-lambdaexclusioninput): {{String}}
  [Mode](#cfn-ec2-vpcencryptioncontrol-mode): {{String}}
  [NatGatewayExclusionInput](#cfn-ec2-vpcencryptioncontrol-natgatewayexclusioninput): {{String}}
  [Tags](#cfn-ec2-vpcencryptioncontrol-tags): {{
    - Tag}}
  [VirtualPrivateGatewayExclusionInput](#cfn-ec2-vpcencryptioncontrol-virtualprivategatewayexclusioninput): {{String}}
  [VpcId](#cfn-ec2-vpcencryptioncontrol-vpcid): {{String}}
  [VpcLatticeExclusionInput](#cfn-ec2-vpcencryptioncontrol-vpclatticeexclusioninput): {{String}}
  [VpcPeeringExclusionInput](#cfn-ec2-vpcencryptioncontrol-vpcpeeringexclusioninput): {{String}}
```

## Properties
<a name="aws-resource-ec2-vpcencryptioncontrol-properties"></a>

`EgressOnlyInternetGatewayExclusionInput`  <a name="cfn-ec2-vpcencryptioncontrol-egressonlyinternetgatewayexclusioninput"></a>
Specifies whether to exclude egress-only internet gateway traffic from encryption enforcement.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ElasticFileSystemExclusionInput`  <a name="cfn-ec2-vpcencryptioncontrol-elasticfilesystemexclusioninput"></a>
Specifies whether to exclude Elastic File System traffic from encryption enforcement.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InternetGatewayExclusionInput`  <a name="cfn-ec2-vpcencryptioncontrol-internetgatewayexclusioninput"></a>
Specifies whether to exclude internet gateway traffic from encryption enforcement.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LambdaExclusionInput`  <a name="cfn-ec2-vpcencryptioncontrol-lambdaexclusioninput"></a>
Specifies whether to exclude Lambda function traffic from encryption enforcement.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-ec2-vpcencryptioncontrol-mode"></a>
The encryption mode for the VPC Encryption Control configuration.
*Required*: No
*Type*: String
*Allowed values*: `monitor | enforce`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NatGatewayExclusionInput`  <a name="cfn-ec2-vpcencryptioncontrol-natgatewayexclusioninput"></a>
Specifies whether to exclude NAT gateway traffic from encryption enforcement.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-vpcencryptioncontrol-tags"></a>
The tags assigned to the VPC Encryption Control configuration.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-vpcencryptioncontrol-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VirtualPrivateGatewayExclusionInput`  <a name="cfn-ec2-vpcencryptioncontrol-virtualprivategatewayexclusioninput"></a>
Specifies whether to exclude virtual private gateway traffic from encryption enforcement.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-ec2-vpcencryptioncontrol-vpcid"></a>
The ID of the VPC for which to create the encryption control configuration.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcLatticeExclusionInput`  <a name="cfn-ec2-vpcencryptioncontrol-vpclatticeexclusioninput"></a>
Specifies whether to exclude VPC Lattice traffic from encryption enforcement.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcPeeringExclusionInput`  <a name="cfn-ec2-vpcencryptioncontrol-vpcpeeringexclusioninput"></a>
Specifies whether to exclude VPC peering connection traffic from encryption enforcement.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-vpcencryptioncontrol-return-values"></a>

### Ref
<a name="aws-resource-ec2-vpcencryptioncontrol-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the VPC Encryption Control ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-vpcencryptioncontrol-return-values-fn--getatt"></a>

Describes the configuration and state of VPC encryption controls.

For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.

####
<a name="aws-resource-ec2-vpcencryptioncontrol-return-values-fn--getatt-fn--getatt"></a>

`ResourceExclusions.EgressOnlyInternetGateway.State`  <a name="ResourceExclusions.EgressOnlyInternetGateway.State-fn::getatt"></a>
The current state of the exclusion configuration.

`ResourceExclusions.EgressOnlyInternetGateway.StateMessage`  <a name="ResourceExclusions.EgressOnlyInternetGateway.StateMessage-fn::getatt"></a>
A message providing additional information about the exclusion state.

`ResourceExclusions.ElasticFileSystem.State`  <a name="ResourceExclusions.ElasticFileSystem.State-fn::getatt"></a>
The current state of the exclusion configuration.

`ResourceExclusions.ElasticFileSystem.StateMessage`  <a name="ResourceExclusions.ElasticFileSystem.StateMessage-fn::getatt"></a>
A message providing additional information about the exclusion state.

`ResourceExclusions.InternetGateway.State`  <a name="ResourceExclusions.InternetGateway.State-fn::getatt"></a>
The current state of the exclusion configuration.

`ResourceExclusions.InternetGateway.StateMessage`  <a name="ResourceExclusions.InternetGateway.StateMessage-fn::getatt"></a>
A message providing additional information about the exclusion state.

`ResourceExclusions.Lambda.State`  <a name="ResourceExclusions.Lambda.State-fn::getatt"></a>
The current state of the exclusion configuration.

`ResourceExclusions.Lambda.StateMessage`  <a name="ResourceExclusions.Lambda.StateMessage-fn::getatt"></a>
A message providing additional information about the exclusion state.

`ResourceExclusions.NatGateway.State`  <a name="ResourceExclusions.NatGateway.State-fn::getatt"></a>
The current state of the exclusion configuration.

`ResourceExclusions.NatGateway.StateMessage`  <a name="ResourceExclusions.NatGateway.StateMessage-fn::getatt"></a>
A message providing additional information about the exclusion state.

`ResourceExclusions.VirtualPrivateGateway.State`  <a name="ResourceExclusions.VirtualPrivateGateway.State-fn::getatt"></a>
The current state of the exclusion configuration.

`ResourceExclusions.VirtualPrivateGateway.StateMessage`  <a name="ResourceExclusions.VirtualPrivateGateway.StateMessage-fn::getatt"></a>
A message providing additional information about the exclusion state.

`ResourceExclusions.VpcLattice.State`  <a name="ResourceExclusions.VpcLattice.State-fn::getatt"></a>
The current state of the exclusion configuration.

`ResourceExclusions.VpcLattice.StateMessage`  <a name="ResourceExclusions.VpcLattice.StateMessage-fn::getatt"></a>
A message providing additional information about the exclusion state.

`ResourceExclusions.VpcPeering.State`  <a name="ResourceExclusions.VpcPeering.State-fn::getatt"></a>
The current state of the exclusion configuration.

`ResourceExclusions.VpcPeering.StateMessage`  <a name="ResourceExclusions.VpcPeering.StateMessage-fn::getatt"></a>
A message providing additional information about the exclusion state.

`State`  <a name="State-fn::getatt"></a>
The current state of the VPC Encryption Control configuration.

`StateMessage`  <a name="StateMessage-fn::getatt"></a>
A message providing additional information about the encryption control state.

`VpcEncryptionControlId`  <a name="VpcEncryptionControlId-fn::getatt"></a>
The ID of the VPC Encryption Control configuration.
