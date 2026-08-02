---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-tablepathelement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet TablePathElement
<a name="aws-properties-quicksight-dataset-tablepathelement"></a>

An element in the hierarchical path to a table within a data source, containing both name and identifier.

## Syntax
<a name="aws-properties-quicksight-dataset-tablepathelement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-tablepathelement-syntax.json"></a>

```
{
  "[Id](#cfn-quicksight-dataset-tablepathelement-id)" : {{String}},
  "[Name](#cfn-quicksight-dataset-tablepathelement-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-tablepathelement-syntax.yaml"></a>

```
  [Id](#cfn-quicksight-dataset-tablepathelement-id): {{String}}
  [Name](#cfn-quicksight-dataset-tablepathelement-name): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-tablepathelement-properties"></a>

`Id`  <a name="cfn-quicksight-dataset-tablepathelement-id"></a>
The unique identifier of the path element.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-dataset-tablepathelement-name"></a>
The name of the path element.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
