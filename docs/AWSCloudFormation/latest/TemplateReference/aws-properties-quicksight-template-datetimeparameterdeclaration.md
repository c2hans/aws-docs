---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-datetimeparameterdeclaration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DateTimeParameterDeclaration
<a name="aws-properties-quicksight-template-datetimeparameterdeclaration"></a>

A parameter declaration for the `DateTime` data type.

## Syntax
<a name="aws-properties-quicksight-template-datetimeparameterdeclaration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-datetimeparameterdeclaration-syntax.json"></a>

```
{
  "[DefaultValues](#cfn-quicksight-template-datetimeparameterdeclaration-defaultvalues)" : {{DateTimeDefaultValues}},
  "[MappedDataSetParameters](#cfn-quicksight-template-datetimeparameterdeclaration-mappeddatasetparameters)" : {{[ MappedDataSetParameter, ... ]}},
  "[Name](#cfn-quicksight-template-datetimeparameterdeclaration-name)" : {{String}},
  "[TimeGranularity](#cfn-quicksight-template-datetimeparameterdeclaration-timegranularity)" : {{String}},
  "[ValueWhenUnset](#cfn-quicksight-template-datetimeparameterdeclaration-valuewhenunset)" : {{DateTimeValueWhenUnsetConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-datetimeparameterdeclaration-syntax.yaml"></a>

```
  [DefaultValues](#cfn-quicksight-template-datetimeparameterdeclaration-defaultvalues): {{
    DateTimeDefaultValues}}
  [MappedDataSetParameters](#cfn-quicksight-template-datetimeparameterdeclaration-mappeddatasetparameters): {{
    - MappedDataSetParameter}}
  [Name](#cfn-quicksight-template-datetimeparameterdeclaration-name): {{String}}
  [TimeGranularity](#cfn-quicksight-template-datetimeparameterdeclaration-timegranularity): {{String}}
  [ValueWhenUnset](#cfn-quicksight-template-datetimeparameterdeclaration-valuewhenunset): {{
    DateTimeValueWhenUnsetConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-datetimeparameterdeclaration-properties"></a>

`DefaultValues`  <a name="cfn-quicksight-template-datetimeparameterdeclaration-defaultvalues"></a>
The default values of a parameter. If the parameter is a single-value parameter, a maximum of one default value can be provided.
*Required*: No
*Type*: [DateTimeDefaultValues](aws-properties-quicksight-template-datetimedefaultvalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MappedDataSetParameters`  <a name="cfn-quicksight-template-datetimeparameterdeclaration-mappeddatasetparameters"></a>
Property description not available.
*Required*: No
*Type*: Array of [MappedDataSetParameter](aws-properties-quicksight-template-mappeddatasetparameter.md)
*Minimum*: `0`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-template-datetimeparameterdeclaration-name"></a>
The name of the parameter that is being declared.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeGranularity`  <a name="cfn-quicksight-template-datetimeparameterdeclaration-timegranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
*Required*: No
*Type*: String
*Allowed values*: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueWhenUnset`  <a name="cfn-quicksight-template-datetimeparameterdeclaration-valuewhenunset"></a>
The configuration that defines the default value of a `DateTime` parameter when a value has not been set.
*Required*: No
*Type*: [DateTimeValueWhenUnsetConfiguration](aws-properties-quicksight-template-datetimevaluewhenunsetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
