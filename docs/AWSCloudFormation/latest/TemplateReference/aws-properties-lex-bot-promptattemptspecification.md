---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-promptattemptspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot PromptAttemptSpecification
<a name="aws-properties-lex-bot-promptattemptspecification"></a>

Specifies the settings on a prompt attempt.

## Syntax
<a name="aws-properties-lex-bot-promptattemptspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-promptattemptspecification-syntax.json"></a>

```
{
  "[AllowedInputTypes](#cfn-lex-bot-promptattemptspecification-allowedinputtypes)" : {{AllowedInputTypes}},
  "[AllowInterrupt](#cfn-lex-bot-promptattemptspecification-allowinterrupt)" : {{Boolean}},
  "[AudioAndDTMFInputSpecification](#cfn-lex-bot-promptattemptspecification-audioanddtmfinputspecification)" : {{AudioAndDTMFInputSpecification}},
  "[TextInputSpecification](#cfn-lex-bot-promptattemptspecification-textinputspecification)" : {{TextInputSpecification}}
}
```

### YAML
<a name="aws-properties-lex-bot-promptattemptspecification-syntax.yaml"></a>

```
  [AllowedInputTypes](#cfn-lex-bot-promptattemptspecification-allowedinputtypes): {{
    AllowedInputTypes}}
  [AllowInterrupt](#cfn-lex-bot-promptattemptspecification-allowinterrupt): {{Boolean}}
  [AudioAndDTMFInputSpecification](#cfn-lex-bot-promptattemptspecification-audioanddtmfinputspecification): {{
    AudioAndDTMFInputSpecification}}
  [TextInputSpecification](#cfn-lex-bot-promptattemptspecification-textinputspecification): {{
    TextInputSpecification}}
```

## Properties
<a name="aws-properties-lex-bot-promptattemptspecification-properties"></a>

`AllowedInputTypes`  <a name="cfn-lex-bot-promptattemptspecification-allowedinputtypes"></a>
Indicates the allowed input types of the prompt attempt.
*Required*: Yes
*Type*: [AllowedInputTypes](aws-properties-lex-bot-allowedinputtypes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowInterrupt`  <a name="cfn-lex-bot-promptattemptspecification-allowinterrupt"></a>
Indicates whether the user can interrupt a speech prompt attempt from the bot.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AudioAndDTMFInputSpecification`  <a name="cfn-lex-bot-promptattemptspecification-audioanddtmfinputspecification"></a>
Specifies the settings on audio and DTMF input.
*Required*: No
*Type*: [AudioAndDTMFInputSpecification](aws-properties-lex-bot-audioanddtmfinputspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextInputSpecification`  <a name="cfn-lex-bot-promptattemptspecification-textinputspecification"></a>
Specifies the settings on text input.
*Required*: No
*Type*: [TextInputSpecification](aws-properties-lex-bot-textinputspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
