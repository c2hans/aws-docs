---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigateway-authorizer-jwtissuer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::Authorizer JwtIssuer

The `JwtIssuer` property type specifies an issuer that a `JWT` authorizer trusts, the audiences it accepts from that issuer, and any additional claim rules.

`JwtIssuer` is a property of the [JwtConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-authorizer-jwtconfiguration.html) property type.

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
The additional claim rules for this issuer. Claim names must be unique within the issuer.
*Required*: No
*Type*: Array of [JwtAdditionalClaim](aws-properties-apigateway-authorizer-jwtadditionalclaim.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Audiences`  <a name="cfn-apigateway-authorizer-jwtissuer-audiences"></a>
The audiences that the issuer can issue tokens for. None can be empty. The token's `aud` claim must contain at least one of these values.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Issuer`  <a name="cfn-apigateway-authorizer-jwtissuer-issuer"></a>
The OpenID Connect (OIDC) issuer URL. The value must be an absolute `https` URL that includes a host and has no user information, query, or fragment. It must exactly match the `iss` claim of the token, and the issuer's OIDC discovery document must name this exact issuer.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-apigateway-authorizer-jwtissuer--seealso"></a>
+ [JwtIssuerInput](https://docs.aws.amazon.com/apigateway/latest/api/API_JwtIssuerInput.html) in the *Amazon API Gateway REST API Reference*
