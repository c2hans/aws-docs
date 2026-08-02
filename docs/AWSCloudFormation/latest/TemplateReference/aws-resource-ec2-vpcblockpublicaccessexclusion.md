---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpcblockpublicaccessexclusion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPCBlockPublicAccessExclusion
<a name="aws-resource-ec2-vpcblockpublicaccessexclusion"></a>

Create a VPC Block Public Access (BPA) exclusion. A VPC BPA exclusion is a mode that can be applied to a single VPC or subnet that exempts it from the account’s BPA mode and will allow bidirectional or egress-only access. You can create BPA exclusions for VPCs and subnets even when BPA is not enabled on the account to ensure that there is no traffic disruption to the exclusions when VPC BPA is turned on. To learn more about VPC BPA, see [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) in the *Amazon VPC User Guide*.

## Syntax
<a name="aws-resource-ec2-vpcblockpublicaccessexclusion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-vpcblockpublicaccessexclusion-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::VPCBlockPublicAccessExclusion",
  "Properties" : {
      "[InternetGatewayExclusionMode](#cfn-ec2-vpcblockpublicaccessexclusion-internetgatewayexclusionmode)" : {{String}},
      "[SubnetId](#cfn-ec2-vpcblockpublicaccessexclusion-subnetid)" : {{String}},
      "[Tags](#cfn-ec2-vpcblockpublicaccessexclusion-tags)" : {{[ Tag, ... ]}},
      "[VpcId](#cfn-ec2-vpcblockpublicaccessexclusion-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-vpcblockpublicaccessexclusion-syntax.yaml"></a>

```
Type: AWS::EC2::VPCBlockPublicAccessExclusion
Properties:
  [InternetGatewayExclusionMode](#cfn-ec2-vpcblockpublicaccessexclusion-internetgatewayexclusionmode): {{String}}
  [SubnetId](#cfn-ec2-vpcblockpublicaccessexclusion-subnetid): {{String}}
  [Tags](#cfn-ec2-vpcblockpublicaccessexclusion-tags): {{
    - Tag}}
  [VpcId](#cfn-ec2-vpcblockpublicaccessexclusion-vpcid): {{String}}
```

## Properties
<a name="aws-resource-ec2-vpcblockpublicaccessexclusion-properties"></a>

`InternetGatewayExclusionMode`  <a name="cfn-ec2-vpcblockpublicaccessexclusion-internetgatewayexclusionmode"></a>
The desired VPC Block Public Access mode for a specific VPC or subnet exclusion.
+ `allow-bidirectional`: Allow all internet traffic to and from the excluded VPCs and subnets.
+ `allow-egress`: Allow outbound internet traffic from the excluded VPCs and subnets. Block inbound internet traffic to the excluded VPCs and subnets. Only applies when VPC Block Public Access is set to `block-bidirectional`.
*Required*: Yes
*Type*: String
*Allowed values*: `allow-bidirectional | allow-egress`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-ec2-vpcblockpublicaccessexclusion-subnetid"></a>
The ID of the subnet you want to exclude. Required only if you don't specify VpcId.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-vpcblockpublicaccessexclusion-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-vpcblockpublicaccessexclusion-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-ec2-vpcblockpublicaccessexclusion-vpcid"></a>
The ID of the VPC you want to exclude. Required only if you don't specify SubnetId.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-vpcblockpublicaccessexclusion-return-values"></a>

### Ref
<a name="aws-resource-ec2-vpcblockpublicaccessexclusion-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the exclusion.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-vpcblockpublicaccessexclusion-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-vpcblockpublicaccessexclusion-return-values-fn--getatt-fn--getatt"></a>

`ExclusionId`  <a name="ExclusionId-fn::getatt"></a>
The ID of the exclusion.
