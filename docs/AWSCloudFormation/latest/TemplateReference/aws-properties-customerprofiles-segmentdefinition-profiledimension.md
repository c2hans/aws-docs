---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-segmentdefinition-profiledimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition ProfileDimension
<a name="aws-properties-customerprofiles-segmentdefinition-profiledimension"></a>

Object that segments on various Customer profile's fields that are larger than normal.

## Syntax
<a name="aws-properties-customerprofiles-segmentdefinition-profiledimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-segmentdefinition-profiledimension-syntax.json"></a>

```
{
  "[DimensionType](#cfn-customerprofiles-segmentdefinition-profiledimension-dimensiontype)" : {{String}},
  "[Values](#cfn-customerprofiles-segmentdefinition-profiledimension-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-segmentdefinition-profiledimension-syntax.yaml"></a>

```
  [DimensionType](#cfn-customerprofiles-segmentdefinition-profiledimension-dimensiontype): {{String}}
  [Values](#cfn-customerprofiles-segmentdefinition-profiledimension-values): {{
    - String}}
```

## Properties
<a name="aws-properties-customerprofiles-segmentdefinition-profiledimension-properties"></a>

`DimensionType`  <a name="cfn-customerprofiles-segmentdefinition-profiledimension-dimensiontype"></a>
The action to segment on.
*Required*: Yes
*Type*: String
*Allowed values*: `INCLUSIVE | EXCLUSIVE | CONTAINS | BEGINS_WITH | ENDS_WITH`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Values`  <a name="cfn-customerprofiles-segmentdefinition-profiledimension-values"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
