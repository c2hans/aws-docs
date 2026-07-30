---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime CustomJWTAuthorizerConfiguration
<a name="aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration"></a>

Configuration for inbound JWT-based authorization, specifying how incoming requests should be authenticated.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration-syntax.json"></a>

```
{
  "[AllowedAudience](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedaudience)" : {{[ String, ... ]}},
  "[AllowedClients](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedclients)" : {{[ String, ... ]}},
  "[AllowedScopes](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedscopes)" : {{[ String, ... ]}},
  "[AllowedWorkloadConfiguration](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedworkloadconfiguration)" : {{AllowedWorkloadConfiguration}},
  "[CustomClaims](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-customclaims)" : {{[ CustomClaimValidationType, ... ]}},
  "[DiscoveryUrl](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-discoveryurl)" : {{String}},
  "[PrivateEndpoint](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-privateendpoint)" : {{PrivateEndpoint}},
  "[PrivateEndpointOverrides](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-privateendpointoverrides)" : {{[ PrivateEndpointOverride, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration-syntax.yaml"></a>

```
  [AllowedAudience](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedaudience): {{
    - String}}
  [AllowedClients](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedclients): {{
    - String}}
  [AllowedScopes](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedscopes): {{
    - String}}
  [AllowedWorkloadConfiguration](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedworkloadconfiguration): {{
    AllowedWorkloadConfiguration}}
  [CustomClaims](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-customclaims): {{
    - CustomClaimValidationType}}
  [DiscoveryUrl](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-discoveryurl): {{String}}
  [PrivateEndpoint](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-privateendpoint): {{
    PrivateEndpoint}}
  [PrivateEndpointOverrides](#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-privateendpointoverrides): {{
    - PrivateEndpointOverride}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration-properties"></a>

`AllowedAudience`  <a name="cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedaudience"></a>
Represents individual audience values that are validated in the incoming JWT token validation process.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedClients`  <a name="cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedclients"></a>
Represents individual client IDs that are validated in the incoming JWT token validation process.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedScopes`  <a name="cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedscopes"></a>
An array of scopes that are allowed to access the token.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedWorkloadConfiguration`  <a name="cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedworkloadconfiguration"></a>
The configuration that restricts which workloads in the request's identity chain are allowed to invoke the target, identified by their hosting environments and workload identities. At launch, this is supported only for AgentCore Runtime targets, and the allowed workloads are AgentCore Gateways.
*Required*: No
*Type*: [AllowedWorkloadConfiguration](aws-properties-bedrockagentcore-runtime-allowedworkloadconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomClaims`  <a name="cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-customclaims"></a>
An array of objects that define a custom claim validation name, value, and operation
*Required*: No
*Type*: Array of [CustomClaimValidationType](aws-properties-bedrockagentcore-runtime-customclaimvalidationtype.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DiscoveryUrl`  <a name="cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-discoveryurl"></a>
This URL is used to fetch OpenID Connect configuration or authorization server metadata for validating incoming tokens.
*Required*: Yes
*Type*: String
*Pattern*: `^.+/\.well-known/openid-configuration$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateEndpoint`  <a name="cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-privateendpoint"></a>
Property description not available.
*Required*: No
*Type*: [PrivateEndpoint](aws-properties-bedrockagentcore-runtime-privateendpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateEndpointOverrides`  <a name="cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-privateendpointoverrides"></a>
The private endpoint overrides for the custom JWT authorizer configuration.
*Required*: No
*Type*: Array of [PrivateEndpointOverride](aws-properties-bedrockagentcore-runtime-privateendpointoverride.md)
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
