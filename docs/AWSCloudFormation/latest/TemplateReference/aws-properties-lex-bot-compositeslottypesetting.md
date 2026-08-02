---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-compositeslottypesetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot CompositeSlotTypeSetting
<a name="aws-properties-lex-bot-compositeslottypesetting"></a>

A composite slot is a combination of two or more slots that capture multiple pieces of information in a single user input.

## Syntax
<a name="aws-properties-lex-bot-compositeslottypesetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-compositeslottypesetting-syntax.json"></a>

```
{
  "[SubSlots](#cfn-lex-bot-compositeslottypesetting-subslots)" : {{[ SubSlotTypeComposition, ... ]}}
}
```

### YAML
<a name="aws-properties-lex-bot-compositeslottypesetting-syntax.yaml"></a>

```
  [SubSlots](#cfn-lex-bot-compositeslottypesetting-subslots): {{
    - SubSlotTypeComposition}}
```

## Properties
<a name="aws-properties-lex-bot-compositeslottypesetting-properties"></a>

`SubSlots`  <a name="cfn-lex-bot-compositeslottypesetting-subslots"></a>
Subslots in the composite slot.
*Required*: No
*Type*: Array of [SubSlotTypeComposition](aws-properties-lex-bot-subslottypecomposition.md)
*Minimum*: `1`
*Maximum*: `6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
