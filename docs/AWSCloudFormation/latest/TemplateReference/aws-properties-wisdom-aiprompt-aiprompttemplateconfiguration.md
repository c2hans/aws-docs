---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiprompt-aiprompttemplateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIPrompt AIPromptTemplateConfiguration
<a name="aws-properties-wisdom-aiprompt-aiprompttemplateconfiguration"></a>

A typed union that specifies the configuration for a prompt template based on its type.

## Syntax
<a name="aws-properties-wisdom-aiprompt-aiprompttemplateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiprompt-aiprompttemplateconfiguration-syntax.json"></a>

```
{
  "[TextFullAIPromptEditTemplateConfiguration](#cfn-wisdom-aiprompt-aiprompttemplateconfiguration-textfullaipromptedittemplateconfiguration)" : {{TextFullAIPromptEditTemplateConfiguration}}
}
```

### YAML
<a name="aws-properties-wisdom-aiprompt-aiprompttemplateconfiguration-syntax.yaml"></a>

```
  [TextFullAIPromptEditTemplateConfiguration](#cfn-wisdom-aiprompt-aiprompttemplateconfiguration-textfullaipromptedittemplateconfiguration): {{
    TextFullAIPromptEditTemplateConfiguration}}
```

## Properties
<a name="aws-properties-wisdom-aiprompt-aiprompttemplateconfiguration-properties"></a>

`TextFullAIPromptEditTemplateConfiguration`  <a name="cfn-wisdom-aiprompt-aiprompttemplateconfiguration-textfullaipromptedittemplateconfiguration"></a>
The configuration for a prompt template that supports full textual prompt configuration using a YAML prompt.
*Required*: Yes
*Type*: [TextFullAIPromptEditTemplateConfiguration](aws-properties-wisdom-aiprompt-textfullaipromptedittemplateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
