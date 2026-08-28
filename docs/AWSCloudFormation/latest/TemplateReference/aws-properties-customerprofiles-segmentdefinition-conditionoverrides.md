---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-segmentdefinition-conditionoverrides.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition ConditionOverrides
<a name="aws-properties-customerprofiles-segmentdefinition-conditionoverrides"></a>

An object to override the original condition block of a calculated attribute.

## Syntax
<a name="aws-properties-customerprofiles-segmentdefinition-conditionoverrides-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-segmentdefinition-conditionoverrides-syntax.json"></a>

```
{
  "[Range](#cfn-customerprofiles-segmentdefinition-conditionoverrides-range)" : {{RangeOverride}}
}
```

### YAML
<a name="aws-properties-customerprofiles-segmentdefinition-conditionoverrides-syntax.yaml"></a>

```
  [Range](#cfn-customerprofiles-segmentdefinition-conditionoverrides-range): {{
    RangeOverride}}
```

## Properties
<a name="aws-properties-customerprofiles-segmentdefinition-conditionoverrides-properties"></a>

`Range`  <a name="cfn-customerprofiles-segmentdefinition-conditionoverrides-range"></a>
The relative time period over which data is included in the aggregation for this override.
*Required*: No
*Type*: [RangeOverride](aws-properties-customerprofiles-segmentdefinition-rangeoverride.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
