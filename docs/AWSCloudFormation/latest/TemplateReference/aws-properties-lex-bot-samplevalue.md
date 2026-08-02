---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-samplevalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SampleValue
<a name="aws-properties-lex-bot-samplevalue"></a>

Defines one of the values for a slot type.

## Syntax
<a name="aws-properties-lex-bot-samplevalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-samplevalue-syntax.json"></a>

```
{
  "[Value](#cfn-lex-bot-samplevalue-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-samplevalue-syntax.yaml"></a>

```
  [Value](#cfn-lex-bot-samplevalue-value): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-samplevalue-properties"></a>

`Value`  <a name="cfn-lex-bot-samplevalue-value"></a>
The value that can be used for a slot type.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `140`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
