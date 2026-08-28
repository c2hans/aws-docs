---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-whatifpointscenario.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard WhatIfPointScenario
<a name="aws-properties-quicksight-dashboard-whatifpointscenario"></a>

Provides the forecast to meet the target for a particular date.

## Syntax
<a name="aws-properties-quicksight-dashboard-whatifpointscenario-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-whatifpointscenario-syntax.json"></a>

```
{
  "[Date](#cfn-quicksight-dashboard-whatifpointscenario-date)" : {{String}},
  "[Value](#cfn-quicksight-dashboard-whatifpointscenario-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-whatifpointscenario-syntax.yaml"></a>

```
  [Date](#cfn-quicksight-dashboard-whatifpointscenario-date): {{String}}
  [Value](#cfn-quicksight-dashboard-whatifpointscenario-value): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-whatifpointscenario-properties"></a>

`Date`  <a name="cfn-quicksight-dashboard-whatifpointscenario-date"></a>
The date that you need the forecast results for.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-dashboard-whatifpointscenario-value"></a>
The target value that you want to meet for the provided date.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
