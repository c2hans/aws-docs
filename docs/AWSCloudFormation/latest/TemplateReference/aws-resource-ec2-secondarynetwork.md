---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-secondarynetwork.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SecondaryNetwork
<a name="aws-resource-ec2-secondarynetwork"></a>

Describes a secondary network.

## Syntax
<a name="aws-resource-ec2-secondarynetwork-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-secondarynetwork-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::SecondaryNetwork",
  "Properties" : {
      "[Ipv4CidrBlock](#cfn-ec2-secondarynetwork-ipv4cidrblock)" : {{String}},
      "[NetworkType](#cfn-ec2-secondarynetwork-networktype)" : {{String}},
      "[Tags](#cfn-ec2-secondarynetwork-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-secondarynetwork-syntax.yaml"></a>

```
Type: AWS::EC2::SecondaryNetwork
Properties:
  [Ipv4CidrBlock](#cfn-ec2-secondarynetwork-ipv4cidrblock): {{String}}
  [NetworkType](#cfn-ec2-secondarynetwork-networktype): {{String}}
  [Tags](#cfn-ec2-secondarynetwork-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-secondarynetwork-properties"></a>

`Ipv4CidrBlock`  <a name="cfn-ec2-secondarynetwork-ipv4cidrblock"></a>
Describes an IPv4 CIDR block.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkType`  <a name="cfn-ec2-secondarynetwork-networktype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `rdma`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-secondarynetwork-tags"></a>
The tags assigned to the secondary network.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-secondarynetwork-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-secondarynetwork-return-values"></a>

### Ref
<a name="aws-resource-ec2-secondarynetwork-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-secondarynetwork-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-secondarynetwork-return-values-fn--getatt-fn--getatt"></a>

`Ipv4CidrBlockAssociations`  <a name="Ipv4CidrBlockAssociations-fn::getatt"></a>
Information about the IPv4 CIDR blocks associated with the secondary network.

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
The ID of the AWS account that owns the secondary network.

`SecondaryNetworkArn`  <a name="SecondaryNetworkArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the secondary network.

`SecondaryNetworkId`  <a name="SecondaryNetworkId-fn::getatt"></a>
The ID of the secondary network.
