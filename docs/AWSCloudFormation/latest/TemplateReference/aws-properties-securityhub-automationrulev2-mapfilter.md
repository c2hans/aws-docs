---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrulev2-mapfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRuleV2 MapFilter
<a name="aws-properties-securityhub-automationrulev2-mapfilter"></a>

A map filter for filtering AWS Security Hub CSPM findings. Each map filter provides the field to check for, the value to check for, and the comparison operator.

## Syntax
<a name="aws-properties-securityhub-automationrulev2-mapfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrulev2-mapfilter-syntax.json"></a>

```
{
  "[Comparison](#cfn-securityhub-automationrulev2-mapfilter-comparison)" : {{String}},
  "[Key](#cfn-securityhub-automationrulev2-mapfilter-key)" : {{String}},
  "[Value](#cfn-securityhub-automationrulev2-mapfilter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrulev2-mapfilter-syntax.yaml"></a>

```
  [Comparison](#cfn-securityhub-automationrulev2-mapfilter-comparison): {{String}}
  [Key](#cfn-securityhub-automationrulev2-mapfilter-key): {{String}}
  [Value](#cfn-securityhub-automationrulev2-mapfilter-value): {{String}}
```

## Properties
<a name="aws-properties-securityhub-automationrulev2-mapfilter-properties"></a>

`Comparison`  <a name="cfn-securityhub-automationrulev2-mapfilter-comparison"></a>
The condition to apply to the key value when filtering Security Hub CSPM findings with a map filter.
To search for values that have the filter value, use one of the following comparison operators:
+ To search for values that include the filter value, use `CONTAINS`. For example, for the `ResourceTags` field, the filter `Department CONTAINS Security` matches findings that include the value `Security` for the `Department` tag. In the same example, a finding with a value of `Security team` for the `Department` tag is a match.
+ To search for values that exactly match the filter value, use `EQUALS`. For example, for the `ResourceTags` field, the filter `Department EQUALS Security` matches findings that have the value `Security` for the `Department` tag.
`CONTAINS` and `EQUALS` filters on the same field are joined by `OR`. A finding matches if it matches any one of those filters. For example, the filters `Department CONTAINS Security OR Department CONTAINS Finance` match a finding that includes either `Security`, `Finance`, or both values.
To search for values that don't have the filter value, use one of the following comparison operators:
+ To search for values that exclude the filter value, use `NOT_CONTAINS`. For example, for the `ResourceTags` field, the filter `Department NOT_CONTAINS Finance` matches findings that exclude the value `Finance` for the `Department` tag.
+ To search for values other than the filter value, use `NOT_EQUALS`. For example, for the `ResourceTags` field, the filter `Department NOT_EQUALS Finance` matches findings that don’t have the value `Finance` for the `Department` tag.
`NOT_CONTAINS` and `NOT_EQUALS` filters on the same field are joined by `AND`. A finding matches only if it matches all of those filters. For example, the filters `Department NOT_CONTAINS Security AND Department NOT_CONTAINS Finance` match a finding that excludes both the `Security` and `Finance` values.
`CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.
You can’t have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you can’t have both an `EQUALS` filter and a `NOT_EQUALS` filter on the same field. Combining filters in this way returns an error.
`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *AWS Security Hub CSPM User Guide*.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS | NOT_EQUALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-securityhub-automationrulev2-mapfilter-key"></a>
The key of the map filter. For example, for `ResourceTags`, `Key` identifies the name of the tag. For `UserDefinedFields`, `Key` is the name of the field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-securityhub-automationrulev2-mapfilter-value"></a>
The value for the key in the map filter. Filter values are case sensitive. For example, one of the values for a tag called `Department` might be `Security`. If you provide `security` as the filter value, then there's no match.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
