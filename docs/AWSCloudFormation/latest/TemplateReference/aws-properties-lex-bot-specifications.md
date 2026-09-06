---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-specifications.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot Specifications
<a name="aws-properties-lex-bot-specifications"></a>

Subslot specifications.

## Syntax
<a name="aws-properties-lex-bot-specifications-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-specifications-syntax.json"></a>

```
{
  "[SlotTypeId](#cfn-lex-bot-specifications-slottypeid)" : {{String}},
  "[SlotTypeName](#cfn-lex-bot-specifications-slottypename)" : {{String}},
  "[ValueElicitationSetting](#cfn-lex-bot-specifications-valueelicitationsetting)" : {{SubSlotValueElicitationSetting}}
}
```

### YAML
<a name="aws-properties-lex-bot-specifications-syntax.yaml"></a>

```
  [SlotTypeId](#cfn-lex-bot-specifications-slottypeid): {{String}}
  [SlotTypeName](#cfn-lex-bot-specifications-slottypename): {{String}}
  [ValueElicitationSetting](#cfn-lex-bot-specifications-valueelicitationsetting): {{
    SubSlotValueElicitationSetting}}
```

## Properties
<a name="aws-properties-lex-bot-specifications-properties"></a>

`SlotTypeId`  <a name="cfn-lex-bot-specifications-slottypeid"></a>
The unique identifier assigned to the slot type.
*Required*: No
*Type*: String
*Pattern*: `^((AMAZON\.)[a-zA-Z_]+?|[0-9a-zA-Z]+)$`
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlotTypeName`  <a name="cfn-lex-bot-specifications-slottypename"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueElicitationSetting`  <a name="cfn-lex-bot-specifications-valueelicitationsetting"></a>
Specifies the elicitation setting details for constituent sub slots of a composite slot.
*Required*: Yes
*Type*: [SubSlotValueElicitationSetting](aws-properties-lex-bot-subslotvalueelicitationsetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
