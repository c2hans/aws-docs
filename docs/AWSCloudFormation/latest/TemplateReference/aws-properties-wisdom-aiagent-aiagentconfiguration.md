---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-aiagentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent AIAgentConfiguration
<a name="aws-properties-wisdom-aiagent-aiagentconfiguration"></a>

A typed union that specifies the configuration based on the type of AI Agent.

## Syntax
<a name="aws-properties-wisdom-aiagent-aiagentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-aiagentconfiguration-syntax.json"></a>

```
{
  "[AnswerRecommendationAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-answerrecommendationaiagentconfiguration)" : {{AnswerRecommendationAIAgentConfiguration}},
  "[CaseSummarizationAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-casesummarizationaiagentconfiguration)" : {{CaseSummarizationAIAgentConfiguration}},
  "[EmailGenerativeAnswerAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-emailgenerativeansweraiagentconfiguration)" : {{EmailGenerativeAnswerAIAgentConfiguration}},
  "[EmailOverviewAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-emailoverviewaiagentconfiguration)" : {{EmailOverviewAIAgentConfiguration}},
  "[EmailResponseAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-emailresponseaiagentconfiguration)" : {{EmailResponseAIAgentConfiguration}},
  "[ManualSearchAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-manualsearchaiagentconfiguration)" : {{ManualSearchAIAgentConfiguration}},
  "[NoteTakingAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-notetakingaiagentconfiguration)" : {{NoteTakingAIAgentConfiguration}},
  "[OrchestrationAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-orchestrationaiagentconfiguration)" : {{OrchestrationAIAgentConfiguration}},
  "[SelfServiceAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-selfserviceaiagentconfiguration)" : {{SelfServiceAIAgentConfiguration}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-aiagentconfiguration-syntax.yaml"></a>

```
  [AnswerRecommendationAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-answerrecommendationaiagentconfiguration): {{
    AnswerRecommendationAIAgentConfiguration}}
  [CaseSummarizationAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-casesummarizationaiagentconfiguration): {{
    CaseSummarizationAIAgentConfiguration}}
  [EmailGenerativeAnswerAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-emailgenerativeansweraiagentconfiguration): {{
    EmailGenerativeAnswerAIAgentConfiguration}}
  [EmailOverviewAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-emailoverviewaiagentconfiguration): {{
    EmailOverviewAIAgentConfiguration}}
  [EmailResponseAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-emailresponseaiagentconfiguration): {{
    EmailResponseAIAgentConfiguration}}
  [ManualSearchAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-manualsearchaiagentconfiguration): {{
    ManualSearchAIAgentConfiguration}}
  [NoteTakingAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-notetakingaiagentconfiguration): {{
    NoteTakingAIAgentConfiguration}}
  [OrchestrationAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-orchestrationaiagentconfiguration): {{
    OrchestrationAIAgentConfiguration}}
  [SelfServiceAIAgentConfiguration](#cfn-wisdom-aiagent-aiagentconfiguration-selfserviceaiagentconfiguration): {{
    SelfServiceAIAgentConfiguration}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-aiagentconfiguration-properties"></a>

`AnswerRecommendationAIAgentConfiguration`  <a name="cfn-wisdom-aiagent-aiagentconfiguration-answerrecommendationaiagentconfiguration"></a>
The configuration for AI Agents of type `ANSWER_RECOMMENDATION`.
*Required*: No
*Type*: [AnswerRecommendationAIAgentConfiguration](aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CaseSummarizationAIAgentConfiguration`  <a name="cfn-wisdom-aiagent-aiagentconfiguration-casesummarizationaiagentconfiguration"></a>
The configuration for AI Agents of type `CASE_SUMMARIZATION`.
*Required*: No
*Type*: [CaseSummarizationAIAgentConfiguration](aws-properties-wisdom-aiagent-casesummarizationaiagentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailGenerativeAnswerAIAgentConfiguration`  <a name="cfn-wisdom-aiagent-aiagentconfiguration-emailgenerativeansweraiagentconfiguration"></a>
The configuration for AI Agents of type `EMAIL_GENERATIVE_ANSWER`.
*Required*: No
*Type*: [EmailGenerativeAnswerAIAgentConfiguration](aws-properties-wisdom-aiagent-emailgenerativeansweraiagentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailOverviewAIAgentConfiguration`  <a name="cfn-wisdom-aiagent-aiagentconfiguration-emailoverviewaiagentconfiguration"></a>
The configuration for AI Agents of type `EMAIL_OVERVIEW`.
*Required*: No
*Type*: [EmailOverviewAIAgentConfiguration](aws-properties-wisdom-aiagent-emailoverviewaiagentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailResponseAIAgentConfiguration`  <a name="cfn-wisdom-aiagent-aiagentconfiguration-emailresponseaiagentconfiguration"></a>
The configuration for AI Agents of type `EMAIL_RESPONSE`.
*Required*: No
*Type*: [EmailResponseAIAgentConfiguration](aws-properties-wisdom-aiagent-emailresponseaiagentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManualSearchAIAgentConfiguration`  <a name="cfn-wisdom-aiagent-aiagentconfiguration-manualsearchaiagentconfiguration"></a>
The configuration for AI Agents of type `MANUAL_SEARCH`.
*Required*: No
*Type*: [ManualSearchAIAgentConfiguration](aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NoteTakingAIAgentConfiguration`  <a name="cfn-wisdom-aiagent-aiagentconfiguration-notetakingaiagentconfiguration"></a>
The configuration for AI Agents of type `NOTE_TAKING`.
*Required*: No
*Type*: [NoteTakingAIAgentConfiguration](aws-properties-wisdom-aiagent-notetakingaiagentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrchestrationAIAgentConfiguration`  <a name="cfn-wisdom-aiagent-aiagentconfiguration-orchestrationaiagentconfiguration"></a>
The configuration for AI Agents of type `ORCHESTRATION`.
*Required*: No
*Type*: [OrchestrationAIAgentConfiguration](aws-properties-wisdom-aiagent-orchestrationaiagentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelfServiceAIAgentConfiguration`  <a name="cfn-wisdom-aiagent-aiagentconfiguration-selfserviceaiagentconfiguration"></a>
The self-service AI agent configuration.
*Required*: No
*Type*: [SelfServiceAIAgentConfiguration](aws-properties-wisdom-aiagent-selfserviceaiagentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
