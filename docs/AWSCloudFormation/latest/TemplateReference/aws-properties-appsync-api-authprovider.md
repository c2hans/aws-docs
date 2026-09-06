---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-api-authprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::Api AuthProvider
<a name="aws-properties-appsync-api-authprovider"></a>

Describes an authorization provider.

## Syntax
<a name="aws-properties-appsync-api-authprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-api-authprovider-syntax.json"></a>

```
{
  "[AuthType](#cfn-appsync-api-authprovider-authtype)" : {{String}},
  "[CognitoConfig](#cfn-appsync-api-authprovider-cognitoconfig)" : {{CognitoConfig}},
  "[LambdaAuthorizerConfig](#cfn-appsync-api-authprovider-lambdaauthorizerconfig)" : {{LambdaAuthorizerConfig}},
  "[OpenIDConnectConfig](#cfn-appsync-api-authprovider-openidconnectconfig)" : {{OpenIDConnectConfig}}
}
```

### YAML
<a name="aws-properties-appsync-api-authprovider-syntax.yaml"></a>

```
  [AuthType](#cfn-appsync-api-authprovider-authtype): {{String}}
  [CognitoConfig](#cfn-appsync-api-authprovider-cognitoconfig): {{
    CognitoConfig}}
  [LambdaAuthorizerConfig](#cfn-appsync-api-authprovider-lambdaauthorizerconfig): {{
    LambdaAuthorizerConfig}}
  [OpenIDConnectConfig](#cfn-appsync-api-authprovider-openidconnectconfig): {{
    OpenIDConnectConfig}}
```

## Properties
<a name="aws-properties-appsync-api-authprovider-properties"></a>

`AuthType`  <a name="cfn-appsync-api-authprovider-authtype"></a>
The authorization type.
*Required*: Yes
*Type*: String
*Allowed values*: `AMAZON_COGNITO_USER_POOLS | AWS_IAM | API_KEY | OPENID_CONNECT | AWS_LAMBDA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CognitoConfig`  <a name="cfn-appsync-api-authprovider-cognitoconfig"></a>
Describes an Amazon Cognito user pool configuration.
*Required*: No
*Type*: [CognitoConfig](aws-properties-appsync-api-cognitoconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LambdaAuthorizerConfig`  <a name="cfn-appsync-api-authprovider-lambdaauthorizerconfig"></a>
A `LambdaAuthorizerConfig` specifies how to authorize AWS AppSync API access when using the `AWS_LAMBDA` authorizer mode. Be aware that an AWS AppSync API can have only one AWS Lambda authorizer configured at a time.
*Required*: No
*Type*: [LambdaAuthorizerConfig](aws-properties-appsync-api-lambdaauthorizerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OpenIDConnectConfig`  <a name="cfn-appsync-api-authprovider-openidconnectconfig"></a>
Describes an OpenID Connect (OIDC) configuration.
*Required*: No
*Type*: [OpenIDConnectConfig](aws-properties-appsync-api-openidconnectconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
