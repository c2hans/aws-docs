---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-datasetreference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DataSetReference
<a name="aws-properties-quicksight-template-datasetreference"></a>

Dataset reference.

## Syntax
<a name="aws-properties-quicksight-template-datasetreference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-datasetreference-syntax.json"></a>

```
{
  "[DataSetArn](#cfn-quicksight-template-datasetreference-datasetarn)" : {{String}},
  "[DataSetPlaceholder](#cfn-quicksight-template-datasetreference-datasetplaceholder)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-datasetreference-syntax.yaml"></a>

```
  [DataSetArn](#cfn-quicksight-template-datasetreference-datasetarn): {{String}}
  [DataSetPlaceholder](#cfn-quicksight-template-datasetreference-datasetplaceholder): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-datasetreference-properties"></a>

`DataSetArn`  <a name="cfn-quicksight-template-datasetreference-datasetarn"></a>
Dataset Amazon Resource Name (ARN).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetPlaceholder`  <a name="cfn-quicksight-template-datasetreference-datasetplaceholder"></a>
Dataset placeholder.
*Required*: Yes
*Type*: String
*Pattern*: `\S`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
