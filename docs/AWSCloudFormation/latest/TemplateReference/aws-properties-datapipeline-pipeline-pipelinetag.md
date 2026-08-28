---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datapipeline-pipeline-pipelinetag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataPipeline::Pipeline PipelineTag
<a name="aws-properties-datapipeline-pipeline-pipelinetag"></a>

A list of arbitrary tags (key-value pairs) to associate with the pipeline, which you can use to control permissions. For more information, see [Controlling Access to Pipelines and Resources](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html) in the *AWS Data Pipeline Developer Guide*.

## Syntax
<a name="aws-properties-datapipeline-pipeline-pipelinetag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datapipeline-pipeline-pipelinetag-syntax.json"></a>

```
{
  "[Key](#cfn-datapipeline-pipeline-pipelinetag-key)" : {{String}},
  "[Value](#cfn-datapipeline-pipeline-pipelinetag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-datapipeline-pipeline-pipelinetag-syntax.yaml"></a>

```
  [Key](#cfn-datapipeline-pipeline-pipelinetag-key): {{String}}
  [Value](#cfn-datapipeline-pipeline-pipelinetag-value): {{String}}
```

## Properties
<a name="aws-properties-datapipeline-pipeline-pipelinetag-properties"></a>

`Key`  <a name="cfn-datapipeline-pipeline-pipelinetag-key"></a>
The key name of a tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-datapipeline-pipeline-pipelinetag-value"></a>
The value to associate with the key name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
