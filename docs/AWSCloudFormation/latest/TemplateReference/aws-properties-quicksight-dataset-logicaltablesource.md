---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-logicaltablesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet LogicalTableSource
<a name="aws-properties-quicksight-dataset-logicaltablesource"></a>

Information about the source of a logical table. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

## Syntax
<a name="aws-properties-quicksight-dataset-logicaltablesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-logicaltablesource-syntax.json"></a>

```
{
  "[DataSetArn](#cfn-quicksight-dataset-logicaltablesource-datasetarn)" : {{String}},
  "[JoinInstruction](#cfn-quicksight-dataset-logicaltablesource-joininstruction)" : {{JoinInstruction}},
  "[PhysicalTableId](#cfn-quicksight-dataset-logicaltablesource-physicaltableid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-logicaltablesource-syntax.yaml"></a>

```
  [DataSetArn](#cfn-quicksight-dataset-logicaltablesource-datasetarn): {{String}}
  [JoinInstruction](#cfn-quicksight-dataset-logicaltablesource-joininstruction): {{
    JoinInstruction}}
  [PhysicalTableId](#cfn-quicksight-dataset-logicaltablesource-physicaltableid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-logicaltablesource-properties"></a>

`DataSetArn`  <a name="cfn-quicksight-dataset-logicaltablesource-datasetarn"></a>
The Amazon Resource Number (ARN) of the parent dataset.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JoinInstruction`  <a name="cfn-quicksight-dataset-logicaltablesource-joininstruction"></a>
Specifies the result of a join of two logical tables.
*Required*: No
*Type*: [JoinInstruction](aws-properties-quicksight-dataset-joininstruction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PhysicalTableId`  <a name="cfn-quicksight-dataset-logicaltablesource-physicaltableid"></a>
Physical table ID.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-zA-Z-]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
