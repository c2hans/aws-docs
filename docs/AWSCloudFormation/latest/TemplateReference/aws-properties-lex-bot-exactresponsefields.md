---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-exactresponsefields.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot ExactResponseFields
<a name="aws-properties-lex-bot-exactresponsefields"></a>

Contains the names of the fields used for an exact response to the user.

## Syntax
<a name="aws-properties-lex-bot-exactresponsefields-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-exactresponsefields-syntax.json"></a>

```
{
  "[AnswerField](#cfn-lex-bot-exactresponsefields-answerfield)" : {{String}},
  "[QuestionField](#cfn-lex-bot-exactresponsefields-questionfield)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-exactresponsefields-syntax.yaml"></a>

```
  [AnswerField](#cfn-lex-bot-exactresponsefields-answerfield): {{String}}
  [QuestionField](#cfn-lex-bot-exactresponsefields-questionfield): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-exactresponsefields-properties"></a>

`AnswerField`  <a name="cfn-lex-bot-exactresponsefields-answerfield"></a>
The name of the field that contains the answer to the query made to the OpenSearch Service database.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QuestionField`  <a name="cfn-lex-bot-exactresponsefields-questionfield"></a>
The name of the field that contains the query made to the OpenSearch Service database.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
