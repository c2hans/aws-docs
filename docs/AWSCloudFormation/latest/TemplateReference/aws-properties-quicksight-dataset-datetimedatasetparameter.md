---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datetimedatasetparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DateTimeDatasetParameter
<a name="aws-properties-quicksight-dataset-datetimedatasetparameter"></a>

A date time parameter that is created in the dataset.

## Syntax
<a name="aws-properties-quicksight-dataset-datetimedatasetparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datetimedatasetparameter-syntax.json"></a>

```
{
  "[DefaultValues](#cfn-quicksight-dataset-datetimedatasetparameter-defaultvalues)" : {{DateTimeDatasetParameterDefaultValues}},
  "[Id](#cfn-quicksight-dataset-datetimedatasetparameter-id)" : {{String}},
  "[Name](#cfn-quicksight-dataset-datetimedatasetparameter-name)" : {{String}},
  "[TimeGranularity](#cfn-quicksight-dataset-datetimedatasetparameter-timegranularity)" : {{String}},
  "[ValueType](#cfn-quicksight-dataset-datetimedatasetparameter-valuetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datetimedatasetparameter-syntax.yaml"></a>

```
  [DefaultValues](#cfn-quicksight-dataset-datetimedatasetparameter-defaultvalues): {{
    DateTimeDatasetParameterDefaultValues}}
  [Id](#cfn-quicksight-dataset-datetimedatasetparameter-id): {{String}}
  [Name](#cfn-quicksight-dataset-datetimedatasetparameter-name): {{String}}
  [TimeGranularity](#cfn-quicksight-dataset-datetimedatasetparameter-timegranularity): {{String}}
  [ValueType](#cfn-quicksight-dataset-datetimedatasetparameter-valuetype): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datetimedatasetparameter-properties"></a>

`DefaultValues`  <a name="cfn-quicksight-dataset-datetimedatasetparameter-defaultvalues"></a>
A list of default values for a given date time parameter. This structure only accepts static values.
*Required*: No
*Type*: [DateTimeDatasetParameterDefaultValues](aws-properties-quicksight-dataset-datetimedatasetparameterdefaultvalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-quicksight-dataset-datetimedatasetparameter-id"></a>
An identifier for the parameter that is created in the dataset.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-dataset-datetimedatasetparameter-name"></a>
The name of the date time parameter that is created in the dataset.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeGranularity`  <a name="cfn-quicksight-dataset-datetimedatasetparameter-timegranularity"></a>
The time granularity of the date time parameter.
*Required*: No
*Type*: String
*Allowed values*: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueType`  <a name="cfn-quicksight-dataset-datetimedatasetparameter-valuetype"></a>
The value type of the dataset parameter. Valid values are `single value` or `multi value`.
*Required*: Yes
*Type*: String
*Allowed values*: `MULTI_VALUED | SINGLE_VALUED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
