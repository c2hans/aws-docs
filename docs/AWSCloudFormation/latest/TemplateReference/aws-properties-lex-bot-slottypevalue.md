---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-slottypevalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SlotTypeValue
<a name="aws-properties-lex-bot-slottypevalue"></a>

Each slot type can have a set of values. Each `SlotTypeValue` represents a value that the slot type can take.

## Syntax
<a name="aws-properties-lex-bot-slottypevalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-slottypevalue-syntax.json"></a>

```
{
  "[SampleValue](#cfn-lex-bot-slottypevalue-samplevalue)" : {{SampleValue}},
  "[Synonyms](#cfn-lex-bot-slottypevalue-synonyms)" : {{[ SampleValue, ... ]}}
}
```

### YAML
<a name="aws-properties-lex-bot-slottypevalue-syntax.yaml"></a>

```
  [SampleValue](#cfn-lex-bot-slottypevalue-samplevalue): {{
    SampleValue}}
  [Synonyms](#cfn-lex-bot-slottypevalue-synonyms): {{
    - SampleValue}}
```

## Properties
<a name="aws-properties-lex-bot-slottypevalue-properties"></a>

`SampleValue`  <a name="cfn-lex-bot-slottypevalue-samplevalue"></a>
The value of the slot type entry.
*Required*: Yes
*Type*: [SampleValue](aws-properties-lex-bot-samplevalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Synonyms`  <a name="cfn-lex-bot-slottypevalue-synonyms"></a>
Additional values related to the slot type entry.
*Required*: No
*Type*: Array of [SampleValue](aws-properties-lex-bot-samplevalue.md)
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
