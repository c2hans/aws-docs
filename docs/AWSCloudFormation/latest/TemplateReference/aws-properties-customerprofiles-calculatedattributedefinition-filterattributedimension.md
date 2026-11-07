---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-calculatedattributedefinition-filterattributedimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::CalculatedAttributeDefinition FilterAttributeDimension
<a name="aws-properties-customerprofiles-calculatedattributedefinition-filterattributedimension"></a>

<a name="aws-properties-customerprofiles-calculatedattributedefinition-filterattributedimension-description"></a>The `FilterAttributeDimension` property type specifies Property description not available. for an [AWS::CustomerProfiles::CalculatedAttributeDefinition](aws-resource-customerprofiles-calculatedattributedefinition.md).

## Syntax
<a name="aws-properties-customerprofiles-calculatedattributedefinition-filterattributedimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-calculatedattributedefinition-filterattributedimension-syntax.json"></a>

```
{
  "[DimensionType](#cfn-customerprofiles-calculatedattributedefinition-filterattributedimension-dimensiontype)" : {{String}},
  "[Values](#cfn-customerprofiles-calculatedattributedefinition-filterattributedimension-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-calculatedattributedefinition-filterattributedimension-syntax.yaml"></a>

```
  [DimensionType](#cfn-customerprofiles-calculatedattributedefinition-filterattributedimension-dimensiontype): {{String}}
  [Values](#cfn-customerprofiles-calculatedattributedefinition-filterattributedimension-values): {{
    - String}}
```

## Properties
<a name="aws-properties-customerprofiles-calculatedattributedefinition-filterattributedimension-properties"></a>

`DimensionType`  <a name="cfn-customerprofiles-calculatedattributedefinition-filterattributedimension-dimensiontype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `INCLUSIVE | EXCLUSIVE | CONTAINS | BEGINS_WITH | ENDS_WITH | BEFORE | AFTER | BETWEEN | NOT_BETWEEN | ON | GREATER_THAN | LESS_THAN | GREATER_THAN_OR_EQUAL | LESS_THAN_OR_EQUAL | EQUAL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Values`  <a name="cfn-customerprofiles-calculatedattributedefinition-filterattributedimension-values"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
