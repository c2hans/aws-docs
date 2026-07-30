---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentmanager-customclaimvalidationtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentManager CustomClaimValidationType
<a name="aws-properties-bedrockagentcore-paymentmanager-customclaimvalidationtype"></a>

Defines a custom claim validation to apply when authorizing inbound JWT tokens.

## Syntax
<a name="aws-properties-bedrockagentcore-paymentmanager-customclaimvalidationtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentmanager-customclaimvalidationtype-syntax.json"></a>

```
{
  "[AuthorizingClaimMatchValue](#cfn-bedrockagentcore-paymentmanager-customclaimvalidationtype-authorizingclaimmatchvalue)" : {{AuthorizingClaimMatchValueType}},
  "[InboundTokenClaimName](#cfn-bedrockagentcore-paymentmanager-customclaimvalidationtype-inboundtokenclaimname)" : {{String}},
  "[InboundTokenClaimValueType](#cfn-bedrockagentcore-paymentmanager-customclaimvalidationtype-inboundtokenclaimvaluetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentmanager-customclaimvalidationtype-syntax.yaml"></a>

```
  [AuthorizingClaimMatchValue](#cfn-bedrockagentcore-paymentmanager-customclaimvalidationtype-authorizingclaimmatchvalue): {{
    AuthorizingClaimMatchValueType}}
  [InboundTokenClaimName](#cfn-bedrockagentcore-paymentmanager-customclaimvalidationtype-inboundtokenclaimname): {{String}}
  [InboundTokenClaimValueType](#cfn-bedrockagentcore-paymentmanager-customclaimvalidationtype-inboundtokenclaimvaluetype): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentmanager-customclaimvalidationtype-properties"></a>

`AuthorizingClaimMatchValue`  <a name="cfn-bedrockagentcore-paymentmanager-customclaimvalidationtype-authorizingclaimmatchvalue"></a>
The value or values to match against the claim.
*Required*: Yes
*Type*: [AuthorizingClaimMatchValueType](aws-properties-bedrockagentcore-paymentmanager-authorizingclaimmatchvaluetype.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InboundTokenClaimName`  <a name="cfn-bedrockagentcore-paymentmanager-customclaimvalidationtype-inboundtokenclaimname"></a>
The name of the claim in the inbound JWT token to validate.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_.:/-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InboundTokenClaimValueType`  <a name="cfn-bedrockagentcore-paymentmanager-customclaimvalidationtype-inboundtokenclaimvaluetype"></a>
The data type of the claim value. Valid values are `STRING` and `STRING_ARRAY`.
*Required*: Yes
*Type*: String
*Allowed values*: `STRING | STRING_ARRAY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
