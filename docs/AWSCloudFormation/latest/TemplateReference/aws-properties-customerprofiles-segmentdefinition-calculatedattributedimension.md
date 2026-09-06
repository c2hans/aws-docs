---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-segmentdefinition-calculatedattributedimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition CalculatedAttributeDimension
<a name="aws-properties-customerprofiles-segmentdefinition-calculatedattributedimension"></a>

Object that segments on Customer Profile's Calculated Attributes.

## Syntax
<a name="aws-properties-customerprofiles-segmentdefinition-calculatedattributedimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-segmentdefinition-calculatedattributedimension-syntax.json"></a>

```
{
  "[ConditionOverrides](#cfn-customerprofiles-segmentdefinition-calculatedattributedimension-conditionoverrides)" : {{ConditionOverrides}},
  "[DimensionType](#cfn-customerprofiles-segmentdefinition-calculatedattributedimension-dimensiontype)" : {{String}},
  "[Values](#cfn-customerprofiles-segmentdefinition-calculatedattributedimension-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-segmentdefinition-calculatedattributedimension-syntax.yaml"></a>

```
  [ConditionOverrides](#cfn-customerprofiles-segmentdefinition-calculatedattributedimension-conditionoverrides): {{
    ConditionOverrides}}
  [DimensionType](#cfn-customerprofiles-segmentdefinition-calculatedattributedimension-dimensiontype): {{String}}
  [Values](#cfn-customerprofiles-segmentdefinition-calculatedattributedimension-values): {{
    - String}}
```

## Properties
<a name="aws-properties-customerprofiles-segmentdefinition-calculatedattributedimension-properties"></a>

`ConditionOverrides`  <a name="cfn-customerprofiles-segmentdefinition-calculatedattributedimension-conditionoverrides"></a>
Applies the given condition over the initial Calculated Attribute's definition.
*Required*: No
*Type*: [ConditionOverrides](aws-properties-customerprofiles-segmentdefinition-conditionoverrides.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DimensionType`  <a name="cfn-customerprofiles-segmentdefinition-calculatedattributedimension-dimensiontype"></a>
The action to segment with.
*Required*: Yes
*Type*: String
*Allowed values*: `INCLUSIVE | EXCLUSIVE | CONTAINS | BEGINS_WITH | ENDS_WITH | BEFORE | AFTER | BETWEEN | NOT_BETWEEN | ON | GREATER_THAN | LESS_THAN | GREATER_THAN_OR_EQUAL | LESS_THAN_OR_EQUAL | EQUAL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Values`  <a name="cfn-customerprofiles-segmentdefinition-calculatedattributedimension-values"></a>
The values to apply the DimensionType with.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
