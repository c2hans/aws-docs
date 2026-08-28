---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-promptflownodeinlineconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion PromptFlowNodeInlineConfiguration
<a name="aws-properties-bedrock-flowversion-promptflownodeinlineconfiguration"></a>

Contains configurations for a prompt defined inline in the node.

## Syntax
<a name="aws-properties-bedrock-flowversion-promptflownodeinlineconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-promptflownodeinlineconfiguration-syntax.json"></a>

```
{
  "[InferenceConfiguration](#cfn-bedrock-flowversion-promptflownodeinlineconfiguration-inferenceconfiguration)" : {{PromptInferenceConfiguration}},
  "[ModelId](#cfn-bedrock-flowversion-promptflownodeinlineconfiguration-modelid)" : {{String}},
  "[TemplateConfiguration](#cfn-bedrock-flowversion-promptflownodeinlineconfiguration-templateconfiguration)" : {{PromptTemplateConfiguration}},
  "[TemplateType](#cfn-bedrock-flowversion-promptflownodeinlineconfiguration-templatetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-promptflownodeinlineconfiguration-syntax.yaml"></a>

```
  [InferenceConfiguration](#cfn-bedrock-flowversion-promptflownodeinlineconfiguration-inferenceconfiguration): {{
    PromptInferenceConfiguration}}
  [ModelId](#cfn-bedrock-flowversion-promptflownodeinlineconfiguration-modelid): {{String}}
  [TemplateConfiguration](#cfn-bedrock-flowversion-promptflownodeinlineconfiguration-templateconfiguration): {{
    PromptTemplateConfiguration}}
  [TemplateType](#cfn-bedrock-flowversion-promptflownodeinlineconfiguration-templatetype): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-promptflownodeinlineconfiguration-properties"></a>

`InferenceConfiguration`  <a name="cfn-bedrock-flowversion-promptflownodeinlineconfiguration-inferenceconfiguration"></a>
Contains inference configurations for the prompt.
*Required*: No
*Type*: [PromptInferenceConfiguration](aws-properties-bedrock-flowversion-promptinferenceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelId`  <a name="cfn-bedrock-flowversion-promptflownodeinlineconfiguration-modelid"></a>
The unique identifier of the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to run inference with.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws(-[^:]{1,12})?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateConfiguration`  <a name="cfn-bedrock-flowversion-promptflownodeinlineconfiguration-templateconfiguration"></a>
Contains a prompt and variables in the prompt that can be replaced with values at runtime.
*Required*: Yes
*Type*: [PromptTemplateConfiguration](aws-properties-bedrock-flowversion-prompttemplateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateType`  <a name="cfn-bedrock-flowversion-promptflownodeinlineconfiguration-templatetype"></a>
The type of prompt template.
*Required*: Yes
*Type*: String
*Allowed values*: `TEXT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
