---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-selfserviceaiagentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent SelfServiceAIAgentConfiguration
<a name="aws-properties-wisdom-aiagent-selfserviceaiagentconfiguration"></a>

The configuration of the self-service AI agent.

## Syntax
<a name="aws-properties-wisdom-aiagent-selfserviceaiagentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-selfserviceaiagentconfiguration-syntax.json"></a>

```
{
  "[AssociationConfigurations](#cfn-wisdom-aiagent-selfserviceaiagentconfiguration-associationconfigurations)" : {{[ AssociationConfiguration, ... ]}},
  "[SelfServiceAIGuardrailId](#cfn-wisdom-aiagent-selfserviceaiagentconfiguration-selfserviceaiguardrailid)" : {{String}},
  "[SelfServiceAnswerGenerationAIPromptId](#cfn-wisdom-aiagent-selfserviceaiagentconfiguration-selfserviceanswergenerationaipromptid)" : {{String}},
  "[SelfServicePreProcessingAIPromptId](#cfn-wisdom-aiagent-selfserviceaiagentconfiguration-selfservicepreprocessingaipromptid)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-selfserviceaiagentconfiguration-syntax.yaml"></a>

```
  [AssociationConfigurations](#cfn-wisdom-aiagent-selfserviceaiagentconfiguration-associationconfigurations): {{
    - AssociationConfiguration}}
  [SelfServiceAIGuardrailId](#cfn-wisdom-aiagent-selfserviceaiagentconfiguration-selfserviceaiguardrailid): {{String}}
  [SelfServiceAnswerGenerationAIPromptId](#cfn-wisdom-aiagent-selfserviceaiagentconfiguration-selfserviceanswergenerationaipromptid): {{String}}
  [SelfServicePreProcessingAIPromptId](#cfn-wisdom-aiagent-selfserviceaiagentconfiguration-selfservicepreprocessingaipromptid): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-selfserviceaiagentconfiguration-properties"></a>

`AssociationConfigurations`  <a name="cfn-wisdom-aiagent-selfserviceaiagentconfiguration-associationconfigurations"></a>
The association configuration of the self-service AI agent.
*Required*: No
*Type*: Array of [AssociationConfiguration](aws-properties-wisdom-aiagent-associationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelfServiceAIGuardrailId`  <a name="cfn-wisdom-aiagent-selfserviceaiagentconfiguration-selfserviceaiguardrailid"></a>
The ID of the self-service AI guardrail.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelfServiceAnswerGenerationAIPromptId`  <a name="cfn-wisdom-aiagent-selfserviceaiagentconfiguration-selfserviceanswergenerationaipromptid"></a>
The ID of the self-service answer generation AI prompt.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelfServicePreProcessingAIPromptId`  <a name="cfn-wisdom-aiagent-selfserviceaiagentconfiguration-selfservicepreprocessingaipromptid"></a>
The ID of the self-service preprocessing AI prompt.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
