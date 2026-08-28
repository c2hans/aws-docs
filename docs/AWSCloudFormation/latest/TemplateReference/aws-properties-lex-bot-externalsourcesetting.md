---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-externalsourcesetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot ExternalSourceSetting
<a name="aws-properties-lex-bot-externalsourcesetting"></a>

Provides information about the external source of the slot type's definition.

## Syntax
<a name="aws-properties-lex-bot-externalsourcesetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-externalsourcesetting-syntax.json"></a>

```
{
  "[GrammarSlotTypeSetting](#cfn-lex-bot-externalsourcesetting-grammarslottypesetting)" : {{GrammarSlotTypeSetting}}
}
```

### YAML
<a name="aws-properties-lex-bot-externalsourcesetting-syntax.yaml"></a>

```
  [GrammarSlotTypeSetting](#cfn-lex-bot-externalsourcesetting-grammarslottypesetting): {{
    GrammarSlotTypeSetting}}
```

## Properties
<a name="aws-properties-lex-bot-externalsourcesetting-properties"></a>

`GrammarSlotTypeSetting`  <a name="cfn-lex-bot-externalsourcesetting-grammarslottypesetting"></a>
Settings required for a slot type based on a grammar that you provide.
*Required*: No
*Type*: [GrammarSlotTypeSetting](aws-properties-lex-bot-grammarslottypesetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
