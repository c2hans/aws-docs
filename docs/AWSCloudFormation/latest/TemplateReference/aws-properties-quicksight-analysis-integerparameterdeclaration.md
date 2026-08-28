---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-integerparameterdeclaration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis IntegerParameterDeclaration
<a name="aws-properties-quicksight-analysis-integerparameterdeclaration"></a>

A parameter declaration for the `Integer` data type.

## Syntax
<a name="aws-properties-quicksight-analysis-integerparameterdeclaration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-integerparameterdeclaration-syntax.json"></a>

```
{
  "[DefaultValues](#cfn-quicksight-analysis-integerparameterdeclaration-defaultvalues)" : {{IntegerDefaultValues}},
  "[MappedDataSetParameters](#cfn-quicksight-analysis-integerparameterdeclaration-mappeddatasetparameters)" : {{[ MappedDataSetParameter, ... ]}},
  "[Name](#cfn-quicksight-analysis-integerparameterdeclaration-name)" : {{String}},
  "[ParameterValueType](#cfn-quicksight-analysis-integerparameterdeclaration-parametervaluetype)" : {{String}},
  "[ValueWhenUnset](#cfn-quicksight-analysis-integerparameterdeclaration-valuewhenunset)" : {{IntegerValueWhenUnsetConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-integerparameterdeclaration-syntax.yaml"></a>

```
  [DefaultValues](#cfn-quicksight-analysis-integerparameterdeclaration-defaultvalues): {{
    IntegerDefaultValues}}
  [MappedDataSetParameters](#cfn-quicksight-analysis-integerparameterdeclaration-mappeddatasetparameters): {{
    - MappedDataSetParameter}}
  [Name](#cfn-quicksight-analysis-integerparameterdeclaration-name): {{String}}
  [ParameterValueType](#cfn-quicksight-analysis-integerparameterdeclaration-parametervaluetype): {{String}}
  [ValueWhenUnset](#cfn-quicksight-analysis-integerparameterdeclaration-valuewhenunset): {{
    IntegerValueWhenUnsetConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-integerparameterdeclaration-properties"></a>

`DefaultValues`  <a name="cfn-quicksight-analysis-integerparameterdeclaration-defaultvalues"></a>
The default values of a parameter. If the parameter is a single-value parameter, a maximum of one default value can be provided.
*Required*: No
*Type*: [IntegerDefaultValues](aws-properties-quicksight-analysis-integerdefaultvalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MappedDataSetParameters`  <a name="cfn-quicksight-analysis-integerparameterdeclaration-mappeddatasetparameters"></a>
Property description not available.
*Required*: No
*Type*: Array of [MappedDataSetParameter](aws-properties-quicksight-analysis-mappeddatasetparameter.md)
*Minimum*: `0`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-analysis-integerparameterdeclaration-name"></a>
The name of the parameter that is being declared.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterValueType`  <a name="cfn-quicksight-analysis-integerparameterdeclaration-parametervaluetype"></a>
The value type determines whether the parameter is a single-value or multi-value parameter.
*Required*: Yes
*Type*: String
*Allowed values*: `MULTI_VALUED | SINGLE_VALUED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueWhenUnset`  <a name="cfn-quicksight-analysis-integerparameterdeclaration-valuewhenunset"></a>
A parameter declaration for the `Integer` data type.
*Required*: No
*Type*: [IntegerValueWhenUnsetConfiguration](aws-properties-quicksight-analysis-integervaluewhenunsetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
