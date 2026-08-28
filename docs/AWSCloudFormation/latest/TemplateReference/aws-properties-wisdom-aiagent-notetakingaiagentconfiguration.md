---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-notetakingaiagentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent NoteTakingAIAgentConfiguration
<a name="aws-properties-wisdom-aiagent-notetakingaiagentconfiguration"></a>

The configuration for AI Agents of type `NOTE_TAKING`.

## Syntax
<a name="aws-properties-wisdom-aiagent-notetakingaiagentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-notetakingaiagentconfiguration-syntax.json"></a>

```
{
  "[Locale](#cfn-wisdom-aiagent-notetakingaiagentconfiguration-locale)" : {{String}},
  "[NoteTakingAIGuardrailId](#cfn-wisdom-aiagent-notetakingaiagentconfiguration-notetakingaiguardrailid)" : {{String}},
  "[NoteTakingAIPromptId](#cfn-wisdom-aiagent-notetakingaiagentconfiguration-notetakingaipromptid)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-notetakingaiagentconfiguration-syntax.yaml"></a>

```
  [Locale](#cfn-wisdom-aiagent-notetakingaiagentconfiguration-locale): {{String}}
  [NoteTakingAIGuardrailId](#cfn-wisdom-aiagent-notetakingaiagentconfiguration-notetakingaiguardrailid): {{String}}
  [NoteTakingAIPromptId](#cfn-wisdom-aiagent-notetakingaiagentconfiguration-notetakingaipromptid): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-notetakingaiagentconfiguration-properties"></a>

`Locale`  <a name="cfn-wisdom-aiagent-notetakingaiagentconfiguration-locale"></a>
The locale setting for language-specific case summarization generation (for example, en\_US, es\_ES).
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NoteTakingAIGuardrailId`  <a name="cfn-wisdom-aiagent-notetakingaiagentconfiguration-notetakingaiguardrailid"></a>
The AI Guardrail identifier used by the Note Taking AI Agent.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NoteTakingAIPromptId`  <a name="cfn-wisdom-aiagent-notetakingaiagentconfiguration-notetakingaipromptid"></a>
The AI Prompt identifier used by the Note Taking AI Agent.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
