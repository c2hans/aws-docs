---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent AnswerRecommendationAIAgentConfiguration
<a name="aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration"></a>

The configuration for AI Agents of type `ANSWER_RECOMMENDATION`.

## Syntax
<a name="aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration-syntax.json"></a>

```
{
  "[AnswerGenerationAIGuardrailId](#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-answergenerationaiguardrailid)" : {{String}},
  "[AnswerGenerationAIPromptId](#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-answergenerationaipromptid)" : {{String}},
  "[AssociationConfigurations](#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-associationconfigurations)" : {{[ AssociationConfiguration, ... ]}},
  "[IntentLabelingGenerationAIPromptId](#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-intentlabelinggenerationaipromptid)" : {{String}},
  "[Locale](#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-locale)" : {{String}},
  "[QueryReformulationAIPromptId](#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-queryreformulationaipromptid)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration-syntax.yaml"></a>

```
  [AnswerGenerationAIGuardrailId](#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-answergenerationaiguardrailid): {{String}}
  [AnswerGenerationAIPromptId](#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-answergenerationaipromptid): {{String}}
  [AssociationConfigurations](#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-associationconfigurations): {{
    - AssociationConfiguration}}
  [IntentLabelingGenerationAIPromptId](#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-intentlabelinggenerationaipromptid): {{String}}
  [Locale](#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-locale): {{String}}
  [QueryReformulationAIPromptId](#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-queryreformulationaipromptid): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration-properties"></a>

`AnswerGenerationAIGuardrailId`  <a name="cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-answergenerationaiguardrailid"></a>
The ID of the answer generation AI guardrail.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AnswerGenerationAIPromptId`  <a name="cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-answergenerationaipromptid"></a>
The AI Prompt identifier for the Answer Generation prompt used by the `ANSWER_RECOMMENDATION` AI Agent.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssociationConfigurations`  <a name="cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-associationconfigurations"></a>
The association configurations for overriding behavior on this AI Agent.
*Required*: No
*Type*: Array of [AssociationConfiguration](aws-properties-wisdom-aiagent-associationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntentLabelingGenerationAIPromptId`  <a name="cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-intentlabelinggenerationaipromptid"></a>
The AI Prompt identifier for the Intent Labeling prompt used by the `ANSWER_RECOMMENDATION` AI Agent.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Locale`  <a name="cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-locale"></a>
The locale to which specifies the language and region settings that determine the response language for [QueryAssistant](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html).
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryReformulationAIPromptId`  <a name="cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-queryreformulationaipromptid"></a>
The AI Prompt identifier for the Query Reformulation prompt used by the `ANSWER_RECOMMENDATION` AI Agent.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
