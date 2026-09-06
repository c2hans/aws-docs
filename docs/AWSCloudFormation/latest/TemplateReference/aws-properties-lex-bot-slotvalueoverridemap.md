---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-slotvalueoverridemap.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SlotValueOverrideMap
<a name="aws-properties-lex-bot-slotvalueoverridemap"></a>

Maps a slot name to the [SlotValueOverride](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SlotValueOverride.html) object.

## Syntax
<a name="aws-properties-lex-bot-slotvalueoverridemap-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-slotvalueoverridemap-syntax.json"></a>

```
{
  "[SlotName](#cfn-lex-bot-slotvalueoverridemap-slotname)" : {{String}},
  "[SlotValueOverride](#cfn-lex-bot-slotvalueoverridemap-slotvalueoverride)" : {{SlotValueOverride}}
}
```

### YAML
<a name="aws-properties-lex-bot-slotvalueoverridemap-syntax.yaml"></a>

```
  [SlotName](#cfn-lex-bot-slotvalueoverridemap-slotname): {{String}}
  [SlotValueOverride](#cfn-lex-bot-slotvalueoverridemap-slotvalueoverride): {{
    SlotValueOverride}}
```

## Properties
<a name="aws-properties-lex-bot-slotvalueoverridemap-properties"></a>

`SlotName`  <a name="cfn-lex-bot-slotvalueoverridemap-slotname"></a>
The name of the slot.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?)+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlotValueOverride`  <a name="cfn-lex-bot-slotvalueoverridemap-slotvalueoverride"></a>
The SlotValueOverride object to which the slot name will be mapped.
*Required*: No
*Type*: [SlotValueOverride](aws-properties-lex-bot-slotvalueoverride.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
