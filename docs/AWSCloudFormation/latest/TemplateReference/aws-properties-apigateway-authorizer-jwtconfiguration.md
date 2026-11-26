---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigateway-authorizer-jwtconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::Authorizer JwtConfiguration

The `JwtConfiguration` property type specifies the issuers and signing algorithms that a `JWT` authorizer accepts.

`JwtConfiguration` is a property of the [AWS::ApiGateway::Authorizer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html) resource.

## Syntax
<a name="aws-properties-apigateway-authorizer-jwtconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigateway-authorizer-jwtconfiguration-syntax.json"></a>

```json
{
  "[DefaultAlgorithms](#cfn-apigateway-authorizer-jwtconfiguration-defaultalgorithms)" : {{[ String, ... ]}},
  "[Issuers](#cfn-apigateway-authorizer-jwtconfiguration-issuers)" : {{[ JwtIssuer, ... ]}}
}
```

### YAML
<a name="aws-properties-apigateway-authorizer-jwtconfiguration-syntax.yaml"></a>

```yaml
  [DefaultAlgorithms](#cfn-apigateway-authorizer-jwtconfiguration-defaultalgorithms): {{
    - String}}
  [Issuers](#cfn-apigateway-authorizer-jwtconfiguration-issuers): {{
    - JwtIssuer}}
```

## Properties
<a name="aws-properties-apigateway-authorizer-jwtconfiguration-properties"></a>

`DefaultAlgorithms`  <a name="cfn-apigateway-authorizer-jwtconfiguration-defaultalgorithms"></a>
The signing algorithms that the authorizer accepts, applied to every issuer. Valid values are `RS256`, `RS384`, `RS512`, `ES256`, `ES384`, and `ES512`.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Issuers`  <a name="cfn-apigateway-authorizer-jwtconfiguration-issuers"></a>
The issuers that the authorizer trusts. Issuer URLs must be unique.
*Required*: Yes
*Type*: Array of [JwtIssuer](aws-properties-apigateway-authorizer-jwtissuer.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-apigateway-authorizer-jwtconfiguration--seealso"></a>
+ [JwtConfigurationInput](https://docs.aws.amazon.com/apigateway/latest/api/API_JwtConfigurationInput.html) in the *Amazon API Gateway REST API Reference*
