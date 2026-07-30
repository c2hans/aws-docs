---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-layout-fieldgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::Layout FieldGroup
<a name="aws-properties-cases-layout-fieldgroup"></a>

Object for a group of fields and associated properties.

## Syntax
<a name="aws-properties-cases-layout-fieldgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-layout-fieldgroup-syntax.json"></a>

```
{
  "[Fields](#cfn-cases-layout-fieldgroup-fields)" : {{[ FieldItem, ... ]}},
  "[Name](#cfn-cases-layout-fieldgroup-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-cases-layout-fieldgroup-syntax.yaml"></a>

```
  [Fields](#cfn-cases-layout-fieldgroup-fields): {{
    - FieldItem}}
  [Name](#cfn-cases-layout-fieldgroup-name): {{String}}
```

## Properties
<a name="aws-properties-cases-layout-fieldgroup-properties"></a>

`Fields`  <a name="cfn-cases-layout-fieldgroup-fields"></a>
Represents an ordered list containing field related information.
*Required*: Yes
*Type*: Array of [FieldItem](aws-properties-cases-layout-fielditem.md)
*Maximum*: `220`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cases-layout-fieldgroup-name"></a>
Name of the field group.
*Required*: No
*Type*: String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
