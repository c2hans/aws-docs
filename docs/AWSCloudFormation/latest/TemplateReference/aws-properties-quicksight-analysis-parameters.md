---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-parameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis Parameters
<a name="aws-properties-quicksight-analysis-parameters"></a>

A list of Quick Sight parameters and the list's override values.

## Syntax
<a name="aws-properties-quicksight-analysis-parameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-parameters-syntax.json"></a>

```
{
  "[DateTimeParameters](#cfn-quicksight-analysis-parameters-datetimeparameters)" : {{[ DateTimeParameter, ... ]}},
  "[DecimalParameters](#cfn-quicksight-analysis-parameters-decimalparameters)" : {{[ DecimalParameter, ... ]}},
  "[IntegerParameters](#cfn-quicksight-analysis-parameters-integerparameters)" : {{[ IntegerParameter, ... ]}},
  "[StringParameters](#cfn-quicksight-analysis-parameters-stringparameters)" : {{[ StringParameter, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-parameters-syntax.yaml"></a>

```
  [DateTimeParameters](#cfn-quicksight-analysis-parameters-datetimeparameters): {{
    - DateTimeParameter}}
  [DecimalParameters](#cfn-quicksight-analysis-parameters-decimalparameters): {{
    - DecimalParameter}}
  [IntegerParameters](#cfn-quicksight-analysis-parameters-integerparameters): {{
    - IntegerParameter}}
  [StringParameters](#cfn-quicksight-analysis-parameters-stringparameters): {{
    - StringParameter}}
```

## Properties
<a name="aws-properties-quicksight-analysis-parameters-properties"></a>

`DateTimeParameters`  <a name="cfn-quicksight-analysis-parameters-datetimeparameters"></a>
The parameters that have a data type of date-time.
*Required*: No
*Type*: Array of [DateTimeParameter](aws-properties-quicksight-analysis-datetimeparameter.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DecimalParameters`  <a name="cfn-quicksight-analysis-parameters-decimalparameters"></a>
The parameters that have a data type of decimal.
*Required*: No
*Type*: Array of [DecimalParameter](aws-properties-quicksight-analysis-decimalparameter.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegerParameters`  <a name="cfn-quicksight-analysis-parameters-integerparameters"></a>
The parameters that have a data type of integer.
*Required*: No
*Type*: Array of [IntegerParameter](aws-properties-quicksight-analysis-integerparameter.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringParameters`  <a name="cfn-quicksight-analysis-parameters-stringparameters"></a>
The parameters that have a data type of string.
*Required*: No
*Type*: Array of [StringParameter](aws-properties-quicksight-analysis-stringparameter.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
