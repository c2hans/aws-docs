---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-emailresponseaiagentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent EmailResponseAIAgentConfiguration
<a name="aws-properties-wisdom-aiagent-emailresponseaiagentconfiguration"></a>

The configuration for AI Agents of type `EMAIL_RESPONSE`.

## Syntax
<a name="aws-properties-wisdom-aiagent-emailresponseaiagentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-emailresponseaiagentconfiguration-syntax.json"></a>

```
{
  "[AssociationConfigurations](#cfn-wisdom-aiagent-emailresponseaiagentconfiguration-associationconfigurations)" : {{[ AssociationConfiguration, ... ]}},
  "[EmailQueryReformulationAIPromptId](#cfn-wisdom-aiagent-emailresponseaiagentconfiguration-emailqueryreformulationaipromptid)" : {{String}},
  "[EmailResponseAIPromptId](#cfn-wisdom-aiagent-emailresponseaiagentconfiguration-emailresponseaipromptid)" : {{String}},
  "[Locale](#cfn-wisdom-aiagent-emailresponseaiagentconfiguration-locale)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-emailresponseaiagentconfiguration-syntax.yaml"></a>

```
  [AssociationConfigurations](#cfn-wisdom-aiagent-emailresponseaiagentconfiguration-associationconfigurations): {{
    - AssociationConfiguration}}
  [EmailQueryReformulationAIPromptId](#cfn-wisdom-aiagent-emailresponseaiagentconfiguration-emailqueryreformulationaipromptid): {{String}}
  [EmailResponseAIPromptId](#cfn-wisdom-aiagent-emailresponseaiagentconfiguration-emailresponseaipromptid): {{String}}
  [Locale](#cfn-wisdom-aiagent-emailresponseaiagentconfiguration-locale): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-emailresponseaiagentconfiguration-properties"></a>

`AssociationConfigurations`  <a name="cfn-wisdom-aiagent-emailresponseaiagentconfiguration-associationconfigurations"></a>
The association configurations for overriding behavior on this AI Agent.
*Required*: No
*Type*: Array of [AssociationConfiguration](aws-properties-wisdom-aiagent-associationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailQueryReformulationAIPromptId`  <a name="cfn-wisdom-aiagent-emailresponseaiagentconfiguration-emailqueryreformulationaipromptid"></a>
The AI Prompt identifier for the Email Query Reformulation prompt used by the `EMAIL_RESPONSE` AI Agent.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailResponseAIPromptId`  <a name="cfn-wisdom-aiagent-emailresponseaiagentconfiguration-emailresponseaipromptid"></a>
The AI Prompt identifier for the Email Response prompt used by the `EMAIL_RESPONSE` AI Agent.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Locale`  <a name="cfn-wisdom-aiagent-emailresponseaiagentconfiguration-locale"></a>
The locale to which specifies the language and region settings that determine the response language for [QueryAssistant](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html).
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
