---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-whatifrangescenario.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard WhatIfRangeScenario
<a name="aws-properties-quicksight-dashboard-whatifrangescenario"></a>

Provides the forecast to meet the target for a particular date range.

## Syntax
<a name="aws-properties-quicksight-dashboard-whatifrangescenario-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-whatifrangescenario-syntax.json"></a>

```
{
  "[EndDate](#cfn-quicksight-dashboard-whatifrangescenario-enddate)" : {{String}},
  "[StartDate](#cfn-quicksight-dashboard-whatifrangescenario-startdate)" : {{String}},
  "[Value](#cfn-quicksight-dashboard-whatifrangescenario-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-whatifrangescenario-syntax.yaml"></a>

```
  [EndDate](#cfn-quicksight-dashboard-whatifrangescenario-enddate): {{String}}
  [StartDate](#cfn-quicksight-dashboard-whatifrangescenario-startdate): {{String}}
  [Value](#cfn-quicksight-dashboard-whatifrangescenario-value): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-whatifrangescenario-properties"></a>

`EndDate`  <a name="cfn-quicksight-dashboard-whatifrangescenario-enddate"></a>
The end date in the date range that you need the forecast results for.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartDate`  <a name="cfn-quicksight-dashboard-whatifrangescenario-startdate"></a>
The start date in the date range that you need the forecast results for.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-dashboard-whatifrangescenario-value"></a>
The target value that you want to meet for the provided date range.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
