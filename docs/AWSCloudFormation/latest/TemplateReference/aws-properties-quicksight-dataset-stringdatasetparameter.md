---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-stringdatasetparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet StringDatasetParameter
<a name="aws-properties-quicksight-dataset-stringdatasetparameter"></a>

A string parameter that is created in the dataset.

## Syntax
<a name="aws-properties-quicksight-dataset-stringdatasetparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-stringdatasetparameter-syntax.json"></a>

```
{
  "[DefaultValues](#cfn-quicksight-dataset-stringdatasetparameter-defaultvalues)" : {{StringDatasetParameterDefaultValues}},
  "[Id](#cfn-quicksight-dataset-stringdatasetparameter-id)" : {{String}},
  "[Name](#cfn-quicksight-dataset-stringdatasetparameter-name)" : {{String}},
  "[ValueType](#cfn-quicksight-dataset-stringdatasetparameter-valuetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-stringdatasetparameter-syntax.yaml"></a>

```
  [DefaultValues](#cfn-quicksight-dataset-stringdatasetparameter-defaultvalues): {{
    StringDatasetParameterDefaultValues}}
  [Id](#cfn-quicksight-dataset-stringdatasetparameter-id): {{String}}
  [Name](#cfn-quicksight-dataset-stringdatasetparameter-name): {{String}}
  [ValueType](#cfn-quicksight-dataset-stringdatasetparameter-valuetype): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-stringdatasetparameter-properties"></a>

`DefaultValues`  <a name="cfn-quicksight-dataset-stringdatasetparameter-defaultvalues"></a>
A list of default values for a given string dataset parameter type. This structure only accepts static values.
*Required*: No
*Type*: [StringDatasetParameterDefaultValues](aws-properties-quicksight-dataset-stringdatasetparameterdefaultvalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-quicksight-dataset-stringdatasetparameter-id"></a>
An identifier for the string parameter that is created in the dataset.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-dataset-stringdatasetparameter-name"></a>
The name of the string parameter that is created in the dataset.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueType`  <a name="cfn-quicksight-dataset-stringdatasetparameter-valuetype"></a>
The value type of the dataset parameter. Valid values are `single value` or `multi value`.
*Required*: Yes
*Type*: String
*Allowed values*: `MULTI_VALUED | SINGLE_VALUED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
