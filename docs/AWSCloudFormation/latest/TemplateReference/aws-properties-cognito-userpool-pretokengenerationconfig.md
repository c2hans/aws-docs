---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-pretokengenerationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool PreTokenGenerationConfig
<a name="aws-properties-cognito-userpool-pretokengenerationconfig"></a>

The properties of a pre token generation Lambda trigger.

## Syntax
<a name="aws-properties-cognito-userpool-pretokengenerationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-pretokengenerationconfig-syntax.json"></a>

```
{
  "[LambdaArn](#cfn-cognito-userpool-pretokengenerationconfig-lambdaarn)" : {{String}},
  "[LambdaVersion](#cfn-cognito-userpool-pretokengenerationconfig-lambdaversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-pretokengenerationconfig-syntax.yaml"></a>

```
  [LambdaArn](#cfn-cognito-userpool-pretokengenerationconfig-lambdaarn): {{String}}
  [LambdaVersion](#cfn-cognito-userpool-pretokengenerationconfig-lambdaversion): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpool-pretokengenerationconfig-properties"></a>

`LambdaArn`  <a name="cfn-cognito-userpool-pretokengenerationconfig-lambdaarn"></a>
The Amazon Resource Name (ARN) of the function that you want to assign to your Lambda trigger.
This parameter and the `PreTokenGeneration` property of `LambdaConfig` have the same value. For new instances of pre token generation triggers, set `LambdaArn`.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LambdaVersion`  <a name="cfn-cognito-userpool-pretokengenerationconfig-lambdaversion"></a>
The user pool trigger version of the request that Amazon Cognito sends to your Lambda function. Higher-numbered versions add fields that support new features.
*Required*: No
*Type*: String
*Allowed values*: `V1_0 | V2_0 | V3_0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
