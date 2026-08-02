---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-sessionattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SessionAttribute
<a name="aws-properties-lex-bot-sessionattribute"></a>

A key/value pair representing session-specific context information. It contains application information passed between Amazon Lex V2 and a client application.

## Syntax
<a name="aws-properties-lex-bot-sessionattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-sessionattribute-syntax.json"></a>

```
{
  "[Key](#cfn-lex-bot-sessionattribute-key)" : {{String}},
  "[Value](#cfn-lex-bot-sessionattribute-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-sessionattribute-syntax.yaml"></a>

```
  [Key](#cfn-lex-bot-sessionattribute-key): {{String}}
  [Value](#cfn-lex-bot-sessionattribute-value): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-sessionattribute-properties"></a>

`Key`  <a name="cfn-lex-bot-sessionattribute-key"></a>
The name of the session attribute.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-lex-bot-sessionattribute-value"></a>
The session-specific context information for the session attribute.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
