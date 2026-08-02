---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-integerparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard IntegerParameter
<a name="aws-properties-quicksight-dashboard-integerparameter"></a>

An integer parameter.

## Syntax
<a name="aws-properties-quicksight-dashboard-integerparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-integerparameter-syntax.json"></a>

```
{
  "[Name](#cfn-quicksight-dashboard-integerparameter-name)" : {{String}},
  "[Values](#cfn-quicksight-dashboard-integerparameter-values)" : {{[ Number, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-integerparameter-syntax.yaml"></a>

```
  [Name](#cfn-quicksight-dashboard-integerparameter-name): {{String}}
  [Values](#cfn-quicksight-dashboard-integerparameter-values): {{
    - Number}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-integerparameter-properties"></a>

`Name`  <a name="cfn-quicksight-dashboard-integerparameter-name"></a>
The name of the integer parameter.
*Required*: Yes
*Type*: String
*Pattern*: `\S`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-dashboard-integerparameter-values"></a>
The values for the integer parameter.
*Required*: Yes
*Type*: Array of Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
