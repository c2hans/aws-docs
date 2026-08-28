---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-advancedrecognitionsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot AdvancedRecognitionSetting
<a name="aws-properties-lex-bot-advancedrecognitionsetting"></a>

Provides settings that enable advanced recognition settings for slot values.

## Syntax
<a name="aws-properties-lex-bot-advancedrecognitionsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-advancedrecognitionsetting-syntax.json"></a>

```
{
  "[AudioRecognitionStrategy](#cfn-lex-bot-advancedrecognitionsetting-audiorecognitionstrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-advancedrecognitionsetting-syntax.yaml"></a>

```
  [AudioRecognitionStrategy](#cfn-lex-bot-advancedrecognitionsetting-audiorecognitionstrategy): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-advancedrecognitionsetting-properties"></a>

`AudioRecognitionStrategy`  <a name="cfn-lex-bot-advancedrecognitionsetting-audiorecognitionstrategy"></a>
Enables using the slot values as a custom vocabulary for recognizing user utterances.
*Required*: No
*Type*: String
*Allowed values*: `UseSlotValuesAsCustomVocabulary`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
