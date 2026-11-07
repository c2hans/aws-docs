---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-calculatedattributedefinition-filtergroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::CalculatedAttributeDefinition FilterGroup
<a name="aws-properties-customerprofiles-calculatedattributedefinition-filtergroup"></a>

<a name="aws-properties-customerprofiles-calculatedattributedefinition-filtergroup-description"></a>The `FilterGroup` property type specifies Property description not available. for an [AWS::CustomerProfiles::CalculatedAttributeDefinition](aws-resource-customerprofiles-calculatedattributedefinition.md).

## Syntax
<a name="aws-properties-customerprofiles-calculatedattributedefinition-filtergroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-calculatedattributedefinition-filtergroup-syntax.json"></a>

```
{
  "[Dimensions](#cfn-customerprofiles-calculatedattributedefinition-filtergroup-dimensions)" : {{[ FilterDimension, ... ]}},
  "[Type](#cfn-customerprofiles-calculatedattributedefinition-filtergroup-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-calculatedattributedefinition-filtergroup-syntax.yaml"></a>

```
  [Dimensions](#cfn-customerprofiles-calculatedattributedefinition-filtergroup-dimensions): {{
    - FilterDimension}}
  [Type](#cfn-customerprofiles-calculatedattributedefinition-filtergroup-type): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-calculatedattributedefinition-filtergroup-properties"></a>

`Dimensions`  <a name="cfn-customerprofiles-calculatedattributedefinition-filtergroup-dimensions"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [FilterDimension](aws-properties-customerprofiles-calculatedattributedefinition-filterdimension.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-customerprofiles-calculatedattributedefinition-filtergroup-type"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ALL | ANY | NONE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
