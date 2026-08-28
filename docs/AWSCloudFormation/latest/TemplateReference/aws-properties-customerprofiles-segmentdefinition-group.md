---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-segmentdefinition-group.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition Group
<a name="aws-properties-customerprofiles-segmentdefinition-group"></a>

Contains dimensions that determine what to segment on.

## Syntax
<a name="aws-properties-customerprofiles-segmentdefinition-group-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-segmentdefinition-group-syntax.json"></a>

```
{
  "[Dimensions](#cfn-customerprofiles-segmentdefinition-group-dimensions)" : {{[ Dimension, ... ]}},
  "[SourceSegments](#cfn-customerprofiles-segmentdefinition-group-sourcesegments)" : {{[ SourceSegment, ... ]}},
  "[SourceType](#cfn-customerprofiles-segmentdefinition-group-sourcetype)" : {{String}},
  "[Type](#cfn-customerprofiles-segmentdefinition-group-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-segmentdefinition-group-syntax.yaml"></a>

```
  [Dimensions](#cfn-customerprofiles-segmentdefinition-group-dimensions): {{
    - Dimension}}
  [SourceSegments](#cfn-customerprofiles-segmentdefinition-group-sourcesegments): {{
    - SourceSegment}}
  [SourceType](#cfn-customerprofiles-segmentdefinition-group-sourcetype): {{String}}
  [Type](#cfn-customerprofiles-segmentdefinition-group-type): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-segmentdefinition-group-properties"></a>

`Dimensions`  <a name="cfn-customerprofiles-segmentdefinition-group-dimensions"></a>
Defines the attributes to segment on.
*Required*: No
*Type*: Array of [Dimension](aws-properties-customerprofiles-segmentdefinition-dimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceSegments`  <a name="cfn-customerprofiles-segmentdefinition-group-sourcesegments"></a>
Defines the starting source of data.
*Required*: No
*Type*: Array of [SourceSegment](aws-properties-customerprofiles-segmentdefinition-sourcesegment.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceType`  <a name="cfn-customerprofiles-segmentdefinition-group-sourcetype"></a>
Defines how to interact with the source data.
*Required*: No
*Type*: String
*Allowed values*: `ALL | ANY | NONE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-customerprofiles-segmentdefinition-group-type"></a>
Defines how to interact with the profiles found in the current filtering.
*Required*: No
*Type*: String
*Allowed values*: `ALL | ANY | NONE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
