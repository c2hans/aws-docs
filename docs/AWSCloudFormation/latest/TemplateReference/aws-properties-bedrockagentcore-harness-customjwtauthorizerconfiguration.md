---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-customjwtauthorizerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness CustomJWTAuthorizerConfiguration
<a name="aws-properties-bedrockagentcore-harness-customjwtauthorizerconfiguration"></a>

Configuration for inbound JWT-based authorization, specifying how incoming requests should be authenticated.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-customjwtauthorizerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-customjwtauthorizerconfiguration-syntax.json"></a>

```
{
  "[AllowedAudience](#cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-allowedaudience)" : {{[ String, ... ]}},
  "[AllowedClients](#cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-allowedclients)" : {{[ String, ... ]}},
  "[AllowedScopes](#cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-allowedscopes)" : {{[ String, ... ]}},
  "[CustomClaims](#cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-customclaims)" : {{[ CustomClaimValidationType, ... ]}},
  "[DiscoveryUrl](#cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-discoveryurl)" : {{String}},
  "[PrivateEndpoint](#cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-privateendpoint)" : {{PrivateEndpoint}},
  "[PrivateEndpointOverrides](#cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-privateendpointoverrides)" : {{[ PrivateEndpointOverride, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-customjwtauthorizerconfiguration-syntax.yaml"></a>

```
  [AllowedAudience](#cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-allowedaudience): {{
    - String}}
  [AllowedClients](#cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-allowedclients): {{
    - String}}
  [AllowedScopes](#cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-allowedscopes): {{
    - String}}
  [CustomClaims](#cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-customclaims): {{
    - CustomClaimValidationType}}
  [DiscoveryUrl](#cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-discoveryurl): {{String}}
  [PrivateEndpoint](#cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-privateendpoint): {{
    PrivateEndpoint}}
  [PrivateEndpointOverrides](#cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-privateendpointoverrides): {{
    - PrivateEndpointOverride}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-customjwtauthorizerconfiguration-properties"></a>

`AllowedAudience`  <a name="cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-allowedaudience"></a>
Represents individual audience values that are validated in the incoming JWT token validation process.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedClients`  <a name="cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-allowedclients"></a>
Represents individual client IDs that are validated in the incoming JWT token validation process.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedScopes`  <a name="cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-allowedscopes"></a>
An array of scopes that are allowed to access the token.
*Required*: No
*Type*: Array of String
*Maximum*: `255`
*Minimum*: `1 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomClaims`  <a name="cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-customclaims"></a>
An array of objects that define a custom claim validation name, value, and operation
*Required*: No
*Type*: Array of [CustomClaimValidationType](aws-properties-bedrockagentcore-harness-customclaimvalidationtype.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DiscoveryUrl`  <a name="cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-discoveryurl"></a>
This URL is used to fetch OpenID Connect configuration or authorization server metadata for validating incoming tokens.
*Required*: Yes
*Type*: String
*Pattern*: `^.+/\.well-known/openid-configuration$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateEndpoint`  <a name="cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-privateendpoint"></a>
Property description not available.
*Required*: No
*Type*: [PrivateEndpoint](aws-properties-bedrockagentcore-harness-privateendpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateEndpointOverrides`  <a name="cfn-bedrockagentcore-harness-customjwtauthorizerconfiguration-privateendpointoverrides"></a>
The private endpoint overrides for the custom JWT authorizer configuration.
*Required*: No
*Type*: Array of [PrivateEndpointOverride](aws-properties-bedrockagentcore-harness-privateendpointoverride.md)
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
