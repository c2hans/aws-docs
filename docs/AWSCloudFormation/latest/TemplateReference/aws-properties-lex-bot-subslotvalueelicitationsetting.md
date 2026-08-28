---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-subslotvalueelicitationsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SubSlotValueElicitationSetting
<a name="aws-properties-lex-bot-subslotvalueelicitationsetting"></a>

Subslot elicitation settings.

`DefaultValueSpecification` is a list of default values for a constituent sub slot in a composite slot. Default values are used when Amazon Lex hasn't determined a value for a slot. You can specify default values from context variables, session attributes, and defined values. This is similar to `DefaultValueSpecification` for slots.

`PromptSpecification` is the prompt that Amazon Lex uses to elicit the sub slot value from the user. This is similar to `PromptSpecification` for slots.

## Syntax
<a name="aws-properties-lex-bot-subslotvalueelicitationsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-subslotvalueelicitationsetting-syntax.json"></a>

```
{
  "[DefaultValueSpecification](#cfn-lex-bot-subslotvalueelicitationsetting-defaultvaluespecification)" : {{SlotDefaultValueSpecification}},
  "[PromptSpecification](#cfn-lex-bot-subslotvalueelicitationsetting-promptspecification)" : {{PromptSpecification}},
  "[SampleUtterances](#cfn-lex-bot-subslotvalueelicitationsetting-sampleutterances)" : {{[ SampleUtterance, ... ]}},
  "[WaitAndContinueSpecification](#cfn-lex-bot-subslotvalueelicitationsetting-waitandcontinuespecification)" : {{WaitAndContinueSpecification}}
}
```

### YAML
<a name="aws-properties-lex-bot-subslotvalueelicitationsetting-syntax.yaml"></a>

```
  [DefaultValueSpecification](#cfn-lex-bot-subslotvalueelicitationsetting-defaultvaluespecification): {{
    SlotDefaultValueSpecification}}
  [PromptSpecification](#cfn-lex-bot-subslotvalueelicitationsetting-promptspecification): {{
    PromptSpecification}}
  [SampleUtterances](#cfn-lex-bot-subslotvalueelicitationsetting-sampleutterances): {{
    - SampleUtterance}}
  [WaitAndContinueSpecification](#cfn-lex-bot-subslotvalueelicitationsetting-waitandcontinuespecification): {{
    WaitAndContinueSpecification}}
```

## Properties
<a name="aws-properties-lex-bot-subslotvalueelicitationsetting-properties"></a>

`DefaultValueSpecification`  <a name="cfn-lex-bot-subslotvalueelicitationsetting-defaultvaluespecification"></a>
Property description not available.
*Required*: No
*Type*: [SlotDefaultValueSpecification](aws-properties-lex-bot-slotdefaultvaluespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PromptSpecification`  <a name="cfn-lex-bot-subslotvalueelicitationsetting-promptspecification"></a>
Property description not available.
*Required*: No
*Type*: [PromptSpecification](aws-properties-lex-bot-promptspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SampleUtterances`  <a name="cfn-lex-bot-subslotvalueelicitationsetting-sampleutterances"></a>
If you know a specific pattern that users might respond to an Amazon Lex request for a sub slot value, you can provide those utterances to improve accuracy. This is optional. In most cases Amazon Lex is capable of understanding user utterances. This is similar to `SampleUtterances` for slots.
*Required*: No
*Type*: Array of [SampleUtterance](aws-properties-lex-bot-sampleutterance.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WaitAndContinueSpecification`  <a name="cfn-lex-bot-subslotvalueelicitationsetting-waitandcontinuespecification"></a>
Property description not available.
*Required*: No
*Type*: [WaitAndContinueSpecification](aws-properties-lex-bot-waitandcontinuespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
