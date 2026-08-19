---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayPolicyTableEntry TransitGatewayPolicyRule
<a name="aws-properties-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule"></a>

Describes a rule associated with a transit gateway policy.

## Syntax
<a name="aws-properties-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-syntax.json"></a>

```
{
  "[DestinationCidrBlock](#cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-destinationcidrblock)" : {{String}},
  "[DestinationPortRange](#cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-destinationportrange)" : {{String}},
  "[Protocol](#cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-protocol)" : {{String}},
  "[SourceCidrBlock](#cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-sourcecidrblock)" : {{String}},
  "[SourcePortRange](#cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-sourceportrange)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-syntax.yaml"></a>

```
  [DestinationCidrBlock](#cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-destinationcidrblock): {{String}}
  [DestinationPortRange](#cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-destinationportrange): {{String}}
  [Protocol](#cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-protocol): {{String}}
  [SourceCidrBlock](#cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-sourcecidrblock): {{String}}
  [SourcePortRange](#cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-sourceportrange): {{String}}
```

## Properties
<a name="aws-properties-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-properties"></a>

`DestinationCidrBlock`  <a name="cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-destinationcidrblock"></a>
The destination CIDR block for the transit gateway policy rule.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationPortRange`  <a name="cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-destinationportrange"></a>
The destination port or port range for the transit gateway policy rule.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-protocol"></a>
The protocol used by the transit gateway policy rule.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceCidrBlock`  <a name="cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-sourcecidrblock"></a>
The source CIDR block for the transit gateway policy rule.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourcePortRange`  <a name="cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule-sourceportrange"></a>
The source port or port range for the transit gateway policy rule.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
