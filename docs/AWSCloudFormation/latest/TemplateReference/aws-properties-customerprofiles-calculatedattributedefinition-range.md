---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-calculatedattributedefinition-range.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::CalculatedAttributeDefinition Range
<a name="aws-properties-customerprofiles-calculatedattributedefinition-range"></a>

The relative time period over which data is included in the aggregation.

## Syntax
<a name="aws-properties-customerprofiles-calculatedattributedefinition-range-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-calculatedattributedefinition-range-syntax.json"></a>

```
{
  "[TimestampFormat](#cfn-customerprofiles-calculatedattributedefinition-range-timestampformat)" : {{String}},
  "[TimestampSource](#cfn-customerprofiles-calculatedattributedefinition-range-timestampsource)" : {{String}},
  "[Unit](#cfn-customerprofiles-calculatedattributedefinition-range-unit)" : {{String}},
  "[Value](#cfn-customerprofiles-calculatedattributedefinition-range-value)" : {{Integer}},
  "[ValueRange](#cfn-customerprofiles-calculatedattributedefinition-range-valuerange)" : {{ValueRange}}
}
```

### YAML
<a name="aws-properties-customerprofiles-calculatedattributedefinition-range-syntax.yaml"></a>

```
  [TimestampFormat](#cfn-customerprofiles-calculatedattributedefinition-range-timestampformat): {{String}}
  [TimestampSource](#cfn-customerprofiles-calculatedattributedefinition-range-timestampsource): {{String}}
  [Unit](#cfn-customerprofiles-calculatedattributedefinition-range-unit): {{String}}
  [Value](#cfn-customerprofiles-calculatedattributedefinition-range-value): {{Integer}}
  [ValueRange](#cfn-customerprofiles-calculatedattributedefinition-range-valuerange): {{
    ValueRange}}
```

## Properties
<a name="aws-properties-customerprofiles-calculatedattributedefinition-range-properties"></a>

`TimestampFormat`  <a name="cfn-customerprofiles-calculatedattributedefinition-range-timestampformat"></a>
The format the timestamp field in your JSON object is specified. This value should be one of EPOCHMILLI (for Unix epoch timestamps with second/millisecond level precision) or ISO\_8601 (following ISO\_8601 format with second/millisecond level precision, with an optional offset of Z or in the format HH:MM or HHMM.). E.g. if your object type is MyType and source JSON is {"generatedAt": {"timestamp": "2001-07-04T12:08:56.235-0700"}}, then TimestampFormat should be "ISO\_8601"
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TimestampSource`  <a name="cfn-customerprofiles-calculatedattributedefinition-range-timestampsource"></a>
An expression specifying the field in your JSON object from which the date should be parsed. The expression should follow the structure of \\"{ObjectTypeName.<Location of timestamp field in JSON pointer format>}\\". E.g. if your object type is MyType and source JSON is {"generatedAt": {"timestamp": "1737587945945"}}, then TimestampSource should be "{MyType.generatedAt.timestamp}"
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Unit`  <a name="cfn-customerprofiles-calculatedattributedefinition-range-unit"></a>
The unit of time.
*Required*: Yes
*Type*: String
*Allowed values*: `DAYS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-customerprofiles-calculatedattributedefinition-range-value"></a>
The amount of time of the specified unit.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueRange`  <a name="cfn-customerprofiles-calculatedattributedefinition-range-valuerange"></a>
A structure letting customers specify a relative time window over which over which data is included in the Calculated Attribute. Use positive numbers to indicate that the endpoint is in the past, and negative numbers to indicate it is in the future. ValueRange overrides Value.
*Required*: No
*Type*: [ValueRange](aws-properties-customerprofiles-calculatedattributedefinition-valuerange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
