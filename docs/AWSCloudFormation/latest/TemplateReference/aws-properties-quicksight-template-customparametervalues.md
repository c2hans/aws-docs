---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-customparametervalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template CustomParameterValues
<a name="aws-properties-quicksight-template-customparametervalues"></a>

The customized parameter values.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-template-customparametervalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-customparametervalues-syntax.json"></a>

```
{
  "[DateTimeValues](#cfn-quicksight-template-customparametervalues-datetimevalues)" : {{[ String, ... ]}},
  "[DecimalValues](#cfn-quicksight-template-customparametervalues-decimalvalues)" : {{[ Number, ... ]}},
  "[IntegerValues](#cfn-quicksight-template-customparametervalues-integervalues)" : {{[ Number, ... ]}},
  "[StringValues](#cfn-quicksight-template-customparametervalues-stringvalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-customparametervalues-syntax.yaml"></a>

```
  [DateTimeValues](#cfn-quicksight-template-customparametervalues-datetimevalues): {{
    - String}}
  [DecimalValues](#cfn-quicksight-template-customparametervalues-decimalvalues): {{
    - Number}}
  [IntegerValues](#cfn-quicksight-template-customparametervalues-integervalues): {{
    - Number}}
  [StringValues](#cfn-quicksight-template-customparametervalues-stringvalues): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-template-customparametervalues-properties"></a>

`DateTimeValues`  <a name="cfn-quicksight-template-customparametervalues-datetimevalues"></a>
A list of datetime-type parameter values.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `50000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DecimalValues`  <a name="cfn-quicksight-template-customparametervalues-decimalvalues"></a>
A list of decimal-type parameter values.
*Required*: No
*Type*: Array of Number
*Minimum*: `0`
*Maximum*: `50000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegerValues`  <a name="cfn-quicksight-template-customparametervalues-integervalues"></a>
A list of integer-type parameter values.
*Required*: No
*Type*: Array of Number
*Minimum*: `0`
*Maximum*: `50000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringValues`  <a name="cfn-quicksight-template-customparametervalues-stringvalues"></a>
A list of string-type parameter values.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `50000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
