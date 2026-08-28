---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-insight-datefilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::Insight DateFilter
<a name="aws-properties-securityhub-insight-datefilter"></a>

A date filter for querying findings.

## Syntax
<a name="aws-properties-securityhub-insight-datefilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-insight-datefilter-syntax.json"></a>

```
{
  "[DateRange](#cfn-securityhub-insight-datefilter-daterange)" : {{DateRange}},
  "[End](#cfn-securityhub-insight-datefilter-end)" : {{String}},
  "[Start](#cfn-securityhub-insight-datefilter-start)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-insight-datefilter-syntax.yaml"></a>

```
  [DateRange](#cfn-securityhub-insight-datefilter-daterange): {{
    DateRange}}
  [End](#cfn-securityhub-insight-datefilter-end): {{String}}
  [Start](#cfn-securityhub-insight-datefilter-start): {{String}}
```

## Properties
<a name="aws-properties-securityhub-insight-datefilter-properties"></a>

`DateRange`  <a name="cfn-securityhub-insight-datefilter-daterange"></a>
A date range for the date filter.
*Required*: No
*Type*: [DateRange](aws-properties-securityhub-insight-daterange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`End`  <a name="cfn-securityhub-insight-datefilter-end"></a>
A timestamp that provides the end date for the date filter.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
*Required*: No
*Type*: String
*Pattern*: `^([\+-]?\d{4}(?!\d{2}))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([tT]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Start`  <a name="cfn-securityhub-insight-datefilter-start"></a>
A timestamp that provides the start date for the date filter.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
*Required*: No
*Type*: String
*Pattern*: `^([\+-]?\d{4}(?!\d{2}))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([tT]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
