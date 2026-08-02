---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent ManualSearchAIAgentConfiguration
<a name="aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration"></a>

The configuration for AI Agents of type `MANUAL_SEARCH`.

## Syntax
<a name="aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration-syntax.json"></a>

```
{
  "[AnswerGenerationAIGuardrailId](#cfn-wisdom-aiagent-manualsearchaiagentconfiguration-answergenerationaiguardrailid)" : {{String}},
  "[AnswerGenerationAIPromptId](#cfn-wisdom-aiagent-manualsearchaiagentconfiguration-answergenerationaipromptid)" : {{String}},
  "[AssociationConfigurations](#cfn-wisdom-aiagent-manualsearchaiagentconfiguration-associationconfigurations)" : {{[ AssociationConfiguration, ... ]}},
  "[Locale](#cfn-wisdom-aiagent-manualsearchaiagentconfiguration-locale)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration-syntax.yaml"></a>

```
  [AnswerGenerationAIGuardrailId](#cfn-wisdom-aiagent-manualsearchaiagentconfiguration-answergenerationaiguardrailid): {{String}}
  [AnswerGenerationAIPromptId](#cfn-wisdom-aiagent-manualsearchaiagentconfiguration-answergenerationaipromptid): {{String}}
  [AssociationConfigurations](#cfn-wisdom-aiagent-manualsearchaiagentconfiguration-associationconfigurations): {{
    - AssociationConfiguration}}
  [Locale](#cfn-wisdom-aiagent-manualsearchaiagentconfiguration-locale): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration-properties"></a>

`AnswerGenerationAIGuardrailId`  <a name="cfn-wisdom-aiagent-manualsearchaiagentconfiguration-answergenerationaiguardrailid"></a>
The ID of the answer generation AI guardrail.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AnswerGenerationAIPromptId`  <a name="cfn-wisdom-aiagent-manualsearchaiagentconfiguration-answergenerationaipromptid"></a>
The AI Prompt identifier for the Answer Generation prompt used by the `ANSWER_RECOMMENDATION` AI Agent.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssociationConfigurations`  <a name="cfn-wisdom-aiagent-manualsearchaiagentconfiguration-associationconfigurations"></a>
The association configurations for overriding behavior on this AI Agent.
*Required*: No
*Type*: Array of [AssociationConfiguration](aws-properties-wisdom-aiagent-associationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Locale`  <a name="cfn-wisdom-aiagent-manualsearchaiagentconfiguration-locale"></a>
The locale to which specifies the language and region settings that determine the response language for [QueryAssistant](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html).
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
