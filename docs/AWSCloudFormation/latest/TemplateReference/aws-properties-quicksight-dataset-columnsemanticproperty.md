---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-columnsemanticproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet ColumnSemanticProperty
<a name="aws-properties-quicksight-dataset-columnsemanticproperty"></a>

A semantic property for a column.

## Syntax
<a name="aws-properties-quicksight-dataset-columnsemanticproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-columnsemanticproperty-syntax.json"></a>

```
{
  "[AdditionalNotes](#cfn-quicksight-dataset-columnsemanticproperty-additionalnotes)" : {{AdditionalNotes}},
  "[Description](#cfn-quicksight-dataset-columnsemanticproperty-description)" : {{ColumnDescription}},
  "[SemanticType](#cfn-quicksight-dataset-columnsemanticproperty-semantictype)" : {{ColumnSemanticType}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-columnsemanticproperty-syntax.yaml"></a>

```
  [AdditionalNotes](#cfn-quicksight-dataset-columnsemanticproperty-additionalnotes): {{
    AdditionalNotes}}
  [Description](#cfn-quicksight-dataset-columnsemanticproperty-description): {{
    ColumnDescription}}
  [SemanticType](#cfn-quicksight-dataset-columnsemanticproperty-semantictype): {{
    ColumnSemanticType}}
```

## Properties
<a name="aws-properties-quicksight-dataset-columnsemanticproperty-properties"></a>

`AdditionalNotes`  <a name="cfn-quicksight-dataset-columnsemanticproperty-additionalnotes"></a>
Additional notes for the column.
*Required*: No
*Type*: [AdditionalNotes](aws-properties-quicksight-dataset-additionalnotes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-quicksight-dataset-columnsemanticproperty-description"></a>
A description of the column.
*Required*: No
*Type*: [ColumnDescription](aws-properties-quicksight-dataset-columndescription.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SemanticType`  <a name="cfn-quicksight-dataset-columnsemanticproperty-semantictype"></a>
The semantic type of the column.
*Required*: No
*Type*: [ColumnSemanticType](aws-properties-quicksight-dataset-columnsemantictype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
