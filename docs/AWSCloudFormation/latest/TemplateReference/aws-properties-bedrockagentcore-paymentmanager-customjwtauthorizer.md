---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentmanager-customjwtauthorizer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentManager CustomJWTAuthorizer
<a name="aws-properties-bedrockagentcore-paymentmanager-customjwtauthorizer"></a>

<a name="aws-properties-bedrockagentcore-paymentmanager-customjwtauthorizer-description"></a>The `CustomJWTAuthorizer` property type specifies Property description not available. for an [AWS::BedrockAgentCore::PaymentManager](aws-resource-bedrockagentcore-paymentmanager.md).

## Syntax
<a name="aws-properties-bedrockagentcore-paymentmanager-customjwtauthorizer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentmanager-customjwtauthorizer-syntax.json"></a>

```
{
  "[AllowedAudience](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizer-allowedaudience)" : {{[ String, ... ]}},
  "[AllowedClients](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizer-allowedclients)" : {{[ String, ... ]}},
  "[AllowedScopes](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizer-allowedscopes)" : {{[ String, ... ]}},
  "[CustomClaims](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizer-customclaims)" : {{[ CustomClaimValidationType, ... ]}},
  "[DiscoveryUrl](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizer-discoveryurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentmanager-customjwtauthorizer-syntax.yaml"></a>

```
  [AllowedAudience](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizer-allowedaudience): {{
    - String}}
  [AllowedClients](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizer-allowedclients): {{
    - String}}
  [AllowedScopes](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizer-allowedscopes): {{
    - String}}
  [CustomClaims](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizer-customclaims): {{
    - CustomClaimValidationType}}
  [DiscoveryUrl](#cfn-bedrockagentcore-paymentmanager-customjwtauthorizer-discoveryurl): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentmanager-customjwtauthorizer-properties"></a>

`AllowedAudience`  <a name="cfn-bedrockagentcore-paymentmanager-customjwtauthorizer-allowedaudience"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AllowedClients`  <a name="cfn-bedrockagentcore-paymentmanager-customjwtauthorizer-allowedclients"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AllowedScopes`  <a name="cfn-bedrockagentcore-paymentmanager-customjwtauthorizer-allowedscopes"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Maximum*: `255`
*Minimum*: `1 | 1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomClaims`  <a name="cfn-bedrockagentcore-paymentmanager-customjwtauthorizer-customclaims"></a>
Property description not available.
*Required*: No
*Type*: Array of [CustomClaimValidationType](aws-properties-bedrockagentcore-paymentmanager-customclaimvalidationtype.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DiscoveryUrl`  <a name="cfn-bedrockagentcore-paymentmanager-customjwtauthorizer-discoveryurl"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\s?#]+/\.well-known/(openid-configuration|oauth-authorization-server)(/[^\s?#]+)?$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
