---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registry-customjwtauthorizerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Registry CustomJWTAuthorizerConfiguration
<a name="aws-properties-agentregistry-registry-customjwtauthorizerconfiguration"></a>

Configuration for a custom JSON Web Token (JWT) authorizer that validates inbound bearer tokens against an OpenID Connect (OIDC) identity provider.

## Syntax
<a name="aws-properties-agentregistry-registry-customjwtauthorizerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registry-customjwtauthorizerconfiguration-syntax.json"></a>

```
{
  "[AllowedAudience](#cfn-agentregistry-registry-customjwtauthorizerconfiguration-allowedaudience)" : {{[ String, ... ]}},
  "[AllowedClients](#cfn-agentregistry-registry-customjwtauthorizerconfiguration-allowedclients)" : {{[ String, ... ]}},
  "[AllowedScopes](#cfn-agentregistry-registry-customjwtauthorizerconfiguration-allowedscopes)" : {{[ String, ... ]}},
  "[CustomClaims](#cfn-agentregistry-registry-customjwtauthorizerconfiguration-customclaims)" : {{[ CustomClaimValidationType, ... ]}},
  "[DiscoveryUrl](#cfn-agentregistry-registry-customjwtauthorizerconfiguration-discoveryurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registry-customjwtauthorizerconfiguration-syntax.yaml"></a>

```
  [AllowedAudience](#cfn-agentregistry-registry-customjwtauthorizerconfiguration-allowedaudience): {{
    - String}}
  [AllowedClients](#cfn-agentregistry-registry-customjwtauthorizerconfiguration-allowedclients): {{
    - String}}
  [AllowedScopes](#cfn-agentregistry-registry-customjwtauthorizerconfiguration-allowedscopes): {{
    - String}}
  [CustomClaims](#cfn-agentregistry-registry-customjwtauthorizerconfiguration-customclaims): {{
    - CustomClaimValidationType}}
  [DiscoveryUrl](#cfn-agentregistry-registry-customjwtauthorizerconfiguration-discoveryurl): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registry-customjwtauthorizerconfiguration-properties"></a>

`AllowedAudience`  <a name="cfn-agentregistry-registry-customjwtauthorizerconfiguration-allowedaudience"></a>
The audience values accepted during JWT validation.
*Required*: No
*Type*: Array of String
*Maximum*: `255`
*Minimum*: `1 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedClients`  <a name="cfn-agentregistry-registry-customjwtauthorizerconfiguration-allowedclients"></a>
The client identifiers accepted during JWT validation.
*Required*: No
*Type*: Array of String
*Maximum*: `255`
*Minimum*: `1 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedScopes`  <a name="cfn-agentregistry-registry-customjwtauthorizerconfiguration-allowedscopes"></a>
The scopes accepted during JWT validation.
*Required*: No
*Type*: Array of String
*Maximum*: `255`
*Minimum*: `1 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomClaims`  <a name="cfn-agentregistry-registry-customjwtauthorizerconfiguration-customclaims"></a>
Additional custom claim validations applied to the inbound JWT.
*Required*: No
*Type*: Array of [CustomClaimValidationType](aws-properties-agentregistry-registry-customclaimvalidationtype.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DiscoveryUrl`  <a name="cfn-agentregistry-registry-customjwtauthorizerconfiguration-discoveryurl"></a>
The OpenID Connect discovery URL used to retrieve the identity provider's metadata and signing keys.
*Required*: Yes
*Type*: String
*Pattern*: `^.+/\.well-known/openid-configuration$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
