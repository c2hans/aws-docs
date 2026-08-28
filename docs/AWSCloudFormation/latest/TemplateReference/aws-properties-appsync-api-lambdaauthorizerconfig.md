---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-api-lambdaauthorizerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::Api LambdaAuthorizerConfig
<a name="aws-properties-appsync-api-lambdaauthorizerconfig"></a>

A `LambdaAuthorizerConfig` specifies how to authorize AWS AppSync API access when using the `AWS_LAMBDA` authorizer mode. Be aware that an AWS AppSync API can have only one AWS Lambda authorizer configured at a time.

## Syntax
<a name="aws-properties-appsync-api-lambdaauthorizerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-api-lambdaauthorizerconfig-syntax.json"></a>

```
{
  "[AuthorizerResultTtlInSeconds](#cfn-appsync-api-lambdaauthorizerconfig-authorizerresultttlinseconds)" : {{Integer}},
  "[AuthorizerUri](#cfn-appsync-api-lambdaauthorizerconfig-authorizeruri)" : {{String}},
  "[IdentityValidationExpression](#cfn-appsync-api-lambdaauthorizerconfig-identityvalidationexpression)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-api-lambdaauthorizerconfig-syntax.yaml"></a>

```
  [AuthorizerResultTtlInSeconds](#cfn-appsync-api-lambdaauthorizerconfig-authorizerresultttlinseconds): {{Integer}}
  [AuthorizerUri](#cfn-appsync-api-lambdaauthorizerconfig-authorizeruri): {{String}}
  [IdentityValidationExpression](#cfn-appsync-api-lambdaauthorizerconfig-identityvalidationexpression): {{String}}
```

## Properties
<a name="aws-properties-appsync-api-lambdaauthorizerconfig-properties"></a>

`AuthorizerResultTtlInSeconds`  <a name="cfn-appsync-api-lambdaauthorizerconfig-authorizerresultttlinseconds"></a>
The number of seconds a response should be cached for. The default is 0 seconds, which disables caching. If you don't specify a value for `authorizerResultTtlInSeconds`, the default value is used. The maximum value is one hour (3600 seconds). The Lambda function can override this by returning a `ttlOverride` key in its response.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizerUri`  <a name="cfn-appsync-api-lambdaauthorizerconfig-authorizeruri"></a>
The Amazon Resource Name (ARN) of the Lambda function to be called for authorization. This can be a standard Lambda ARN, a version ARN (`.../v3`), or an alias ARN.
**Note**: This Lambda function must have the following resource-based policy assigned to it. When configuring Lambda authorizers in the console, this is done for you. To use the AWS Command Line Interface (AWS CLI), run the following:
 `aws lambda add-permission --function-name "arn:aws:lambda:us-east-2:111122223333:function:my-function" --statement-id "appsync" --principal appsync.amazonaws.com --action lambda:InvokeFunction`
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityValidationExpression`  <a name="cfn-appsync-api-lambdaauthorizerconfig-identityvalidationexpression"></a>
A regular expression for validation of tokens before the Lambda function is called.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
