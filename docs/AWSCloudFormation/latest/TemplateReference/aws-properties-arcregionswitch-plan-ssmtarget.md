---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-ssmtarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan SsmTarget
<a name="aws-properties-arcregionswitch-plan-ssmtarget"></a>

A single `SendCommand` target filter, consisting of a target key and the values matched by that key.

## Syntax
<a name="aws-properties-arcregionswitch-plan-ssmtarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-ssmtarget-syntax.json"></a>

```
{
  "[Key](#cfn-arcregionswitch-plan-ssmtarget-key)" : {{String}},
  "[Values](#cfn-arcregionswitch-plan-ssmtarget-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-ssmtarget-syntax.yaml"></a>

```
  [Key](#cfn-arcregionswitch-plan-ssmtarget-key): {{String}}
  [Values](#cfn-arcregionswitch-plan-ssmtarget-values): {{
    - String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-ssmtarget-properties"></a>

`Key`  <a name="cfn-arcregionswitch-plan-ssmtarget-key"></a>
The target key, such as `tag:Environment` or `InstanceIds`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{Z}\p{N}_.:/=\-@]*$`
*Minimum*: `1`
*Maximum*: `163`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-arcregionswitch-plan-ssmtarget-values"></a>
The values matched by this target key. Multiple values combine with a logical OR.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `256 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
