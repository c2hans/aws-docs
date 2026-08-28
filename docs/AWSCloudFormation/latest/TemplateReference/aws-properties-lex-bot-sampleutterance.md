---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-sampleutterance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SampleUtterance
<a name="aws-properties-lex-bot-sampleutterance"></a>

A sample utterance that invokes an intent or respond to a slot elicitation prompt.

## Syntax
<a name="aws-properties-lex-bot-sampleutterance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-sampleutterance-syntax.json"></a>

```
{
  "[Utterance](#cfn-lex-bot-sampleutterance-utterance)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-sampleutterance-syntax.yaml"></a>

```
  [Utterance](#cfn-lex-bot-sampleutterance-utterance): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-sampleutterance-properties"></a>

`Utterance`  <a name="cfn-lex-bot-sampleutterance-utterance"></a>
A sample utterance that invokes an intent or respond to a slot elicitation prompt.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
