---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-calculatedattributedefinition-attributeitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::CalculatedAttributeDefinition AttributeItem
<a name="aws-properties-customerprofiles-calculatedattributedefinition-attributeitem"></a>

The details of a single attribute item specified in the mathematical expression.

## Syntax
<a name="aws-properties-customerprofiles-calculatedattributedefinition-attributeitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-calculatedattributedefinition-attributeitem-syntax.json"></a>

```
{
  "[Name](#cfn-customerprofiles-calculatedattributedefinition-attributeitem-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-calculatedattributedefinition-attributeitem-syntax.yaml"></a>

```
  [Name](#cfn-customerprofiles-calculatedattributedefinition-attributeitem-name): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-calculatedattributedefinition-attributeitem-properties"></a>

`Name`  <a name="cfn-customerprofiles-calculatedattributedefinition-attributeitem-name"></a>
The unique name of the calculated attribute.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
