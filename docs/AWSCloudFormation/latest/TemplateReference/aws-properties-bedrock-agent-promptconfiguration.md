---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-promptconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent PromptConfiguration
<a name="aws-properties-bedrock-agent-promptconfiguration"></a>

 Contains configurations to override a prompt template in one part of an agent sequence. For more information, see [Advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html).

## Syntax
<a name="aws-properties-bedrock-agent-promptconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-promptconfiguration-syntax.json"></a>

```
{
  "[AdditionalModelRequestFields](#cfn-bedrock-agent-promptconfiguration-additionalmodelrequestfields)" : {{Json}},
  "[BasePromptTemplate](#cfn-bedrock-agent-promptconfiguration-baseprompttemplate)" : {{String}},
  "[FoundationModel](#cfn-bedrock-agent-promptconfiguration-foundationmodel)" : {{String}},
  "[InferenceConfiguration](#cfn-bedrock-agent-promptconfiguration-inferenceconfiguration)" : {{InferenceConfiguration}},
  "[ParserMode](#cfn-bedrock-agent-promptconfiguration-parsermode)" : {{String}},
  "[PromptCreationMode](#cfn-bedrock-agent-promptconfiguration-promptcreationmode)" : {{String}},
  "[PromptState](#cfn-bedrock-agent-promptconfiguration-promptstate)" : {{String}},
  "[PromptType](#cfn-bedrock-agent-promptconfiguration-prompttype)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-promptconfiguration-syntax.yaml"></a>

```
  [AdditionalModelRequestFields](#cfn-bedrock-agent-promptconfiguration-additionalmodelrequestfields): {{Json}}
  [BasePromptTemplate](#cfn-bedrock-agent-promptconfiguration-baseprompttemplate): {{String}}
  [FoundationModel](#cfn-bedrock-agent-promptconfiguration-foundationmodel): {{String}}
  [InferenceConfiguration](#cfn-bedrock-agent-promptconfiguration-inferenceconfiguration): {{
    InferenceConfiguration}}
  [ParserMode](#cfn-bedrock-agent-promptconfiguration-parsermode): {{String}}
  [PromptCreationMode](#cfn-bedrock-agent-promptconfiguration-promptcreationmode): {{String}}
  [PromptState](#cfn-bedrock-agent-promptconfiguration-promptstate): {{String}}
  [PromptType](#cfn-bedrock-agent-promptconfiguration-prompttype): {{String}}
```

## Properties
<a name="aws-properties-bedrock-agent-promptconfiguration-properties"></a>

`AdditionalModelRequestFields`  <a name="cfn-bedrock-agent-promptconfiguration-additionalmodelrequestfields"></a>
If the Converse or ConverseStream operations support the model, `additionalModelRequestFields` contains additional inference parameters, beyond the base set of inference parameters in the `inferenceConfiguration` field.
For more information, see [Inference request parameters and response fields for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BasePromptTemplate`  <a name="cfn-bedrock-agent-promptconfiguration-baseprompttemplate"></a>
Defines the prompt template with which to replace the default prompt template. You can use placeholder variables in the base prompt template to customize the prompt. For more information, see [Prompt template placeholder variables](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-placeholders.html). For more information, see [Configure the prompt templates](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts-configure.html).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FoundationModel`  <a name="cfn-bedrock-agent-promptconfiguration-foundationmodel"></a>
The agent's foundation model.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}))|([0-9]{12}:(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+))|(([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}))|(([0-9a-zA-Z][_-]?)+)$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InferenceConfiguration`  <a name="cfn-bedrock-agent-promptconfiguration-inferenceconfiguration"></a>
Contains inference parameters to use when the agent invokes a foundation model in the part of the agent sequence defined by the `promptType`. For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).
*Required*: No
*Type*: [InferenceConfiguration](aws-properties-bedrock-agent-inferenceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParserMode`  <a name="cfn-bedrock-agent-promptconfiguration-parsermode"></a>
Specifies whether to override the default parser Lambda function when parsing the raw foundation model output in the part of the agent sequence defined by the `promptType`. If you set the field as `OVERRIDDEN`, the `overrideLambda` field in the [PromptOverrideConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptOverrideConfiguration.html) must be specified with the ARN of a Lambda function.
*Required*: No
*Type*: String
*Allowed values*: `DEFAULT | OVERRIDDEN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PromptCreationMode`  <a name="cfn-bedrock-agent-promptconfiguration-promptcreationmode"></a>
Specifies whether to override the default prompt template for this `promptType`. Set this value to `OVERRIDDEN` to use the prompt that you provide in the `basePromptTemplate`. If you leave it as `DEFAULT`, the agent uses a default prompt template.
*Required*: No
*Type*: String
*Allowed values*: `DEFAULT | OVERRIDDEN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PromptState`  <a name="cfn-bedrock-agent-promptconfiguration-promptstate"></a>
Specifies whether to allow the inline agent to carry out the step specified in the `promptType`. If you set this value to `DISABLED`, the agent skips that step. The default state for each `promptType` is as follows.
+ `PRE_PROCESSING` – `ENABLED`
+ `ORCHESTRATION` – `ENABLED`
+ `KNOWLEDGE_BASE_RESPONSE_GENERATION` – `ENABLED`
+ `POST_PROCESSING` – `DISABLED`
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PromptType`  <a name="cfn-bedrock-agent-promptconfiguration-prompttype"></a>
 The step in the agent sequence that this prompt configuration applies to.
*Required*: No
*Type*: String
*Allowed values*: `PRE_PROCESSING | ORCHESTRATION | POST_PROCESSING | ROUTING_CLASSIFIER | MEMORY_SUMMARIZATION | KNOWLEDGE_BASE_RESPONSE_GENERATION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
