---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-flownodeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion FlowNodeConfiguration
<a name="aws-properties-bedrock-flowversion-flownodeconfiguration"></a>

Contains configurations for a node in your flow. For more information, see [Node types in a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-flowversion-flownodeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-flownodeconfiguration-syntax.json"></a>

```
{
  "[Agent](#cfn-bedrock-flowversion-flownodeconfiguration-agent)" : {{AgentFlowNodeConfiguration}},
  "[Collector](#cfn-bedrock-flowversion-flownodeconfiguration-collector)" : {{Json}},
  "[Condition](#cfn-bedrock-flowversion-flownodeconfiguration-condition)" : {{ConditionFlowNodeConfiguration}},
  "[InlineCode](#cfn-bedrock-flowversion-flownodeconfiguration-inlinecode)" : {{InlineCodeFlowNodeConfiguration}},
  "[Input](#cfn-bedrock-flowversion-flownodeconfiguration-input)" : {{Json}},
  "[Iterator](#cfn-bedrock-flowversion-flownodeconfiguration-iterator)" : {{Json}},
  "[KnowledgeBase](#cfn-bedrock-flowversion-flownodeconfiguration-knowledgebase)" : {{KnowledgeBaseFlowNodeConfiguration}},
  "[LambdaFunction](#cfn-bedrock-flowversion-flownodeconfiguration-lambdafunction)" : {{LambdaFunctionFlowNodeConfiguration}},
  "[Lex](#cfn-bedrock-flowversion-flownodeconfiguration-lex)" : {{LexFlowNodeConfiguration}},
  "[Loop](#cfn-bedrock-flowversion-flownodeconfiguration-loop)" : {{LoopFlowNodeConfiguration}},
  "[LoopController](#cfn-bedrock-flowversion-flownodeconfiguration-loopcontroller)" : {{LoopControllerFlowNodeConfiguration}},
  "[LoopInput](#cfn-bedrock-flowversion-flownodeconfiguration-loopinput)" : {{Json}},
  "[Output](#cfn-bedrock-flowversion-flownodeconfiguration-output)" : {{Json}},
  "[Prompt](#cfn-bedrock-flowversion-flownodeconfiguration-prompt)" : {{PromptFlowNodeConfiguration}},
  "[Retrieval](#cfn-bedrock-flowversion-flownodeconfiguration-retrieval)" : {{RetrievalFlowNodeConfiguration}},
  "[Storage](#cfn-bedrock-flowversion-flownodeconfiguration-storage)" : {{StorageFlowNodeConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-flownodeconfiguration-syntax.yaml"></a>

```
  [Agent](#cfn-bedrock-flowversion-flownodeconfiguration-agent): {{
    AgentFlowNodeConfiguration}}
  [Collector](#cfn-bedrock-flowversion-flownodeconfiguration-collector): {{Json}}
  [Condition](#cfn-bedrock-flowversion-flownodeconfiguration-condition): {{
    ConditionFlowNodeConfiguration}}
  [InlineCode](#cfn-bedrock-flowversion-flownodeconfiguration-inlinecode): {{
    InlineCodeFlowNodeConfiguration}}
  [Input](#cfn-bedrock-flowversion-flownodeconfiguration-input): {{Json}}
  [Iterator](#cfn-bedrock-flowversion-flownodeconfiguration-iterator): {{Json}}
  [KnowledgeBase](#cfn-bedrock-flowversion-flownodeconfiguration-knowledgebase): {{
    KnowledgeBaseFlowNodeConfiguration}}
  [LambdaFunction](#cfn-bedrock-flowversion-flownodeconfiguration-lambdafunction): {{
    LambdaFunctionFlowNodeConfiguration}}
  [Lex](#cfn-bedrock-flowversion-flownodeconfiguration-lex): {{
    LexFlowNodeConfiguration}}
  [Loop](#cfn-bedrock-flowversion-flownodeconfiguration-loop): {{
    LoopFlowNodeConfiguration}}
  [LoopController](#cfn-bedrock-flowversion-flownodeconfiguration-loopcontroller): {{
    LoopControllerFlowNodeConfiguration}}
  [LoopInput](#cfn-bedrock-flowversion-flownodeconfiguration-loopinput): {{Json}}
  [Output](#cfn-bedrock-flowversion-flownodeconfiguration-output): {{Json}}
  [Prompt](#cfn-bedrock-flowversion-flownodeconfiguration-prompt): {{
    PromptFlowNodeConfiguration}}
  [Retrieval](#cfn-bedrock-flowversion-flownodeconfiguration-retrieval): {{
    RetrievalFlowNodeConfiguration}}
  [Storage](#cfn-bedrock-flowversion-flownodeconfiguration-storage): {{
    StorageFlowNodeConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-flownodeconfiguration-properties"></a>

`Agent`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-agent"></a>
Contains configurations for an agent node in your flow. Invokes an alias of an agent and returns the response.
*Required*: No
*Type*: [AgentFlowNodeConfiguration](aws-properties-bedrock-flowversion-agentflownodeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Collector`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-collector"></a>
Contains configurations for a collector node in your flow. Collects an iteration of inputs and consolidates them into an array of outputs.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Condition`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-condition"></a>
Contains configurations for a condition node in your flow. Defines conditions that lead to different branches of the flow.
*Required*: No
*Type*: [ConditionFlowNodeConfiguration](aws-properties-bedrock-flowversion-conditionflownodeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InlineCode`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-inlinecode"></a>
Contains configurations for an inline code node in your flow. Inline code nodes let you write and execute code directly within your flow, enabling data transformations, custom logic, and integrations without needing an external Lambda function.
*Required*: No
*Type*: [InlineCodeFlowNodeConfiguration](aws-properties-bedrock-flowversion-inlinecodeflownodeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Input`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-input"></a>
Contains configurations for an input flow node in your flow. The first node in the flow. `inputs` can't be specified for this node.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Iterator`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-iterator"></a>
Contains configurations for an iterator node in your flow. Takes an input that is an array and iteratively sends each item of the array as an output to the following node. The size of the array is also returned in the output.
The output flow node at the end of the flow iteration will return a response for each member of the array. To return only one response, you can include a collector node downstream from the iterator node.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KnowledgeBase`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-knowledgebase"></a>
Contains configurations for a knowledge base node in your flow. Queries a knowledge base and returns the retrieved results or generated response.
*Required*: No
*Type*: [KnowledgeBaseFlowNodeConfiguration](aws-properties-bedrock-flowversion-knowledgebaseflownodeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LambdaFunction`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-lambdafunction"></a>
Contains configurations for a Lambda function node in your flow. Invokes an AWS Lambda function.
*Required*: No
*Type*: [LambdaFunctionFlowNodeConfiguration](aws-properties-bedrock-flowversion-lambdafunctionflownodeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Lex`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-lex"></a>
Contains configurations for a Lex node in your flow. Invokes an Amazon Lex bot to identify the intent of the input and return the intent as the output.
*Required*: No
*Type*: [LexFlowNodeConfiguration](aws-properties-bedrock-flowversion-lexflownodeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Loop`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-loop"></a>
Contains configurations for a DoWhile loop in your flow.
*Required*: No
*Type*: [LoopFlowNodeConfiguration](aws-properties-bedrock-flowversion-loopflownodeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoopController`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-loopcontroller"></a>
Contains controller node configurations for a DoWhile loop in your flow.
*Required*: No
*Type*: [LoopControllerFlowNodeConfiguration](aws-properties-bedrock-flowversion-loopcontrollerflownodeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoopInput`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-loopinput"></a>
Contains input node configurations for a DoWhile loop in your flow.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Output`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-output"></a>
Contains configurations for an output flow node in your flow. The last node in the flow. `outputs` can't be specified for this node.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prompt`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-prompt"></a>
Contains configurations for a prompt node in your flow. Runs a prompt and generates the model response as the output. You can use a prompt from Prompt management or you can configure one in this node.
*Required*: No
*Type*: [PromptFlowNodeConfiguration](aws-properties-bedrock-flowversion-promptflownodeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Retrieval`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-retrieval"></a>
Contains configurations for a retrieval node in your flow. Retrieves data from an Amazon S3 location and returns it as the output.
*Required*: No
*Type*: [RetrievalFlowNodeConfiguration](aws-properties-bedrock-flowversion-retrievalflownodeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Storage`  <a name="cfn-bedrock-flowversion-flownodeconfiguration-storage"></a>
Contains configurations for a storage node in your flow. Stores an input in an Amazon S3 location.
*Required*: No
*Type*: [StorageFlowNodeConfiguration](aws-properties-bedrock-flowversion-storageflownodeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
