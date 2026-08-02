---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datetimedatasetparameterdefaultvalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DateTimeDatasetParameterDefaultValues
<a name="aws-properties-quicksight-dataset-datetimedatasetparameterdefaultvalues"></a>

<a name="aws-properties-quicksight-dataset-datetimedatasetparameterdefaultvalues-description"></a>The `DateTimeDatasetParameterDefaultValues` property type specifies Property description not available. for an [AWS::QuickSight::DataSet](aws-resource-quicksight-dataset.md).

## Syntax
<a name="aws-properties-quicksight-dataset-datetimedatasetparameterdefaultvalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datetimedatasetparameterdefaultvalues-syntax.json"></a>

```
{
  "[StaticValues](#cfn-quicksight-dataset-datetimedatasetparameterdefaultvalues-staticvalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datetimedatasetparameterdefaultvalues-syntax.yaml"></a>

```
  [StaticValues](#cfn-quicksight-dataset-datetimedatasetparameterdefaultvalues-staticvalues): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datetimedatasetparameterdefaultvalues-properties"></a>

`StaticValues`  <a name="cfn-quicksight-dataset-datetimedatasetparameterdefaultvalues-staticvalues"></a>
A list of static default values for a given date time parameter. The valid format for this property is `yyyy-MM-dd’T’HH:mm:ss’Z’`.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
