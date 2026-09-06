---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-inputcontext.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot InputContext
<a name="aws-properties-lex-bot-inputcontext"></a>

A context that must be active for an intent to be selected by Amazon Lex.

## Syntax
<a name="aws-properties-lex-bot-inputcontext-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-inputcontext-syntax.json"></a>

```
{
  "[Name](#cfn-lex-bot-inputcontext-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-inputcontext-syntax.yaml"></a>

```
  [Name](#cfn-lex-bot-inputcontext-name): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-inputcontext-properties"></a>

`Name`  <a name="cfn-lex-bot-inputcontext-name"></a>
The name of the context.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?)+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
