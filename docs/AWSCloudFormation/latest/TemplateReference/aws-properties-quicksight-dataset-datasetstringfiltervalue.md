---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datasetstringfiltervalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataSetStringFilterValue
<a name="aws-properties-quicksight-dataset-datasetstringfiltervalue"></a>

Represents a string value used in filter conditions.

## Syntax
<a name="aws-properties-quicksight-dataset-datasetstringfiltervalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datasetstringfiltervalue-syntax.json"></a>

```
{
  "[StaticValue](#cfn-quicksight-dataset-datasetstringfiltervalue-staticvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datasetstringfiltervalue-syntax.yaml"></a>

```
  [StaticValue](#cfn-quicksight-dataset-datasetstringfiltervalue-staticvalue): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datasetstringfiltervalue-properties"></a>

`StaticValue`  <a name="cfn-quicksight-dataset-datasetstringfiltervalue-staticvalue"></a>
A static string value used for filtering.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
