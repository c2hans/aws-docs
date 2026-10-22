---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentmanager-authorizingclaimmatchvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentManager AuthorizingClaimMatchValue
<a name="aws-properties-bedrockagentcore-paymentmanager-authorizingclaimmatchvalue"></a>

<a name="aws-properties-bedrockagentcore-paymentmanager-authorizingclaimmatchvalue-description"></a>The `AuthorizingClaimMatchValue` property type specifies Property description not available. for an [AWS::BedrockAgentCore::PaymentManager](aws-resource-bedrockagentcore-paymentmanager.md).

## Syntax
<a name="aws-properties-bedrockagentcore-paymentmanager-authorizingclaimmatchvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentmanager-authorizingclaimmatchvalue-syntax.json"></a>

```
{
  "[ClaimMatchOperator](#cfn-bedrockagentcore-paymentmanager-authorizingclaimmatchvalue-claimmatchoperator)" : {{String}},
  "[ClaimMatchValue](#cfn-bedrockagentcore-paymentmanager-authorizingclaimmatchvalue-claimmatchvalue)" : {{ClaimMatchValue}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentmanager-authorizingclaimmatchvalue-syntax.yaml"></a>

```
  [ClaimMatchOperator](#cfn-bedrockagentcore-paymentmanager-authorizingclaimmatchvalue-claimmatchoperator): {{String}}
  [ClaimMatchValue](#cfn-bedrockagentcore-paymentmanager-authorizingclaimmatchvalue-claimmatchvalue): {{
    ClaimMatchValue}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentmanager-authorizingclaimmatchvalue-properties"></a>

`ClaimMatchOperator`  <a name="cfn-bedrockagentcore-paymentmanager-authorizingclaimmatchvalue-claimmatchoperator"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS | CONTAINS | CONTAINS_ANY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClaimMatchValue`  <a name="cfn-bedrockagentcore-paymentmanager-authorizingclaimmatchvalue-claimmatchvalue"></a>
Property description not available.
*Required*: Yes
*Type*: [ClaimMatchValue](aws-properties-bedrockagentcore-paymentmanager-claimmatchvalue.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
