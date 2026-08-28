---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrulev2-datefilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRuleV2 DateFilter
<a name="aws-properties-securityhub-automationrulev2-datefilter"></a>

A date filter for querying findings.

## Syntax
<a name="aws-properties-securityhub-automationrulev2-datefilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrulev2-datefilter-syntax.json"></a>

```
{
  "[DateRange](#cfn-securityhub-automationrulev2-datefilter-daterange)" : {{DateRange}},
  "[End](#cfn-securityhub-automationrulev2-datefilter-end)" : {{String}},
  "[Start](#cfn-securityhub-automationrulev2-datefilter-start)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrulev2-datefilter-syntax.yaml"></a>

```
  [DateRange](#cfn-securityhub-automationrulev2-datefilter-daterange): {{
    DateRange}}
  [End](#cfn-securityhub-automationrulev2-datefilter-end): {{String}}
  [Start](#cfn-securityhub-automationrulev2-datefilter-start): {{String}}
```

## Properties
<a name="aws-properties-securityhub-automationrulev2-datefilter-properties"></a>

`DateRange`  <a name="cfn-securityhub-automationrulev2-datefilter-daterange"></a>
A date range for the date filter.
*Required*: No
*Type*: [DateRange](aws-properties-securityhub-automationrulev2-daterange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`End`  <a name="cfn-securityhub-automationrulev2-datefilter-end"></a>
A timestamp that provides the end date for the date filter.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
*Required*: No
*Type*: String
*Pattern*: `^(\d\d\d\d)-([0][1-9]|[1][0-2])-([0][1-9]|[1-2](\d)|[3][0-1])[T](?:([0-1](\d)|[2][0-3]):[0-5](\d):[0-5](\d)|23:59:60)(?:\.(\d)+)?([Z]|[+-](\d\d)(:?(\d\d))?)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Start`  <a name="cfn-securityhub-automationrulev2-datefilter-start"></a>
A timestamp that provides the start date for the date filter.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
*Required*: No
*Type*: String
*Pattern*: `^(\d\d\d\d)-([0][1-9]|[1][0-2])-([0][1-9]|[1-2](\d)|[3][0-1])[T](?:([0-1](\d)|[2][0-3]):[0-5](\d):[0-5](\d)|23:59:60)(?:\.(\d)+)?([Z]|[+-](\d\d)(:?(\d\d))?)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
