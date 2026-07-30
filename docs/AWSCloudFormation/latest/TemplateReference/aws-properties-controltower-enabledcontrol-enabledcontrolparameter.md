---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-controltower-enabledcontrol-enabledcontrolparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ControlTower::EnabledControl EnabledControlParameter
<a name="aws-properties-controltower-enabledcontrol-enabledcontrolparameter"></a>

A set of parameters that configure the behavior of the enabled control. Expressed as a key/value pair, where `Key` is of type `String` and `Value` is of type `Document`.

## Syntax
<a name="aws-properties-controltower-enabledcontrol-enabledcontrolparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-controltower-enabledcontrol-enabledcontrolparameter-syntax.json"></a>

```
{
  "[Key](#cfn-controltower-enabledcontrol-enabledcontrolparameter-key)" : {{String}},
  "[Value](#cfn-controltower-enabledcontrol-enabledcontrolparameter-value)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-controltower-enabledcontrol-enabledcontrolparameter-syntax.yaml"></a>

```
  [Key](#cfn-controltower-enabledcontrol-enabledcontrolparameter-key): {{String}}
  [Value](#cfn-controltower-enabledcontrol-enabledcontrolparameter-value): {{
    - String}}
```

## Properties
<a name="aws-properties-controltower-enabledcontrol-enabledcontrolparameter-properties"></a>

`Key`  <a name="cfn-controltower-enabledcontrol-enabledcontrolparameter-key"></a>
The key of a key/value pair. It is of type `string`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-controltower-enabledcontrol-enabledcontrolparameter-value"></a>
The value of a key/value pair. It can be of type `array`, `string`, `number`, `object`, or `boolean`. [Note: The *Type* field that follows may show a single type such as Number, which is only one possible type.]
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
