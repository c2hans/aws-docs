---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-guardrail-wordpolicyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Guardrail WordPolicyConfig
<a name="aws-properties-bedrock-guardrail-wordpolicyconfig"></a>

Contains details about the word policy to configured for the guardrail.

## Syntax
<a name="aws-properties-bedrock-guardrail-wordpolicyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-guardrail-wordpolicyconfig-syntax.json"></a>

```
{
  "[ManagedWordListsConfig](#cfn-bedrock-guardrail-wordpolicyconfig-managedwordlistsconfig)" : {{[ ManagedWordsConfig, ... ]}},
  "[WordsConfig](#cfn-bedrock-guardrail-wordpolicyconfig-wordsconfig)" : {{[ WordConfig, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-guardrail-wordpolicyconfig-syntax.yaml"></a>

```
  [ManagedWordListsConfig](#cfn-bedrock-guardrail-wordpolicyconfig-managedwordlistsconfig): {{
    - ManagedWordsConfig}}
  [WordsConfig](#cfn-bedrock-guardrail-wordpolicyconfig-wordsconfig): {{
    - WordConfig}}
```

## Properties
<a name="aws-properties-bedrock-guardrail-wordpolicyconfig-properties"></a>

`ManagedWordListsConfig`  <a name="cfn-bedrock-guardrail-wordpolicyconfig-managedwordlistsconfig"></a>
A list of managed words to configure for the guardrail.
*Required*: No
*Type*: Array of [ManagedWordsConfig](aws-properties-bedrock-guardrail-managedwordsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WordsConfig`  <a name="cfn-bedrock-guardrail-wordpolicyconfig-wordsconfig"></a>
A list of words to configure for the guardrail.
*Required*: No
*Type*: Array of [WordConfig](aws-properties-bedrock-guardrail-wordconfig.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
