---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-custominstruction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet CustomInstruction
<a name="aws-properties-quicksight-dataset-custominstruction"></a>

A custom instruction that provides guidance on how the dataset should be consumed.

## Syntax
<a name="aws-properties-quicksight-dataset-custominstruction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-custominstruction-syntax.json"></a>

```
{
  "[InlineCustomInstruction](#cfn-quicksight-dataset-custominstruction-inlinecustominstruction)" : {{InlineCustomInstruction}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-custominstruction-syntax.yaml"></a>

```
  [InlineCustomInstruction](#cfn-quicksight-dataset-custominstruction-inlinecustominstruction): {{
    InlineCustomInstruction}}
```

## Properties
<a name="aws-properties-quicksight-dataset-custominstruction-properties"></a>

`InlineCustomInstruction`  <a name="cfn-quicksight-dataset-custominstruction-inlinecustominstruction"></a>
An inline custom instruction containing text and optional uploaded document metadata.
*Required*: No
*Type*: [InlineCustomInstruction](aws-properties-quicksight-dataset-inlinecustominstruction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
