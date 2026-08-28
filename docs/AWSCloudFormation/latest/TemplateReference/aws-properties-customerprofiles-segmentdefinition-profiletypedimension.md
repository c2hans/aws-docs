---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-segmentdefinition-profiletypedimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition ProfileTypeDimension
<a name="aws-properties-customerprofiles-segmentdefinition-profiletypedimension"></a>

Specifies profile type based criteria for a segment.

## Syntax
<a name="aws-properties-customerprofiles-segmentdefinition-profiletypedimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-segmentdefinition-profiletypedimension-syntax.json"></a>

```
{
  "[DimensionType](#cfn-customerprofiles-segmentdefinition-profiletypedimension-dimensiontype)" : {{String}},
  "[Values](#cfn-customerprofiles-segmentdefinition-profiletypedimension-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-segmentdefinition-profiletypedimension-syntax.yaml"></a>

```
  [DimensionType](#cfn-customerprofiles-segmentdefinition-profiletypedimension-dimensiontype): {{String}}
  [Values](#cfn-customerprofiles-segmentdefinition-profiletypedimension-values): {{
    - String}}
```

## Properties
<a name="aws-properties-customerprofiles-segmentdefinition-profiletypedimension-properties"></a>

`DimensionType`  <a name="cfn-customerprofiles-segmentdefinition-profiletypedimension-dimensiontype"></a>
The action to segment on.
*Required*: Yes
*Type*: String
*Allowed values*: `INCLUSIVE | EXCLUSIVE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Values`  <a name="cfn-customerprofiles-segmentdefinition-profiletypedimension-values"></a>
The values to apply the DimensionType on.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
