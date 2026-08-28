---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-grammarslottypesetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot GrammarSlotTypeSetting
<a name="aws-properties-lex-bot-grammarslottypesetting"></a>

Settings requried for a slot type based on a grammar that you provide.

## Syntax
<a name="aws-properties-lex-bot-grammarslottypesetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-grammarslottypesetting-syntax.json"></a>

```
{
  "[Source](#cfn-lex-bot-grammarslottypesetting-source)" : {{GrammarSlotTypeSource}}
}
```

### YAML
<a name="aws-properties-lex-bot-grammarslottypesetting-syntax.yaml"></a>

```
  [Source](#cfn-lex-bot-grammarslottypesetting-source): {{
    GrammarSlotTypeSource}}
```

## Properties
<a name="aws-properties-lex-bot-grammarslottypesetting-properties"></a>

`Source`  <a name="cfn-lex-bot-grammarslottypesetting-source"></a>
The source of the grammar used to create the slot type.
*Required*: No
*Type*: [GrammarSlotTypeSource](aws-properties-lex-bot-grammarslottypesource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
