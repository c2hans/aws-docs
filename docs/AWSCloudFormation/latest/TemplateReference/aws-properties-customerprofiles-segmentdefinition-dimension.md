---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-segmentdefinition-dimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition Dimension
<a name="aws-properties-customerprofiles-segmentdefinition-dimension"></a>

Defines the attribute to segment on.

## Syntax
<a name="aws-properties-customerprofiles-segmentdefinition-dimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-segmentdefinition-dimension-syntax.json"></a>

```
{
  "[CalculatedAttributes](#cfn-customerprofiles-segmentdefinition-dimension-calculatedattributes)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ProfileAttributes](#cfn-customerprofiles-segmentdefinition-dimension-profileattributes)" : {{ProfileAttributes}}
}
```

### YAML
<a name="aws-properties-customerprofiles-segmentdefinition-dimension-syntax.yaml"></a>

```
  [CalculatedAttributes](#cfn-customerprofiles-segmentdefinition-dimension-calculatedattributes): {{
    {{Key}}: {{Value}}}}
  [ProfileAttributes](#cfn-customerprofiles-segmentdefinition-dimension-profileattributes): {{
    ProfileAttributes}}
```

## Properties
<a name="aws-properties-customerprofiles-segmentdefinition-dimension-properties"></a>

`CalculatedAttributes`  <a name="cfn-customerprofiles-segmentdefinition-dimension-calculatedattributes"></a>
Object that holds the calculated attributes to segment on.
*Required*: No
*Type*: Object of [CalculatedAttributeDimension](aws-properties-customerprofiles-segmentdefinition-calculatedattributedimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProfileAttributes`  <a name="cfn-customerprofiles-segmentdefinition-dimension-profileattributes"></a>
Object that holds the profile attributes to segment on.
*Required*: No
*Type*: [ProfileAttributes](aws-properties-customerprofiles-segmentdefinition-profileattributes.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
