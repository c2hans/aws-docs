---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-controltower-enabledbaseline-parameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ControlTower::EnabledBaseline Parameter
<a name="aws-properties-controltower-enabledbaseline-parameter"></a>

A key-value pair that specifies a parameter for the baseline configuration.

## Syntax
<a name="aws-properties-controltower-enabledbaseline-parameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-controltower-enabledbaseline-parameter-syntax.json"></a>

```
{
  "[Key](#cfn-controltower-enabledbaseline-parameter-key)" : {{String}},
  "[Value](#cfn-controltower-enabledbaseline-parameter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-controltower-enabledbaseline-parameter-syntax.yaml"></a>

```
  [Key](#cfn-controltower-enabledbaseline-parameter-key): {{String}}
  [Value](#cfn-controltower-enabledbaseline-parameter-value): {{String}}
```

## Properties
<a name="aws-properties-controltower-enabledbaseline-parameter-properties"></a>

`Key`  <a name="cfn-controltower-enabledbaseline-parameter-key"></a>
The key name of the parameter. You can specify a value that identifies the parameter configuration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-controltower-enabledbaseline-parameter-value"></a>
The value of the parameter. The value can be of type array, string, number, object, or boolean.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
