---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGatewayV2::Authorizer JWTConfiguration
<a name="aws-properties-apigatewayv2-authorizer-jwtconfiguration"></a>

The `JWTConfiguration` property specifies the configuration of a JWT authorizer. Required for the `JWT` authorizer type. Supported only for HTTP APIs.

## Syntax
<a name="aws-properties-apigatewayv2-authorizer-jwtconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigatewayv2-authorizer-jwtconfiguration-syntax.json"></a>

```
{
  "[Audience](#cfn-apigatewayv2-authorizer-jwtconfiguration-audience)" : {{[ String, ... ]}},
  "[Issuer](#cfn-apigatewayv2-authorizer-jwtconfiguration-issuer)" : {{String}}
}
```

### YAML
<a name="aws-properties-apigatewayv2-authorizer-jwtconfiguration-syntax.yaml"></a>

```
  [Audience](#cfn-apigatewayv2-authorizer-jwtconfiguration-audience): {{
    - String}}
  [Issuer](#cfn-apigatewayv2-authorizer-jwtconfiguration-issuer): {{String}}
```

## Properties
<a name="aws-properties-apigatewayv2-authorizer-jwtconfiguration-properties"></a>

`Audience`  <a name="cfn-apigatewayv2-authorizer-jwtconfiguration-audience"></a>
A list of the intended recipients of the JWT. A valid JWT must provide an `aud` that matches at least one entry in this list. See [RFC 7519](https://tools.ietf.org/html/rfc7519#section-4.1.3). Required for the `JWT` authorizer type. Supported only for HTTP APIs.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Issuer`  <a name="cfn-apigatewayv2-authorizer-jwtconfiguration-issuer"></a>
The base domain of the identity provider that issues JSON Web Tokens. For example, an Amazon Cognito user pool has the following format: `https://cognito-idp.{{{region}}}.amazonaws.com/{{{userPoolId}}}`. Required for the `JWT` authorizer type. Supported only for HTTP APIs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
