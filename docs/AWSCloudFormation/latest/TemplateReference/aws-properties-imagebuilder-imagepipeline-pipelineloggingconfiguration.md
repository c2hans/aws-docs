---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-imagepipeline-pipelineloggingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ImagePipeline PipelineLoggingConfiguration
<a name="aws-properties-imagebuilder-imagepipeline-pipelineloggingconfiguration"></a>

The logging configuration that's defined for pipeline execution.

## Syntax
<a name="aws-properties-imagebuilder-imagepipeline-pipelineloggingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-imagepipeline-pipelineloggingconfiguration-syntax.json"></a>

```
{
  "[ImageLogGroupName](#cfn-imagebuilder-imagepipeline-pipelineloggingconfiguration-imageloggroupname)" : {{String}},
  "[PipelineLogGroupName](#cfn-imagebuilder-imagepipeline-pipelineloggingconfiguration-pipelineloggroupname)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-imagepipeline-pipelineloggingconfiguration-syntax.yaml"></a>

```
  [ImageLogGroupName](#cfn-imagebuilder-imagepipeline-pipelineloggingconfiguration-imageloggroupname): {{String}}
  [PipelineLogGroupName](#cfn-imagebuilder-imagepipeline-pipelineloggingconfiguration-pipelineloggroupname): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-imagepipeline-pipelineloggingconfiguration-properties"></a>

`ImageLogGroupName`  <a name="cfn-imagebuilder-imagepipeline-pipelineloggingconfiguration-imageloggroupname"></a>
Specifies the CloudWatch Logs log group name for image build logs. The log group name can contain alphanumeric characters, hyphens, underscores, forward slashes, and periods, up to 512 characters. Log group names not starting with `/aws/imagebuilder/` require an `executionRole` with CloudWatch Logs write permissions. If not specified, defaults to `/aws/imagebuilder/image-name`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-_/\.]{1,512}$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PipelineLogGroupName`  <a name="cfn-imagebuilder-imagepipeline-pipelineloggingconfiguration-pipelineloggroupname"></a>
Specifies the CloudWatch Logs log group name for pipeline execution logs. The log group name can contain alphanumeric characters, hyphens, underscores, forward slashes, and periods, up to 512 characters. Log group names not starting with `/aws/imagebuilder/` require an `executionRole` with CloudWatch Logs write permissions. If not specified, defaults to `/aws/imagebuilder/pipeline/pipeline-name`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-_/\.]{1,512}$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
