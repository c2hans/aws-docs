---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-custompermissions-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::CustomPermissions Tag
<a name="aws-properties-quicksight-custompermissions-tag"></a>

The tags to associate with the custom permissions profile.

## Syntax
<a name="aws-properties-quicksight-custompermissions-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-custompermissions-tag-syntax.json"></a>

```
{
  "[Key](#cfn-quicksight-custompermissions-tag-key)" : {{String}},
  "[Value](#cfn-quicksight-custompermissions-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-custompermissions-tag-syntax.yaml"></a>

```
  [Key](#cfn-quicksight-custompermissions-tag-key): {{String}}
  [Value](#cfn-quicksight-custompermissions-tag-value): {{String}}
```

## Properties
<a name="aws-properties-quicksight-custompermissions-tag-properties"></a>

`Key`  <a name="cfn-quicksight-custompermissions-tag-key"></a>
The unique key for a tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-custompermissions-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
