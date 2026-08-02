---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-emailoverviewaiagentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent EmailOverviewAIAgentConfiguration
<a name="aws-properties-wisdom-aiagent-emailoverviewaiagentconfiguration"></a>

The configuration for AI Agents of type `EMAIL_OVERVIEW`.

## Syntax
<a name="aws-properties-wisdom-aiagent-emailoverviewaiagentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-emailoverviewaiagentconfiguration-syntax.json"></a>

```
{
  "[EmailOverviewAIPromptId](#cfn-wisdom-aiagent-emailoverviewaiagentconfiguration-emailoverviewaipromptid)" : {{String}},
  "[Locale](#cfn-wisdom-aiagent-emailoverviewaiagentconfiguration-locale)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-emailoverviewaiagentconfiguration-syntax.yaml"></a>

```
  [EmailOverviewAIPromptId](#cfn-wisdom-aiagent-emailoverviewaiagentconfiguration-emailoverviewaipromptid): {{String}}
  [Locale](#cfn-wisdom-aiagent-emailoverviewaiagentconfiguration-locale): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-emailoverviewaiagentconfiguration-properties"></a>

`EmailOverviewAIPromptId`  <a name="cfn-wisdom-aiagent-emailoverviewaiagentconfiguration-emailoverviewaipromptid"></a>
The AI Prompt identifier for the Email Overview prompt used by the `EMAIL_OVERVIEW` AI Agent.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Locale`  <a name="cfn-wisdom-aiagent-emailoverviewaiagentconfiguration-locale"></a>
The locale to which specifies the language and region settings that determine the response language for [QueryAssistant](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html).
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
