---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-customclaimvalidationtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway CustomClaimValidationType
<a name="aws-properties-bedrockagentcore-gateway-customclaimvalidationtype"></a>

Defines the name of a custom claim field and rules for finding matches to authenticate its value.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-customclaimvalidationtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-customclaimvalidationtype-syntax.json"></a>

```
{
  "[AuthorizingClaimMatchValue](#cfn-bedrockagentcore-gateway-customclaimvalidationtype-authorizingclaimmatchvalue)" : {{AuthorizingClaimMatchValueType}},
  "[InboundTokenClaimName](#cfn-bedrockagentcore-gateway-customclaimvalidationtype-inboundtokenclaimname)" : {{String}},
  "[InboundTokenClaimValueType](#cfn-bedrockagentcore-gateway-customclaimvalidationtype-inboundtokenclaimvaluetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-customclaimvalidationtype-syntax.yaml"></a>

```
  [AuthorizingClaimMatchValue](#cfn-bedrockagentcore-gateway-customclaimvalidationtype-authorizingclaimmatchvalue): {{
    AuthorizingClaimMatchValueType}}
  [InboundTokenClaimName](#cfn-bedrockagentcore-gateway-customclaimvalidationtype-inboundtokenclaimname): {{String}}
  [InboundTokenClaimValueType](#cfn-bedrockagentcore-gateway-customclaimvalidationtype-inboundtokenclaimvaluetype): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-customclaimvalidationtype-properties"></a>

`AuthorizingClaimMatchValue`  <a name="cfn-bedrockagentcore-gateway-customclaimvalidationtype-authorizingclaimmatchvalue"></a>
Defines the value or values to match for and the relationship of the match.
*Required*: Yes
*Type*: [AuthorizingClaimMatchValueType](aws-properties-bedrockagentcore-gateway-authorizingclaimmatchvaluetype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InboundTokenClaimName`  <a name="cfn-bedrockagentcore-gateway-customclaimvalidationtype-inboundtokenclaimname"></a>
The name of the custom claim field to check.
*Required*: Yes
*Type*: String
*Pattern*: `[A-Za-z0-9_.-:]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InboundTokenClaimValueType`  <a name="cfn-bedrockagentcore-gateway-customclaimvalidationtype-inboundtokenclaimvaluetype"></a>
The data type of the claim value to check for.
+ Use `STRING` if you want to find an exact match to a string you define.
+ Use `STRING_ARRAY` if you want to fnd a match to at least one value in an array you define.
*Required*: Yes
*Type*: String
*Allowed values*: `STRING | STRING_ARRAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
