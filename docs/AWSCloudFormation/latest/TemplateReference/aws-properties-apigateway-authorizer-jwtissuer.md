---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigateway-authorizer-jwtissuer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::Authorizer JwtIssuer

<a name="aws-properties-apigateway-authorizer-jwtissuer-description"></a>The `JwtIssuer` property type specifies Property description not available. for an [AWS::ApiGateway::Authorizer](aws-resource-apigateway-authorizer.md).

## Syntax
<a name="aws-properties-apigateway-authorizer-jwtissuer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigateway-authorizer-jwtissuer-syntax.json"></a>

```json
{
  "[AdditionalClaims](#cfn-apigateway-authorizer-jwtissuer-additionalclaims)" : {{[ JwtAdditionalClaim, ... ]}},
  "[Audiences](#cfn-apigateway-authorizer-jwtissuer-audiences)" : {{[ String, ... ]}},
  "[Issuer](#cfn-apigateway-authorizer-jwtissuer-issuer)" : {{String}}
}
```

### YAML
<a name="aws-properties-apigateway-authorizer-jwtissuer-syntax.yaml"></a>

```yaml
  [AdditionalClaims](#cfn-apigateway-authorizer-jwtissuer-additionalclaims): {{
    - JwtAdditionalClaim}}
  [Audiences](#cfn-apigateway-authorizer-jwtissuer-audiences): {{
    - String}}
  [Issuer](#cfn-apigateway-authorizer-jwtissuer-issuer): {{String}}
```

## Properties
<a name="aws-properties-apigateway-authorizer-jwtissuer-properties"></a>

`AdditionalClaims`  <a name="cfn-apigateway-authorizer-jwtissuer-additionalclaims"></a>
Property description not available.
*Required*: No
*Type*: Array of [JwtAdditionalClaim](aws-properties-apigateway-authorizer-jwtadditionalclaim.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Audiences`  <a name="cfn-apigateway-authorizer-jwtissuer-audiences"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Issuer`  <a name="cfn-apigateway-authorizer-jwtissuer-issuer"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
