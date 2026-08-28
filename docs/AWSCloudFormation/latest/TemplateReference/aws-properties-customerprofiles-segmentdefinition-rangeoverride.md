---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-segmentdefinition-rangeoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition RangeOverride
<a name="aws-properties-customerprofiles-segmentdefinition-rangeoverride"></a>

Overrides the original range on a calculated attribute definition.

## Syntax
<a name="aws-properties-customerprofiles-segmentdefinition-rangeoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-segmentdefinition-rangeoverride-syntax.json"></a>

```
{
  "[End](#cfn-customerprofiles-segmentdefinition-rangeoverride-end)" : {{Integer}},
  "[Start](#cfn-customerprofiles-segmentdefinition-rangeoverride-start)" : {{Integer}},
  "[Unit](#cfn-customerprofiles-segmentdefinition-rangeoverride-unit)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-segmentdefinition-rangeoverride-syntax.yaml"></a>

```
  [End](#cfn-customerprofiles-segmentdefinition-rangeoverride-end): {{Integer}}
  [Start](#cfn-customerprofiles-segmentdefinition-rangeoverride-start): {{Integer}}
  [Unit](#cfn-customerprofiles-segmentdefinition-rangeoverride-unit): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-segmentdefinition-rangeoverride-properties"></a>

`End`  <a name="cfn-customerprofiles-segmentdefinition-rangeoverride-end"></a>
The end time of when to include objects.
*Required*: No
*Type*: Integer
*Minimum*: `-2147483648`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Start`  <a name="cfn-customerprofiles-segmentdefinition-rangeoverride-start"></a>
The start time of when to include objects.
*Required*: Yes
*Type*: Integer
*Minimum*: `-2147483648`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Unit`  <a name="cfn-customerprofiles-segmentdefinition-rangeoverride-unit"></a>
The unit for start and end.
*Required*: Yes
*Type*: String
*Allowed values*: `DAYS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
