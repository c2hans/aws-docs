---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-calculatedattributedefinition-valuerange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::CalculatedAttributeDefinition ValueRange
<a name="aws-properties-customerprofiles-calculatedattributedefinition-valuerange"></a>

A structure letting customers specify a relative time window over which over which data is included in the Calculated Attribute. Use positive numbers to indicate that the endpoint is in the past, and negative numbers to indicate it is in the future. ValueRange overrides Value.

## Syntax
<a name="aws-properties-customerprofiles-calculatedattributedefinition-valuerange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-calculatedattributedefinition-valuerange-syntax.json"></a>

```
{
  "[End](#cfn-customerprofiles-calculatedattributedefinition-valuerange-end)" : {{Integer}},
  "[Start](#cfn-customerprofiles-calculatedattributedefinition-valuerange-start)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-customerprofiles-calculatedattributedefinition-valuerange-syntax.yaml"></a>

```
  [End](#cfn-customerprofiles-calculatedattributedefinition-valuerange-end): {{Integer}}
  [Start](#cfn-customerprofiles-calculatedattributedefinition-valuerange-start): {{Integer}}
```

## Properties
<a name="aws-properties-customerprofiles-calculatedattributedefinition-valuerange-properties"></a>

`End`  <a name="cfn-customerprofiles-calculatedattributedefinition-valuerange-end"></a>
The ending point for this overridden range. Positive numbers indicate how many days in the past data should be included, and negative numbers indicate how many days in the future.
*Required*: Yes
*Type*: Integer
*Minimum*: `-2147483648`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Start`  <a name="cfn-customerprofiles-calculatedattributedefinition-valuerange-start"></a>
The starting point for this overridden range. Positive numbers indicate how many days in the past data should be included, and negative numbers indicate how many days in the future.
*Required*: Yes
*Type*: Integer
*Minimum*: `-2147483648`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
