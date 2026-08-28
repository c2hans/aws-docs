---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datapipeline-pipeline-pipelineobject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataPipeline::Pipeline PipelineObject
<a name="aws-properties-datapipeline-pipeline-pipelineobject"></a>

PipelineObject is property of the AWS::DataPipeline::Pipeline resource that contains information about a pipeline object. This can be a logical, physical, or physical attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

## Syntax
<a name="aws-properties-datapipeline-pipeline-pipelineobject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datapipeline-pipeline-pipelineobject-syntax.json"></a>

```
{
  "[Fields](#cfn-datapipeline-pipeline-pipelineobject-fields)" : {{[ Field, ... ]}},
  "[Id](#cfn-datapipeline-pipeline-pipelineobject-id)" : {{String}},
  "[Name](#cfn-datapipeline-pipeline-pipelineobject-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-datapipeline-pipeline-pipelineobject-syntax.yaml"></a>

```
  [Fields](#cfn-datapipeline-pipeline-pipelineobject-fields): {{
    - Field}}
  [Id](#cfn-datapipeline-pipeline-pipelineobject-id): {{String}}
  [Name](#cfn-datapipeline-pipeline-pipelineobject-name): {{String}}
```

## Properties
<a name="aws-properties-datapipeline-pipeline-pipelineobject-properties"></a>

`Fields`  <a name="cfn-datapipeline-pipeline-pipelineobject-fields"></a>
Key-value pairs that define the properties of the object.
*Required*: Yes
*Type*: Array of [Field](aws-properties-datapipeline-pipeline-field.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-datapipeline-pipeline-pipelineobject-id"></a>
The ID of the object.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-datapipeline-pipeline-pipelineobject-name"></a>
The name of the object.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
