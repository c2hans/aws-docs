---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::GraphQLApi AdditionalAuthenticationProvider
<a name="aws-properties-appsync-graphqlapi-additionalauthenticationprovider"></a>

Describes an additional authentication provider.

## Syntax
<a name="aws-properties-appsync-graphqlapi-additionalauthenticationprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-graphqlapi-additionalauthenticationprovider-syntax.json"></a>

```
{
  "[AuthenticationType](#cfn-appsync-graphqlapi-additionalauthenticationprovider-authenticationtype)" : {{String}},
  "[LambdaAuthorizerConfig](#cfn-appsync-graphqlapi-additionalauthenticationprovider-lambdaauthorizerconfig)" : {{LambdaAuthorizerConfig}},
  "[OpenIDConnectConfig](#cfn-appsync-graphqlapi-additionalauthenticationprovider-openidconnectconfig)" : {{OpenIDConnectConfig}},
  "[UserPoolConfig](#cfn-appsync-graphqlapi-additionalauthenticationprovider-userpoolconfig)" : {{CognitoUserPoolConfig}}
}
```

### YAML
<a name="aws-properties-appsync-graphqlapi-additionalauthenticationprovider-syntax.yaml"></a>

```
  [AuthenticationType](#cfn-appsync-graphqlapi-additionalauthenticationprovider-authenticationtype): {{String}}
  [LambdaAuthorizerConfig](#cfn-appsync-graphqlapi-additionalauthenticationprovider-lambdaauthorizerconfig): {{
    LambdaAuthorizerConfig}}
  [OpenIDConnectConfig](#cfn-appsync-graphqlapi-additionalauthenticationprovider-openidconnectconfig): {{
    OpenIDConnectConfig}}
  [UserPoolConfig](#cfn-appsync-graphqlapi-additionalauthenticationprovider-userpoolconfig): {{
    CognitoUserPoolConfig}}
```

## Properties
<a name="aws-properties-appsync-graphqlapi-additionalauthenticationprovider-properties"></a>

`AuthenticationType`  <a name="cfn-appsync-graphqlapi-additionalauthenticationprovider-authenticationtype"></a>
The authentication type for API key, AWS Identity and Access Management, OIDC, Amazon Cognito user pools, or AWS Lambda.
Valid Values: `API_KEY` \| `AWS_IAM` \| `OPENID_CONNECT` \| `AMAZON_COGNITO_USER_POOLS` \| `AWS_LAMBDA`
*Required*: Yes
*Type*: String
*Allowed values*: `API_KEY | AWS_IAM | AMAZON_COGNITO_USER_POOLS | OPENID_CONNECT | AWS_LAMBDA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LambdaAuthorizerConfig`  <a name="cfn-appsync-graphqlapi-additionalauthenticationprovider-lambdaauthorizerconfig"></a>
Configuration for AWS Lambda function authorization.
*Required*: No
*Type*: [LambdaAuthorizerConfig](aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OpenIDConnectConfig`  <a name="cfn-appsync-graphqlapi-additionalauthenticationprovider-openidconnectconfig"></a>
The OIDC configuration.
*Required*: No
*Type*: [OpenIDConnectConfig](aws-properties-appsync-graphqlapi-openidconnectconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolConfig`  <a name="cfn-appsync-graphqlapi-additionalauthenticationprovider-userpoolconfig"></a>
The Amazon Cognito user pool configuration.
*Required*: No
*Type*: [CognitoUserPoolConfig](aws-properties-appsync-graphqlapi-cognitouserpoolconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
