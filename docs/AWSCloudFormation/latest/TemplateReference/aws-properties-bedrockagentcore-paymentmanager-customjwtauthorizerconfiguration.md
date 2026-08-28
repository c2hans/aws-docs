---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentManager CustomJWTAuthorizerConfiguration
<a name="aws-properties-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration"></a>

Configuration for inbound JWT-based authorization, specifying how incoming requests should be authenticated.

## Syntax
<a name="aws-properties-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-syntax.json"></a>

```
{
  "[AllowedAudience](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-allowedaudience)" : {{[ String, ... ]}},
  "[AllowedClients](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-allowedclients)" : {{[ String, ... ]}},
  "[AllowedScopes](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-allowedscopes)" : {{[ String, ... ]}},
  "[CustomClaims](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-customclaims)" : {{[ CustomClaimValidationType, ... ]}},
  "[DiscoveryUrl](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-discoveryurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-syntax.yaml"></a>

```
  [AllowedAudience](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-allowedaudience): {{
    - String}}
  [AllowedClients](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-allowedclients): {{
    - String}}
  [AllowedScopes](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-allowedscopes): {{
    - String}}
  [CustomClaims](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-customclaims): {{
    - CustomClaimValidationType}}
  [DiscoveryUrl](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-discoveryurl): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-properties"></a>

`AllowedAudience`  <a name="cfn-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-allowedaudience"></a>
Represents individual audience values that are validated in the incoming JWT token validation process.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AllowedClients`  <a name="cfn-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-allowedclients"></a>
Represents individual client IDs that are validated in the incoming JWT token validation process.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AllowedScopes`  <a name="cfn-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-allowedscopes"></a>
An array of scopes that are allowed to access the token.
*Required*: No
*Type*: Array of String
*Maximum*: `255`
*Minimum*: `1 | 1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomClaims`  <a name="cfn-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-customclaims"></a>
An array of objects that define a custom claim validation name, value, and operation
*Required*: No
*Type*: Array of [CustomClaimValidationType](aws-properties-bedrockagentcore-paymentmanager-customclaimvalidationtype.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DiscoveryUrl`  <a name="cfn-bedrockagentcore-paymentmanager-customjwtauthorizerconfiguration-discoveryurl"></a>
This URL is used to fetch OpenID Connect configuration or authorization server metadata for validating incoming tokens.
*Required*: Yes
*Type*: String
*Pattern*: `^.+/\.well-known/openid-configuration$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
