---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrule-datefilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRule DateFilter
<a name="aws-properties-securityhub-automationrule-datefilter"></a>

A date filter for querying findings.

## Syntax
<a name="aws-properties-securityhub-automationrule-datefilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrule-datefilter-syntax.json"></a>

```
{
  "[DateRange](#cfn-securityhub-automationrule-datefilter-daterange)" : {{DateRange}},
  "[End](#cfn-securityhub-automationrule-datefilter-end)" : {{String}},
  "[Start](#cfn-securityhub-automationrule-datefilter-start)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrule-datefilter-syntax.yaml"></a>

```
  [DateRange](#cfn-securityhub-automationrule-datefilter-daterange): {{
    DateRange}}
  [End](#cfn-securityhub-automationrule-datefilter-end): {{String}}
  [Start](#cfn-securityhub-automationrule-datefilter-start): {{String}}
```

## Properties
<a name="aws-properties-securityhub-automationrule-datefilter-properties"></a>

`DateRange`  <a name="cfn-securityhub-automationrule-datefilter-daterange"></a>
A date range for the date filter.
*Required*: No
*Type*: [DateRange](aws-properties-securityhub-automationrule-daterange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`End`  <a name="cfn-securityhub-automationrule-datefilter-end"></a>
A timestamp that provides the end date for the date filter.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
*Required*: No
*Type*: String
*Pattern*: `^(\d\d\d\d)-([0][1-9]|[1][0-2])-([0][1-9]|[1-2](\d)|[3][0-1])[T](?:([0-1](\d)|[2][0-3]):[0-5](\d):[0-5](\d)|23:59:60)(?:\.(\d)+)?([Z]|[+-](\d\d)(:?(\d\d))?)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Start`  <a name="cfn-securityhub-automationrule-datefilter-start"></a>
A timestamp that provides the start date for the date filter.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
*Required*: No
*Type*: String
*Pattern*: `^(\d\d\d\d)-([0][1-9]|[1][0-2])-([0][1-9]|[1-2](\d)|[3][0-1])[T](?:([0-1](\d)|[2][0-3]):[0-5](\d):[0-5](\d)|23:59:60)(?:\.(\d)+)?([Z]|[+-](\d\d)(:?(\d\d))?)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
