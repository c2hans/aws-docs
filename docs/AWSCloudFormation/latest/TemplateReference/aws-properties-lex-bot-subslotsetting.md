---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-subslotsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SubSlotSetting
<a name="aws-properties-lex-bot-subslotsetting"></a>

Specifications for the constituent sub slots and the expression for the composite slot.

## Syntax
<a name="aws-properties-lex-bot-subslotsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-subslotsetting-syntax.json"></a>

```
{
  "[Expression](#cfn-lex-bot-subslotsetting-expression)" : {{String}},
  "[SlotSpecifications](#cfn-lex-bot-subslotsetting-slotspecifications)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-lex-bot-subslotsetting-syntax.yaml"></a>

```
  [Expression](#cfn-lex-bot-subslotsetting-expression): {{String}}
  [SlotSpecifications](#cfn-lex-bot-subslotsetting-slotspecifications): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-lex-bot-subslotsetting-properties"></a>

`Expression`  <a name="cfn-lex-bot-subslotsetting-expression"></a>
The expression text for defining the constituent sub slots in the composite slot using logical AND and OR operators.
*Required*: No
*Type*: String
*Pattern*: `[0-9A-Za-z_\-\s\(\)]+`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlotSpecifications`  <a name="cfn-lex-bot-subslotsetting-slotspecifications"></a>
Specifications for the constituent sub slots of a composite slot.
*Required*: No
*Type*: Object of [Specifications](aws-properties-lex-bot-specifications.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
