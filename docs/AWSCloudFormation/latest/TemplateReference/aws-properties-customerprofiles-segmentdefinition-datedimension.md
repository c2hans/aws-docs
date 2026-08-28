---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-segmentdefinition-datedimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition DateDimension
<a name="aws-properties-customerprofiles-segmentdefinition-datedimension"></a>

Object that segments on various Customer Profile's date fields.

## Syntax
<a name="aws-properties-customerprofiles-segmentdefinition-datedimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-segmentdefinition-datedimension-syntax.json"></a>

```
{
  "[DimensionType](#cfn-customerprofiles-segmentdefinition-datedimension-dimensiontype)" : {{String}},
  "[Values](#cfn-customerprofiles-segmentdefinition-datedimension-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-segmentdefinition-datedimension-syntax.yaml"></a>

```
  [DimensionType](#cfn-customerprofiles-segmentdefinition-datedimension-dimensiontype): {{String}}
  [Values](#cfn-customerprofiles-segmentdefinition-datedimension-values): {{
    - String}}
```

## Properties
<a name="aws-properties-customerprofiles-segmentdefinition-datedimension-properties"></a>

`DimensionType`  <a name="cfn-customerprofiles-segmentdefinition-datedimension-dimensiontype"></a>
The action to segment on.
*Required*: Yes
*Type*: String
*Allowed values*: `BEFORE | AFTER | BETWEEN | NOT_BETWEEN | ON`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Values`  <a name="cfn-customerprofiles-segmentdefinition-datedimension-values"></a>
The values to apply the DimensionType on.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
