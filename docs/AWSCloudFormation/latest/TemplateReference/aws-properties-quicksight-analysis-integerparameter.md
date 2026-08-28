---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-integerparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis IntegerParameter
<a name="aws-properties-quicksight-analysis-integerparameter"></a>

An integer parameter.

## Syntax
<a name="aws-properties-quicksight-analysis-integerparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-integerparameter-syntax.json"></a>

```
{
  "[Name](#cfn-quicksight-analysis-integerparameter-name)" : {{String}},
  "[Values](#cfn-quicksight-analysis-integerparameter-values)" : {{[ Number, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-integerparameter-syntax.yaml"></a>

```
  [Name](#cfn-quicksight-analysis-integerparameter-name): {{String}}
  [Values](#cfn-quicksight-analysis-integerparameter-values): {{
    - Number}}
```

## Properties
<a name="aws-properties-quicksight-analysis-integerparameter-properties"></a>

`Name`  <a name="cfn-quicksight-analysis-integerparameter-name"></a>
The name of the integer parameter.
*Required*: Yes
*Type*: String
*Pattern*: `\S`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-analysis-integerparameter-values"></a>
The values for the integer parameter.
*Required*: Yes
*Type*: Array of Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
