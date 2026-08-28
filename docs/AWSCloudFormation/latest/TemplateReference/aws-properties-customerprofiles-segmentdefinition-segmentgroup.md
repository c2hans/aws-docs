---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-segmentdefinition-segmentgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition SegmentGroup
<a name="aws-properties-customerprofiles-segmentdefinition-segmentgroup"></a>

Contains all groups of the segment definition.

## Syntax
<a name="aws-properties-customerprofiles-segmentdefinition-segmentgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-segmentdefinition-segmentgroup-syntax.json"></a>

```
{
  "[Groups](#cfn-customerprofiles-segmentdefinition-segmentgroup-groups)" : {{[ Group, ... ]}},
  "[Include](#cfn-customerprofiles-segmentdefinition-segmentgroup-include)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-segmentdefinition-segmentgroup-syntax.yaml"></a>

```
  [Groups](#cfn-customerprofiles-segmentdefinition-segmentgroup-groups): {{
    - Group}}
  [Include](#cfn-customerprofiles-segmentdefinition-segmentgroup-include): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-segmentdefinition-segmentgroup-properties"></a>

`Groups`  <a name="cfn-customerprofiles-segmentdefinition-segmentgroup-groups"></a>
Holds the list of groups within the segment definition.
*Required*: No
*Type*: Array of [Group](aws-properties-customerprofiles-segmentdefinition-group.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Include`  <a name="cfn-customerprofiles-segmentdefinition-segmentgroup-include"></a>
Defines whether to include or exclude the profiles that fit the segment criteria.
*Required*: No
*Type*: String
*Allowed values*: `ALL | ANY | NONE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
