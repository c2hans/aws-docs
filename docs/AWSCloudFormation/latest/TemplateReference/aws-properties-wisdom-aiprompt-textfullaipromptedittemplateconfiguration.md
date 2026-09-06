---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiprompt-textfullaipromptedittemplateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIPrompt TextFullAIPromptEditTemplateConfiguration
<a name="aws-properties-wisdom-aiprompt-textfullaipromptedittemplateconfiguration"></a>

The configuration for a prompt template that supports full textual prompt configuration using a YAML prompt.

## Syntax
<a name="aws-properties-wisdom-aiprompt-textfullaipromptedittemplateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiprompt-textfullaipromptedittemplateconfiguration-syntax.json"></a>

```
{
  "[Text](#cfn-wisdom-aiprompt-textfullaipromptedittemplateconfiguration-text)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiprompt-textfullaipromptedittemplateconfiguration-syntax.yaml"></a>

```
  [Text](#cfn-wisdom-aiprompt-textfullaipromptedittemplateconfiguration-text): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiprompt-textfullaipromptedittemplateconfiguration-properties"></a>

`Text`  <a name="cfn-wisdom-aiprompt-textfullaipromptedittemplateconfiguration-text"></a>
The YAML text for the AI Prompt template.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `200000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
