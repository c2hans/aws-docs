---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-slotvalueregexfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SlotValueRegexFilter
<a name="aws-properties-lex-bot-slotvalueregexfilter"></a>

Provides a regular expression used to validate the value of a slot.

## Syntax
<a name="aws-properties-lex-bot-slotvalueregexfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-slotvalueregexfilter-syntax.json"></a>

```
{
  "[Pattern](#cfn-lex-bot-slotvalueregexfilter-pattern)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-slotvalueregexfilter-syntax.yaml"></a>

```
  [Pattern](#cfn-lex-bot-slotvalueregexfilter-pattern): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-slotvalueregexfilter-properties"></a>

`Pattern`  <a name="cfn-lex-bot-slotvalueregexfilter-pattern"></a>
A regular expression used to validate the value of a slot.
 Use a standard regular expression. Amazon Lex supports the following characters in the regular expression:
+ A-Z, a-z
+ 0-9
+ Unicode characters ("\\⁠u<Unicode>")
 Represent Unicode characters with four digits, for example "\\⁠u0041" or "\\⁠u005A".
 The following regular expression operators are not supported:
+ Infinite repeaters: \*, \+, or {x,} with no upper bound.
+ Wild card (.)
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
