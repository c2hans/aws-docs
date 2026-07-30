---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-knowledgebaseorchestrationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion KnowledgeBaseOrchestrationConfiguration
<a name="aws-properties-bedrock-flowversion-knowledgebaseorchestrationconfiguration"></a>

Configures how the knowledge base orchestrates the retrieval and generation process, allowing for customization of prompts, inference parameters, and performance settings.

## Syntax
<a name="aws-properties-bedrock-flowversion-knowledgebaseorchestrationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-knowledgebaseorchestrationconfiguration-syntax.json"></a>

```
{
  "[AdditionalModelRequestFields](#cfn-bedrock-flowversion-knowledgebaseorchestrationconfiguration-additionalmodelrequestfields)" : {{Json}},
  "[InferenceConfig](#cfn-bedrock-flowversion-knowledgebaseorchestrationconfiguration-inferenceconfig)" : {{PromptInferenceConfiguration}},
  "[PerformanceConfig](#cfn-bedrock-flowversion-knowledgebaseorchestrationconfiguration-performanceconfig)" : {{PerformanceConfiguration}},
  "[PromptTemplate](#cfn-bedrock-flowversion-knowledgebaseorchestrationconfiguration-prompttemplate)" : {{KnowledgeBasePromptTemplate}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-knowledgebaseorchestrationconfiguration-syntax.yaml"></a>

```
  [AdditionalModelRequestFields](#cfn-bedrock-flowversion-knowledgebaseorchestrationconfiguration-additionalmodelrequestfields): {{Json}}
  [InferenceConfig](#cfn-bedrock-flowversion-knowledgebaseorchestrationconfiguration-inferenceconfig): {{
    PromptInferenceConfiguration}}
  [PerformanceConfig](#cfn-bedrock-flowversion-knowledgebaseorchestrationconfiguration-performanceconfig): {{
    PerformanceConfiguration}}
  [PromptTemplate](#cfn-bedrock-flowversion-knowledgebaseorchestrationconfiguration-prompttemplate): {{
    KnowledgeBasePromptTemplate}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-knowledgebaseorchestrationconfiguration-properties"></a>

`AdditionalModelRequestFields`  <a name="cfn-bedrock-flowversion-knowledgebaseorchestrationconfiguration-additionalmodelrequestfields"></a>
The additional model-specific request parameters as key-value pairs to be included in the request to the foundation model.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InferenceConfig`  <a name="cfn-bedrock-flowversion-knowledgebaseorchestrationconfiguration-inferenceconfig"></a>
Contains inference configurations for the prompt.
*Required*: No
*Type*: [PromptInferenceConfiguration](aws-properties-bedrock-flowversion-promptinferenceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PerformanceConfig`  <a name="cfn-bedrock-flowversion-knowledgebaseorchestrationconfiguration-performanceconfig"></a>
The performance configuration options for the knowledge base retrieval and generation process.
*Required*: No
*Type*: [PerformanceConfiguration](aws-properties-bedrock-flowversion-performanceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PromptTemplate`  <a name="cfn-bedrock-flowversion-knowledgebaseorchestrationconfiguration-prompttemplate"></a>
A custom prompt template for orchestrating the retrieval and generation process.
*Required*: No
*Type*: [KnowledgeBasePromptTemplate](aws-properties-bedrock-flowversion-knowledgebaseprompttemplate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
