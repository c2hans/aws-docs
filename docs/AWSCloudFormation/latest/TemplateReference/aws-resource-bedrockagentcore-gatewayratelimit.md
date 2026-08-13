---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-gatewayratelimit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRateLimit
<a name="aws-resource-bedrockagentcore-gatewayratelimit"></a>

Creates a rate limit for a gateway. Rate limits define throttling rules for each dimension that control request rates, token consumption rates, and concurrent connections through the gateway.

## Syntax
<a name="aws-resource-bedrockagentcore-gatewayratelimit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-gatewayratelimit-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::GatewayRateLimit",
  "Properties" : {
      "[Description](#cfn-bedrockagentcore-gatewayratelimit-description)" : {{String}},
      "[DimensionKeys](#cfn-bedrockagentcore-gatewayratelimit-dimensionkeys)" : {{[ String, ... ]}},
      "[Entries](#cfn-bedrockagentcore-gatewayratelimit-entries)" : {{[ LimitEntry, ... ]}},
      "[GatewayIdentifier](#cfn-bedrockagentcore-gatewayratelimit-gatewayidentifier)" : {{String}},
      "[RateLimitId](#cfn-bedrockagentcore-gatewayratelimit-ratelimitid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-gatewayratelimit-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::GatewayRateLimit
Properties:
  [Description](#cfn-bedrockagentcore-gatewayratelimit-description): {{String}}
  [DimensionKeys](#cfn-bedrockagentcore-gatewayratelimit-dimensionkeys): {{
    - String}}
  [Entries](#cfn-bedrockagentcore-gatewayratelimit-entries): {{
    - LimitEntry}}
  [GatewayIdentifier](#cfn-bedrockagentcore-gatewayratelimit-gatewayidentifier): {{String}}
  [RateLimitId](#cfn-bedrockagentcore-gatewayratelimit-ratelimitid): {{String}}
```

## Properties
<a name="aws-resource-bedrockagentcore-gatewayratelimit-properties"></a>

`Description`  <a name="cfn-bedrockagentcore-gatewayratelimit-description"></a>
The human-readable description of the rate limit.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DimensionKeys`  <a name="cfn-bedrockagentcore-gatewayratelimit-dimensionkeys"></a>
The ordered list of dimension key names that define the scope of this rate limit.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `80 | 10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Entries`  <a name="cfn-bedrockagentcore-gatewayratelimit-entries"></a>
The list of rule entries that map dimension values to rate configurations.
*Required*: Yes
*Type*: Array of [LimitEntry](aws-properties-bedrockagentcore-gatewayratelimit-limitentry.md)
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GatewayIdentifier`  <a name="cfn-bedrockagentcore-gatewayratelimit-gatewayidentifier"></a>
The unique identifier of the gateway.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-z][-]?){1,100}-[0-9a-z]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RateLimitId`  <a name="cfn-bedrockagentcore-gatewayratelimit-ratelimitid"></a>
The unique identifier of the rate limit.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9\-_\.]{0,62}[a-zA-Z0-9]$`
*Minimum*: `2`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-bedrockagentcore-gatewayratelimit-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-gatewayratelimit-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-gatewayratelimit-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrockagentcore-gatewayratelimit-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the rate limit was created.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the rate limit.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the rate limit was last updated.
