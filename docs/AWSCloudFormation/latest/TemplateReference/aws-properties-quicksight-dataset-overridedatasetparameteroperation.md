---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-overridedatasetparameteroperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet OverrideDatasetParameterOperation
<a name="aws-properties-quicksight-dataset-overridedatasetparameteroperation"></a>

A transform operation that overrides the dataset parameter values that are defined in another dataset.

## Syntax
<a name="aws-properties-quicksight-dataset-overridedatasetparameteroperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-overridedatasetparameteroperation-syntax.json"></a>

```
{
  "[NewDefaultValues](#cfn-quicksight-dataset-overridedatasetparameteroperation-newdefaultvalues)" : {{NewDefaultValues}},
  "[NewParameterName](#cfn-quicksight-dataset-overridedatasetparameteroperation-newparametername)" : {{String}},
  "[ParameterName](#cfn-quicksight-dataset-overridedatasetparameteroperation-parametername)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-overridedatasetparameteroperation-syntax.yaml"></a>

```
  [NewDefaultValues](#cfn-quicksight-dataset-overridedatasetparameteroperation-newdefaultvalues): {{
    NewDefaultValues}}
  [NewParameterName](#cfn-quicksight-dataset-overridedatasetparameteroperation-newparametername): {{String}}
  [ParameterName](#cfn-quicksight-dataset-overridedatasetparameteroperation-parametername): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-overridedatasetparameteroperation-properties"></a>

`NewDefaultValues`  <a name="cfn-quicksight-dataset-overridedatasetparameteroperation-newdefaultvalues"></a>
The new default values for the parameter.
*Required*: No
*Type*: [NewDefaultValues](aws-properties-quicksight-dataset-newdefaultvalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NewParameterName`  <a name="cfn-quicksight-dataset-overridedatasetparameteroperation-newparametername"></a>
The new name for the parameter.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterName`  <a name="cfn-quicksight-dataset-overridedatasetparameteroperation-parametername"></a>
The name of the parameter to be overridden with different values.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
