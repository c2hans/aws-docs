---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-sagemakerpipelineparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe SageMakerPipelineParameter
<a name="aws-properties-pipes-pipe-sagemakerpipelineparameter"></a>

Name/Value pair of a parameter to start execution of a SageMaker AI Model Building Pipeline.

## Syntax
<a name="aws-properties-pipes-pipe-sagemakerpipelineparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-sagemakerpipelineparameter-syntax.json"></a>

```
{
  "[Name](#cfn-pipes-pipe-sagemakerpipelineparameter-name)" : {{String}},
  "[Value](#cfn-pipes-pipe-sagemakerpipelineparameter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-sagemakerpipelineparameter-syntax.yaml"></a>

```
  [Name](#cfn-pipes-pipe-sagemakerpipelineparameter-name): {{String}}
  [Value](#cfn-pipes-pipe-sagemakerpipelineparameter-value): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-sagemakerpipelineparameter-properties"></a>

`Name`  <a name="cfn-pipes-pipe-sagemakerpipelineparameter-name"></a>
Name of parameter to start execution of a SageMaker AI Model Building Pipeline.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-pipes-pipe-sagemakerpipelineparameter-value"></a>
Value of parameter to start execution of a SageMaker AI Model Building Pipeline.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
