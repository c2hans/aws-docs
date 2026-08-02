---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-runtimesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot RuntimeSettings
<a name="aws-properties-lex-bot-runtimesettings"></a>

Contains specifications about the Amazon Lex runtime generative AI capabilities from Amazon Bedrock that you can turn on for your bot.

## Syntax
<a name="aws-properties-lex-bot-runtimesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-runtimesettings-syntax.json"></a>

```
{
  "[NluImprovementSpecification](#cfn-lex-bot-runtimesettings-nluimprovementspecification)" : {{NluImprovementSpecification}},
  "[SlotResolutionImprovementSpecification](#cfn-lex-bot-runtimesettings-slotresolutionimprovementspecification)" : {{SlotResolutionImprovementSpecification}}
}
```

### YAML
<a name="aws-properties-lex-bot-runtimesettings-syntax.yaml"></a>

```
  [NluImprovementSpecification](#cfn-lex-bot-runtimesettings-nluimprovementspecification): {{
    NluImprovementSpecification}}
  [SlotResolutionImprovementSpecification](#cfn-lex-bot-runtimesettings-slotresolutionimprovementspecification): {{
    SlotResolutionImprovementSpecification}}
```

## Properties
<a name="aws-properties-lex-bot-runtimesettings-properties"></a>

`NluImprovementSpecification`  <a name="cfn-lex-bot-runtimesettings-nluimprovementspecification"></a>
Property description not available.
*Required*: No
*Type*: [NluImprovementSpecification](aws-properties-lex-bot-nluimprovementspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlotResolutionImprovementSpecification`  <a name="cfn-lex-bot-runtimesettings-slotresolutionimprovementspecification"></a>
Property description not available.
*Required*: No
*Type*: [SlotResolutionImprovementSpecification](aws-properties-lex-bot-slotresolutionimprovementspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
