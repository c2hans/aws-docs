---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-stringdatasetparameterdefaultvalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet StringDatasetParameterDefaultValues
<a name="aws-properties-quicksight-dataset-stringdatasetparameterdefaultvalues"></a>

A list of default values for a given string dataset parameter type. This structure only accepts static values.

## Syntax
<a name="aws-properties-quicksight-dataset-stringdatasetparameterdefaultvalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-stringdatasetparameterdefaultvalues-syntax.json"></a>

```
{
  "[StaticValues](#cfn-quicksight-dataset-stringdatasetparameterdefaultvalues-staticvalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-stringdatasetparameterdefaultvalues-syntax.yaml"></a>

```
  [StaticValues](#cfn-quicksight-dataset-stringdatasetparameterdefaultvalues-staticvalues): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-stringdatasetparameterdefaultvalues-properties"></a>

`StaticValues`  <a name="cfn-quicksight-dataset-stringdatasetparameterdefaultvalues-staticvalues"></a>
A list of static default values for a given string parameter.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 0`
*Maximum*: `512 | 32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
