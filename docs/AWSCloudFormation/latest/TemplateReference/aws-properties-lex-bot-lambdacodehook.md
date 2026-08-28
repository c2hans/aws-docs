---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-lambdacodehook.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot LambdaCodeHook
<a name="aws-properties-lex-bot-lambdacodehook"></a>

Specifies a Lambda function that verifies requests to a bot or fulfills the user's request to a bot.

## Syntax
<a name="aws-properties-lex-bot-lambdacodehook-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-lambdacodehook-syntax.json"></a>

```
{
  "[CodeHookInterfaceVersion](#cfn-lex-bot-lambdacodehook-codehookinterfaceversion)" : {{String}},
  "[LambdaArn](#cfn-lex-bot-lambdacodehook-lambdaarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-lambdacodehook-syntax.yaml"></a>

```
  [CodeHookInterfaceVersion](#cfn-lex-bot-lambdacodehook-codehookinterfaceversion): {{String}}
  [LambdaArn](#cfn-lex-bot-lambdacodehook-lambdaarn): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-lambdacodehook-properties"></a>

`CodeHookInterfaceVersion`  <a name="cfn-lex-bot-lambdacodehook-codehookinterfaceversion"></a>
The version of the request-response that you want Amazon Lex to use to invoke your Lambda function.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LambdaArn`  <a name="cfn-lex-bot-lambdacodehook-lambdaarn"></a>
The Amazon Resource Name (ARN) of the Lambda function.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
