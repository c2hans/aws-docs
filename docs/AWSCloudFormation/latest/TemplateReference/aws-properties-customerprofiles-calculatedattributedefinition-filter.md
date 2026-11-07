---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-calculatedattributedefinition-filter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::CalculatedAttributeDefinition Filter
<a name="aws-properties-customerprofiles-calculatedattributedefinition-filter"></a>

<a name="aws-properties-customerprofiles-calculatedattributedefinition-filter-description"></a>The `Filter` property type specifies Property description not available. for an [AWS::CustomerProfiles::CalculatedAttributeDefinition](aws-resource-customerprofiles-calculatedattributedefinition.md).

## Syntax
<a name="aws-properties-customerprofiles-calculatedattributedefinition-filter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-calculatedattributedefinition-filter-syntax.json"></a>

```
{
  "[Groups](#cfn-customerprofiles-calculatedattributedefinition-filter-groups)" : {{[ FilterGroup, ... ]}},
  "[Include](#cfn-customerprofiles-calculatedattributedefinition-filter-include)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-calculatedattributedefinition-filter-syntax.yaml"></a>

```
  [Groups](#cfn-customerprofiles-calculatedattributedefinition-filter-groups): {{
    - FilterGroup}}
  [Include](#cfn-customerprofiles-calculatedattributedefinition-filter-include): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-calculatedattributedefinition-filter-properties"></a>

`Groups`  <a name="cfn-customerprofiles-calculatedattributedefinition-filter-groups"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [FilterGroup](aws-properties-customerprofiles-calculatedattributedefinition-filtergroup.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Include`  <a name="cfn-customerprofiles-calculatedattributedefinition-filter-include"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ALL | ANY | NONE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
