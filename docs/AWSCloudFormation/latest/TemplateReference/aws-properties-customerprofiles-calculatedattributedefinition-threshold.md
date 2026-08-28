---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-calculatedattributedefinition-threshold.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::CalculatedAttributeDefinition Threshold
<a name="aws-properties-customerprofiles-calculatedattributedefinition-threshold"></a>

The threshold for the calculated attribute.

## Syntax
<a name="aws-properties-customerprofiles-calculatedattributedefinition-threshold-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-calculatedattributedefinition-threshold-syntax.json"></a>

```
{
  "[Operator](#cfn-customerprofiles-calculatedattributedefinition-threshold-operator)" : {{String}},
  "[Value](#cfn-customerprofiles-calculatedattributedefinition-threshold-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-calculatedattributedefinition-threshold-syntax.yaml"></a>

```
  [Operator](#cfn-customerprofiles-calculatedattributedefinition-threshold-operator): {{String}}
  [Value](#cfn-customerprofiles-calculatedattributedefinition-threshold-value): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-calculatedattributedefinition-threshold-properties"></a>

`Operator`  <a name="cfn-customerprofiles-calculatedattributedefinition-threshold-operator"></a>
The operator of the threshold.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUAL_TO | GREATER_THAN | LESS_THAN | NOT_EQUAL_TO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-customerprofiles-calculatedattributedefinition-threshold-value"></a>
The value of the threshold.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
