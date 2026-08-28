---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-subslottypecomposition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SubSlotTypeComposition
<a name="aws-properties-lex-bot-subslottypecomposition"></a>

Subslot type composition.

## Syntax
<a name="aws-properties-lex-bot-subslottypecomposition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-subslottypecomposition-syntax.json"></a>

```
{
  "[Name](#cfn-lex-bot-subslottypecomposition-name)" : {{String}},
  "[SlotTypeId](#cfn-lex-bot-subslottypecomposition-slottypeid)" : {{String}},
  "[SlotTypeName](#cfn-lex-bot-subslottypecomposition-slottypename)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-subslottypecomposition-syntax.yaml"></a>

```
  [Name](#cfn-lex-bot-subslottypecomposition-name): {{String}}
  [SlotTypeId](#cfn-lex-bot-subslottypecomposition-slottypeid): {{String}}
  [SlotTypeName](#cfn-lex-bot-subslottypecomposition-slottypename): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-subslottypecomposition-properties"></a>

`Name`  <a name="cfn-lex-bot-subslottypecomposition-name"></a>
Name of a constituent sub slot inside a composite slot.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlotTypeId`  <a name="cfn-lex-bot-subslottypecomposition-slottypeid"></a>
The unique identifier assigned to a slot type. This refers to either a built-in slot type or the unique slotTypeId of a custom slot type.
*Required*: No
*Type*: String
*Pattern*: `^((AMAZON\.)[a-zA-Z_]+?|[0-9a-zA-Z]+)$`
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlotTypeName`  <a name="cfn-lex-bot-subslottypecomposition-slottypename"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
