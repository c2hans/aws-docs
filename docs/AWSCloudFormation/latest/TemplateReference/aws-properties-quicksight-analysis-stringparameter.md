---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-stringparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis StringParameter
<a name="aws-properties-quicksight-analysis-stringparameter"></a>

A string parameter.

## Syntax
<a name="aws-properties-quicksight-analysis-stringparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-stringparameter-syntax.json"></a>

```
{
  "[Name](#cfn-quicksight-analysis-stringparameter-name)" : {{String}},
  "[Values](#cfn-quicksight-analysis-stringparameter-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-stringparameter-syntax.yaml"></a>

```
  [Name](#cfn-quicksight-analysis-stringparameter-name): {{String}}
  [Values](#cfn-quicksight-analysis-stringparameter-values): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-stringparameter-properties"></a>

`Name`  <a name="cfn-quicksight-analysis-stringparameter-name"></a>
A display name for a string parameter.
*Required*: Yes
*Type*: String
*Pattern*: `\S`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-analysis-stringparameter-values"></a>
The values of a string parameter.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
