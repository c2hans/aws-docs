---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrulev2-daterange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRuleV2 DateRange
<a name="aws-properties-securityhub-automationrulev2-daterange"></a>

A date range for the date filter.

## Syntax
<a name="aws-properties-securityhub-automationrulev2-daterange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrulev2-daterange-syntax.json"></a>

```
{
  "[Unit](#cfn-securityhub-automationrulev2-daterange-unit)" : {{String}},
  "[Value](#cfn-securityhub-automationrulev2-daterange-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrulev2-daterange-syntax.yaml"></a>

```
  [Unit](#cfn-securityhub-automationrulev2-daterange-unit): {{String}}
  [Value](#cfn-securityhub-automationrulev2-daterange-value): {{Number}}
```

## Properties
<a name="aws-properties-securityhub-automationrulev2-daterange-properties"></a>

`Unit`  <a name="cfn-securityhub-automationrulev2-daterange-unit"></a>
A date range unit for the date filter.
*Required*: Yes
*Type*: String
*Allowed values*: `DAYS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-securityhub-automationrulev2-daterange-value"></a>
A date range value for the date filter.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
