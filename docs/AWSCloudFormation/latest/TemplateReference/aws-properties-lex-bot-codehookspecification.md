---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-codehookspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot CodeHookSpecification
<a name="aws-properties-lex-bot-codehookspecification"></a>

Contains information about code hooks that Amazon Lex calls during a conversation.

## Syntax
<a name="aws-properties-lex-bot-codehookspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-codehookspecification-syntax.json"></a>

```
{
  "[LambdaCodeHook](#cfn-lex-bot-codehookspecification-lambdacodehook)" : {{LambdaCodeHook}}
}
```

### YAML
<a name="aws-properties-lex-bot-codehookspecification-syntax.yaml"></a>

```
  [LambdaCodeHook](#cfn-lex-bot-codehookspecification-lambdacodehook): {{
    LambdaCodeHook}}
```

## Properties
<a name="aws-properties-lex-bot-codehookspecification-properties"></a>

`LambdaCodeHook`  <a name="cfn-lex-bot-codehookspecification-lambdacodehook"></a>
Specifies a Lambda function that verifies requests to a bot or fulfills the user's request to a bot.
*Required*: Yes
*Type*: [LambdaCodeHook](aws-properties-lex-bot-lambdacodehook.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
