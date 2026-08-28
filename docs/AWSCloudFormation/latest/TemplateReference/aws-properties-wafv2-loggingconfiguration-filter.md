---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-loggingconfiguration-filter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::LoggingConfiguration Filter
<a name="aws-properties-wafv2-loggingconfiguration-filter"></a>

A single logging filter, used in `LoggingFilter`.

## Syntax
<a name="aws-properties-wafv2-loggingconfiguration-filter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-loggingconfiguration-filter-syntax.json"></a>

```
{
  "[Behavior](#cfn-wafv2-loggingconfiguration-filter-behavior)" : {{String}},
  "[Conditions](#cfn-wafv2-loggingconfiguration-filter-conditions)" : {{[ Condition, ... ]}},
  "[Requirement](#cfn-wafv2-loggingconfiguration-filter-requirement)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-loggingconfiguration-filter-syntax.yaml"></a>

```
  [Behavior](#cfn-wafv2-loggingconfiguration-filter-behavior): {{String}}
  [Conditions](#cfn-wafv2-loggingconfiguration-filter-conditions): {{
    - Condition}}
  [Requirement](#cfn-wafv2-loggingconfiguration-filter-requirement): {{String}}
```

## Properties
<a name="aws-properties-wafv2-loggingconfiguration-filter-properties"></a>

`Behavior`  <a name="cfn-wafv2-loggingconfiguration-filter-behavior"></a>
How to handle logs that satisfy the filter's conditions and requirement.
*Required*: Yes
*Type*: String
*Allowed values*: `KEEP | DROP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Conditions`  <a name="cfn-wafv2-loggingconfiguration-filter-conditions"></a>
Match conditions for the filter.
*Required*: Yes
*Type*: Array of [Condition](aws-properties-wafv2-loggingconfiguration-condition.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Requirement`  <a name="cfn-wafv2-loggingconfiguration-filter-requirement"></a>
Logic to apply to the filtering conditions. You can specify that, in order to satisfy the filter, a log must match all conditions or must match at least one condition.
*Required*: Yes
*Type*: String
*Allowed values*: `MEETS_ALL | MEETS_ANY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
