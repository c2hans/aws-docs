---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gameliftstreams-streamgroup-vpctransitconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLiftStreams::StreamGroup VpcTransitConfiguration
<a name="aws-properties-gameliftstreams-streamgroup-vpctransitconfiguration"></a>

Configuration for connecting a stream group location to resources in your Amazon VPC using a Transit Gateway. When you specify a VPC transit configuration, Amazon GameLift Streams creates a Transit Gateway and shares it with your account using Resource Access Manager. After the stream group is active, you must complete the setup by accepting the resource share, creating a VPC attachment, and configuring routing.

## Syntax
<a name="aws-properties-gameliftstreams-streamgroup-vpctransitconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gameliftstreams-streamgroup-vpctransitconfiguration-syntax.json"></a>

```
{
  "[Ipv4CidrBlocks](#cfn-gameliftstreams-streamgroup-vpctransitconfiguration-ipv4cidrblocks)" : {{[ String, ... ]}},
  "[VpcId](#cfn-gameliftstreams-streamgroup-vpctransitconfiguration-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-gameliftstreams-streamgroup-vpctransitconfiguration-syntax.yaml"></a>

```
  [Ipv4CidrBlocks](#cfn-gameliftstreams-streamgroup-vpctransitconfiguration-ipv4cidrblocks): {{
    - String}}
  [VpcId](#cfn-gameliftstreams-streamgroup-vpctransitconfiguration-vpcid): {{String}}
```

## Properties
<a name="aws-properties-gameliftstreams-streamgroup-vpctransitconfiguration-properties"></a>

`Ipv4CidrBlocks`  <a name="cfn-gameliftstreams-streamgroup-vpctransitconfiguration-ipv4cidrblocks"></a>
A list of IPv4 CIDR blocks in your VPC that you want the stream group to be able to access. You can specify up to 5 CIDR blocks. The CIDR blocks must be valid subsets of the VPC's CIDR blocks and cannot overlap with the service VPC CIDR block.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-gameliftstreams-streamgroup-vpctransitconfiguration-vpcid"></a>
The ID of the Amazon VPC that you want to connect to the stream group. The VPC must be in the same AWS account as the stream group. This value cannot be changed after the stream group is created.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
