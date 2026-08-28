---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-segment-segmentgroups.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Segment SegmentGroups
<a name="aws-properties-pinpoint-segment-segmentgroups"></a>

Specifies the set of segment criteria to evaluate when handling segment groups for the segment.

## Syntax
<a name="aws-properties-pinpoint-segment-segmentgroups-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-segment-segmentgroups-syntax.json"></a>

```
{
  "[Groups](#cfn-pinpoint-segment-segmentgroups-groups)" : {{[ Groups, ... ]}},
  "[Include](#cfn-pinpoint-segment-segmentgroups-include)" : {{String}}
}
```

### YAML
<a name="aws-properties-pinpoint-segment-segmentgroups-syntax.yaml"></a>

```
  [Groups](#cfn-pinpoint-segment-segmentgroups-groups): {{
    - Groups}}
  [Include](#cfn-pinpoint-segment-segmentgroups-include): {{String}}
```

## Properties
<a name="aws-properties-pinpoint-segment-segmentgroups-properties"></a>

`Groups`  <a name="cfn-pinpoint-segment-segmentgroups-groups"></a>
Specifies the set of segment criteria to evaluate when handling segment groups for the segment.
*Required*: No
*Type*: [Array](aws-properties-pinpoint-segment-groups.md) of [Groups](aws-properties-pinpoint-segment-groups.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Include`  <a name="cfn-pinpoint-segment-segmentgroups-include"></a>
Specifies how to handle multiple segment groups for the segment. For example, if the segment includes three segment groups, whether the resulting segment includes endpoints that match all, any, or none of the segment groups.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
