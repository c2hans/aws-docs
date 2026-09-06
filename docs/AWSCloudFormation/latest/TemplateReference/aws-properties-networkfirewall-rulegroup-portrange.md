---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-rulegroup-portrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::RuleGroup PortRange
<a name="aws-properties-networkfirewall-rulegroup-portrange"></a>

A single port range specification. This is used for source and destination port ranges in the stateless match attributes.

## Syntax
<a name="aws-properties-networkfirewall-rulegroup-portrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-rulegroup-portrange-syntax.json"></a>

```
{
  "[FromPort](#cfn-networkfirewall-rulegroup-portrange-fromport)" : {{Integer}},
  "[ToPort](#cfn-networkfirewall-rulegroup-portrange-toport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-networkfirewall-rulegroup-portrange-syntax.yaml"></a>

```
  [FromPort](#cfn-networkfirewall-rulegroup-portrange-fromport): {{Integer}}
  [ToPort](#cfn-networkfirewall-rulegroup-portrange-toport): {{Integer}}
```

## Properties
<a name="aws-properties-networkfirewall-rulegroup-portrange-properties"></a>

`FromPort`  <a name="cfn-networkfirewall-rulegroup-portrange-fromport"></a>
The lower limit of the port range. This must be less than or equal to the `ToPort` specification.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToPort`  <a name="cfn-networkfirewall-rulegroup-portrange-toport"></a>
The upper limit of the port range. This must be greater than or equal to the `FromPort` specification.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
