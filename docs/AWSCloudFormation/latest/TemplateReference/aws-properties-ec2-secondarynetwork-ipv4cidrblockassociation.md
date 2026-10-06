---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-secondarynetwork-ipv4cidrblockassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SecondaryNetwork Ipv4CidrBlockAssociation
<a name="aws-properties-ec2-secondarynetwork-ipv4cidrblockassociation"></a>

<a name="aws-properties-ec2-secondarynetwork-ipv4cidrblockassociation-description"></a>The `Ipv4CidrBlockAssociation` property type specifies Property description not available. for an [AWS::EC2::SecondaryNetwork](aws-resource-ec2-secondarynetwork.md).

## Syntax
<a name="aws-properties-ec2-secondarynetwork-ipv4cidrblockassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-secondarynetwork-ipv4cidrblockassociation-syntax.json"></a>

```
{
  "[AssociationId](#cfn-ec2-secondarynetwork-ipv4cidrblockassociation-associationid)" : {{String}},
  "[CidrBlock](#cfn-ec2-secondarynetwork-ipv4cidrblockassociation-cidrblock)" : {{String}},
  "[State](#cfn-ec2-secondarynetwork-ipv4cidrblockassociation-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-secondarynetwork-ipv4cidrblockassociation-syntax.yaml"></a>

```
  [AssociationId](#cfn-ec2-secondarynetwork-ipv4cidrblockassociation-associationid): {{String}}
  [CidrBlock](#cfn-ec2-secondarynetwork-ipv4cidrblockassociation-cidrblock): {{String}}
  [State](#cfn-ec2-secondarynetwork-ipv4cidrblockassociation-state): {{String}}
```

## Properties
<a name="aws-properties-ec2-secondarynetwork-ipv4cidrblockassociation-properties"></a>

`AssociationId`  <a name="cfn-ec2-secondarynetwork-ipv4cidrblockassociation-associationid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CidrBlock`  <a name="cfn-ec2-secondarynetwork-ipv4cidrblockassociation-cidrblock"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-ec2-secondarynetwork-ipv4cidrblockassociation-state"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `associating | associated | association-failed | disassociating | disassociated | disassociation-failed`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
