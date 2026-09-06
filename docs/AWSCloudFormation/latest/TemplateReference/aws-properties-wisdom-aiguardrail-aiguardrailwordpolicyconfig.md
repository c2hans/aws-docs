---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiguardrail-aiguardrailwordpolicyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIGuardrail AIGuardrailWordPolicyConfig
<a name="aws-properties-wisdom-aiguardrail-aiguardrailwordpolicyconfig"></a>

Word policy config for a guardrail.

## Syntax
<a name="aws-properties-wisdom-aiguardrail-aiguardrailwordpolicyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiguardrail-aiguardrailwordpolicyconfig-syntax.json"></a>

```
{
  "[ManagedWordListsConfig](#cfn-wisdom-aiguardrail-aiguardrailwordpolicyconfig-managedwordlistsconfig)" : {{[ GuardrailManagedWordsConfig, ... ]}},
  "[WordsConfig](#cfn-wisdom-aiguardrail-aiguardrailwordpolicyconfig-wordsconfig)" : {{[ GuardrailWordConfig, ... ]}}
}
```

### YAML
<a name="aws-properties-wisdom-aiguardrail-aiguardrailwordpolicyconfig-syntax.yaml"></a>

```
  [ManagedWordListsConfig](#cfn-wisdom-aiguardrail-aiguardrailwordpolicyconfig-managedwordlistsconfig): {{
    - GuardrailManagedWordsConfig}}
  [WordsConfig](#cfn-wisdom-aiguardrail-aiguardrailwordpolicyconfig-wordsconfig): {{
    - GuardrailWordConfig}}
```

## Properties
<a name="aws-properties-wisdom-aiguardrail-aiguardrailwordpolicyconfig-properties"></a>

`ManagedWordListsConfig`  <a name="cfn-wisdom-aiguardrail-aiguardrailwordpolicyconfig-managedwordlistsconfig"></a>
A config for the list of managed words.
*Required*: No
*Type*: Array of [GuardrailManagedWordsConfig](aws-properties-wisdom-aiguardrail-guardrailmanagedwordsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WordsConfig`  <a name="cfn-wisdom-aiguardrail-aiguardrailwordpolicyconfig-wordsconfig"></a>
List of custom word configurations.
*Required*: No
*Type*: Array of [GuardrailWordConfig](aws-properties-wisdom-aiguardrail-guardrailwordconfig.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
