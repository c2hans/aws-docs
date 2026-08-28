---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-customsmssender.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool CustomSMSSender
<a name="aws-properties-cognito-userpool-customsmssender"></a>

The configuration of a custom SMS sender Lambda trigger. This trigger routes all SMS notifications from a user pool to a Lambda function that delivers the message using custom logic.

## Syntax
<a name="aws-properties-cognito-userpool-customsmssender-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-customsmssender-syntax.json"></a>

```
{
  "[LambdaArn](#cfn-cognito-userpool-customsmssender-lambdaarn)" : {{String}},
  "[LambdaVersion](#cfn-cognito-userpool-customsmssender-lambdaversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-customsmssender-syntax.yaml"></a>

```
  [LambdaArn](#cfn-cognito-userpool-customsmssender-lambdaarn): {{String}}
  [LambdaVersion](#cfn-cognito-userpool-customsmssender-lambdaversion): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpool-customsmssender-properties"></a>

`LambdaArn`  <a name="cfn-cognito-userpool-customsmssender-lambdaarn"></a>
The Amazon Resource Name (ARN) of the function that you want to assign to your Lambda trigger.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LambdaVersion`  <a name="cfn-cognito-userpool-customsmssender-lambdaversion"></a>
The user pool trigger version of the request that Amazon Cognito sends to your Lambda function. Higher-numbered versions add fields that support new features.
You must use a `LambdaVersion` of `V1_0` with a custom sender function.
*Required*: No
*Type*: String
*Allowed values*: `V1_0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
