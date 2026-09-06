---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fms-policy-portrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FMS::Policy PortRange
<a name="aws-properties-fms-policy-portrange"></a>

TCP or UDP protocols: The range of ports the rule applies to.

## Syntax
<a name="aws-properties-fms-policy-portrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fms-policy-portrange-syntax.json"></a>

```
{
  "[From](#cfn-fms-policy-portrange-from)" : {{Integer}},
  "[To](#cfn-fms-policy-portrange-to)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-fms-policy-portrange-syntax.yaml"></a>

```
  [From](#cfn-fms-policy-portrange-from): {{Integer}}
  [To](#cfn-fms-policy-portrange-to): {{Integer}}
```

## Properties
<a name="aws-properties-fms-policy-portrange-properties"></a>

`From`  <a name="cfn-fms-policy-portrange-from"></a>
The beginning port number of the range.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`To`  <a name="cfn-fms-policy-portrange-to"></a>
The ending port number of the range.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
