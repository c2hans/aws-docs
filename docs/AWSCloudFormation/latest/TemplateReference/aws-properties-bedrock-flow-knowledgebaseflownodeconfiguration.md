---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-knowledgebaseflownodeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow KnowledgeBaseFlowNodeConfiguration
<a name="aws-properties-bedrock-flow-knowledgebaseflownodeconfiguration"></a>

Contains configurations for a knowledge base node in a flow. This node takes a query as the input and returns, as the output, the retrieved responses directly (as an array) or a response generated based on the retrieved responses. For more information, see [Node types in a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-flow-knowledgebaseflownodeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-knowledgebaseflownodeconfiguration-syntax.json"></a>

```
{
  "[GuardrailConfiguration](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-guardrailconfiguration)" : {{GuardrailConfiguration}},
  "[InferenceConfiguration](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-inferenceconfiguration)" : {{PromptInferenceConfiguration}},
  "[KnowledgeBaseId](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-knowledgebaseid)" : {{String}},
  "[ModelId](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-modelid)" : {{String}},
  "[NumberOfResults](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-numberofresults)" : {{Number}},
  "[OrchestrationConfiguration](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-orchestrationconfiguration)" : {{KnowledgeBaseOrchestrationConfiguration}},
  "[PromptTemplate](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-prompttemplate)" : {{KnowledgeBasePromptTemplate}},
  "[RerankingConfiguration](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-rerankingconfiguration)" : {{VectorSearchRerankingConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-knowledgebaseflownodeconfiguration-syntax.yaml"></a>

```
  [GuardrailConfiguration](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-guardrailconfiguration): {{
    GuardrailConfiguration}}
  [InferenceConfiguration](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-inferenceconfiguration): {{
    PromptInferenceConfiguration}}
  [KnowledgeBaseId](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-knowledgebaseid): {{String}}
  [ModelId](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-modelid): {{String}}
  [NumberOfResults](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-numberofresults): {{
    Number}}
  [OrchestrationConfiguration](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-orchestrationconfiguration): {{
    KnowledgeBaseOrchestrationConfiguration}}
  [PromptTemplate](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-prompttemplate): {{
    KnowledgeBasePromptTemplate}}
  [RerankingConfiguration](#cfn-bedrock-flow-knowledgebaseflownodeconfiguration-rerankingconfiguration): {{
    VectorSearchRerankingConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-flow-knowledgebaseflownodeconfiguration-properties"></a>

`GuardrailConfiguration`  <a name="cfn-bedrock-flow-knowledgebaseflownodeconfiguration-guardrailconfiguration"></a>
Contains configurations for a guardrail to apply during query and response generation for the knowledge base in this configuration.
*Required*: No
*Type*: [GuardrailConfiguration](aws-properties-bedrock-flow-guardrailconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InferenceConfiguration`  <a name="cfn-bedrock-flow-knowledgebaseflownodeconfiguration-inferenceconfiguration"></a>
Contains inference configurations for the prompt.
*Required*: No
*Type*: [PromptInferenceConfiguration](aws-properties-bedrock-flow-promptinferenceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KnowledgeBaseId`  <a name="cfn-bedrock-flow-knowledgebaseflownodeconfiguration-knowledgebaseid"></a>
The unique identifier of the knowledge base to query.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z]+$`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelId`  <a name="cfn-bedrock-flow-knowledgebaseflownodeconfiguration-modelid"></a>
The unique identifier of the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to use to generate a response from the query results. Omit this field if you want to return the retrieved results as an array.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws(-[^:]{1,12})?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberOfResults`  <a name="cfn-bedrock-flow-knowledgebaseflownodeconfiguration-numberofresults"></a>
The number of results to retrieve from the knowledge base.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrchestrationConfiguration`  <a name="cfn-bedrock-flow-knowledgebaseflownodeconfiguration-orchestrationconfiguration"></a>
The configuration for orchestrating the retrieval and generation process in the knowledge base node.
*Required*: No
*Type*: [KnowledgeBaseOrchestrationConfiguration](aws-properties-bedrock-flow-knowledgebaseorchestrationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PromptTemplate`  <a name="cfn-bedrock-flow-knowledgebaseflownodeconfiguration-prompttemplate"></a>
A custom prompt template to use with the knowledge base for generating responses.
*Required*: No
*Type*: [KnowledgeBasePromptTemplate](aws-properties-bedrock-flow-knowledgebaseprompttemplate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RerankingConfiguration`  <a name="cfn-bedrock-flow-knowledgebaseflownodeconfiguration-rerankingconfiguration"></a>
The configuration for reranking the retrieved results from the knowledge base to improve relevance.
*Required*: No
*Type*: [VectorSearchRerankingConfiguration](aws-properties-bedrock-flow-vectorsearchrerankingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
