---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway CustomJWTAuthorizerConfiguration
<a name="aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration"></a>

Configuration for inbound JWT-based authorization, specifying how incoming requests should be authenticated.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration-syntax.json"></a>

```
{
  "[AllowedAudience](#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-allowedaudience)" : {{[ String, ... ]}},
  "[AllowedClients](#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-allowedclients)" : {{[ String, ... ]}},
  "[AllowedScopes](#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-allowedscopes)" : {{[ String, ... ]}},
  "[CustomClaims](#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-customclaims)" : {{[ CustomClaimValidationType, ... ]}},
  "[DiscoveryUrl](#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-discoveryurl)" : {{String}},
  "[PrivateEndpoint](#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-privateendpoint)" : {{PrivateEndpoint}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration-syntax.yaml"></a>

```
  [AllowedAudience](#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-allowedaudience): {{
    - String}}
  [AllowedClients](#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-allowedclients): {{
    - String}}
  [AllowedScopes](#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-allowedscopes): {{
    - String}}
  [CustomClaims](#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-customclaims): {{
    - CustomClaimValidationType}}
  [DiscoveryUrl](#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-discoveryurl): {{String}}
  [PrivateEndpoint](#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-privateendpoint): {{
    PrivateEndpoint}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration-properties"></a>

`AllowedAudience`  <a name="cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-allowedaudience"></a>
Represents individual audience values that are validated in the incoming JWT token validation process.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedClients`  <a name="cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-allowedclients"></a>
Represents individual client IDs that are validated in the incoming JWT token validation process.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedScopes`  <a name="cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-allowedscopes"></a>
An array of scopes that are allowed to access the token.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomClaims`  <a name="cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-customclaims"></a>
An array of objects that define a custom claim validation name, value, and operation
*Required*: No
*Type*: Array of [CustomClaimValidationType](aws-properties-bedrockagentcore-gateway-customclaimvalidationtype.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DiscoveryUrl`  <a name="cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-discoveryurl"></a>
This URL is used to fetch OpenID Connect configuration or authorization server metadata for validating incoming tokens.
*Required*: Yes
*Type*: String
*Pattern*: `^.+/\.well-known/openid-configuration$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateEndpoint`  <a name="cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-privateendpoint"></a>
Property description not available.
*Required*: No
*Type*: [PrivateEndpoint](aws-properties-bedrockagentcore-gateway-privateendpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
