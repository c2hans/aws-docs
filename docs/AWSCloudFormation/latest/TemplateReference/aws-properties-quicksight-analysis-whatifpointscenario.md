---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-whatifpointscenario.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis WhatIfPointScenario
<a name="aws-properties-quicksight-analysis-whatifpointscenario"></a>

Provides the forecast to meet the target for a particular date.

## Syntax
<a name="aws-properties-quicksight-analysis-whatifpointscenario-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-whatifpointscenario-syntax.json"></a>

```
{
  "[Date](#cfn-quicksight-analysis-whatifpointscenario-date)" : {{String}},
  "[Value](#cfn-quicksight-analysis-whatifpointscenario-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-whatifpointscenario-syntax.yaml"></a>

```
  [Date](#cfn-quicksight-analysis-whatifpointscenario-date): {{String}}
  [Value](#cfn-quicksight-analysis-whatifpointscenario-value): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-analysis-whatifpointscenario-properties"></a>

`Date`  <a name="cfn-quicksight-analysis-whatifpointscenario-date"></a>
The date that you need the forecast results for.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-analysis-whatifpointscenario-value"></a>
The target value that you want to meet for the provided date.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
