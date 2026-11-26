---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigateway-authorizer-jwtadditionalclaim.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::Authorizer JwtAdditionalClaim

The `JwtAdditionalClaim` property type specifies a claim rule that a token from the issuer must satisfy, in addition to the issuer, audience, and signing algorithm checks.

`JwtAdditionalClaim` is a property of the [JwtIssuer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-authorizer-jwtissuer.html) property type.

## Syntax
<a name="aws-properties-apigateway-authorizer-jwtadditionalclaim-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigateway-authorizer-jwtadditionalclaim-syntax.json"></a>

```json
{
  "[ClaimName](#cfn-apigateway-authorizer-jwtadditionalclaim-claimname)" : {{String}},
  "[ExpectedValues](#cfn-apigateway-authorizer-jwtadditionalclaim-expectedvalues)" : {{[ String, ... ]}},
  "[Format](#cfn-apigateway-authorizer-jwtadditionalclaim-format)" : {{String}},
  "[Required](#cfn-apigateway-authorizer-jwtadditionalclaim-required)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-apigateway-authorizer-jwtadditionalclaim-syntax.yaml"></a>

```yaml
  [ClaimName](#cfn-apigateway-authorizer-jwtadditionalclaim-claimname): {{String}}
  [ExpectedValues](#cfn-apigateway-authorizer-jwtadditionalclaim-expectedvalues): {{
    - String}}
  [Format](#cfn-apigateway-authorizer-jwtadditionalclaim-format): {{String}}
  [Required](#cfn-apigateway-authorizer-jwtadditionalclaim-required): {{Boolean}}
```

## Properties
<a name="aws-properties-apigateway-authorizer-jwtadditionalclaim-properties"></a>

`ClaimName`  <a name="cfn-apigateway-authorizer-jwtadditionalclaim-claimname"></a>
The name of the claim to check. The value cannot be empty and cannot be `iss`, `aud`, `exp`, `nbf`, `iat`, `scope`, or `scp`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExpectedValues`  <a name="cfn-apigateway-authorizer-jwtadditionalclaim-expectedvalues"></a>
The accepted value for the claim. The value cannot be empty. When a value is specified, the claim must match it exactly, and the match is case-sensitive. When no value is specified, the claim only has to be present.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-apigateway-authorizer-jwtadditionalclaim-format"></a>
The format of the claim value. The only valid value is `SINGLE_STRING`.
*Required*: Yes
*Type*: String
*Allowed values*: `SINGLE_STRING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Required`  <a name="cfn-apigateway-authorizer-jwtadditionalclaim-required"></a>
Specifies whether the claim must be present in the token. Defaults to `false`. When `true`, the token must contain the claim.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-apigateway-authorizer-jwtadditionalclaim--seealso"></a>
+ [JwtAdditionalClaim](https://docs.aws.amazon.com/apigateway/latest/api/API_JwtAdditionalClaim.html) in the *Amazon API Gateway REST API Reference*
