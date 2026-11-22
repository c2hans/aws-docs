---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigateway-authorizer-jwtconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::Authorizer JwtConfiguration

<a name="aws-properties-apigateway-authorizer-jwtconfiguration-description"></a>The `JwtConfiguration` property type specifies Property description not available. for an [AWS::ApiGateway::Authorizer](aws-resource-apigateway-authorizer.md).

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
Property description not available.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Issuers`  <a name="cfn-apigateway-authorizer-jwtconfiguration-issuers"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [JwtIssuer](aws-properties-apigateway-authorizer-jwtissuer.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
