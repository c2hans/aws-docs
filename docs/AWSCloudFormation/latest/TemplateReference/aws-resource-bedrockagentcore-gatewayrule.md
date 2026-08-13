---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-gatewayrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule
<a name="aws-resource-bedrockagentcore-gatewayrule"></a>

Creates a rule for a gateway. Rules define conditions and actions that control how requests are routed and processed through the gateway, including principal-based access control and path-based routing.

## Syntax
<a name="aws-resource-bedrockagentcore-gatewayrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-gatewayrule-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::GatewayRule",
  "Properties" : {
      "[Actions](#cfn-bedrockagentcore-gatewayrule-actions)" : {{[ Action, ... ]}},
      "[Conditions](#cfn-bedrockagentcore-gatewayrule-conditions)" : {{[ Condition, ... ]}},
      "[Description](#cfn-bedrockagentcore-gatewayrule-description)" : {{String}},
      "[GatewayIdentifier](#cfn-bedrockagentcore-gatewayrule-gatewayidentifier)" : {{String}},
      "[Priority](#cfn-bedrockagentcore-gatewayrule-priority)" : {{Number}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-gatewayrule-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::GatewayRule
Properties:
  [Actions](#cfn-bedrockagentcore-gatewayrule-actions): {{
    - Action}}
  [Conditions](#cfn-bedrockagentcore-gatewayrule-conditions): {{
    - Condition}}
  [Description](#cfn-bedrockagentcore-gatewayrule-description): {{String}}
  [GatewayIdentifier](#cfn-bedrockagentcore-gatewayrule-gatewayidentifier): {{String}}
  [Priority](#cfn-bedrockagentcore-gatewayrule-priority): {{Number}}
```

## Properties
<a name="aws-resource-bedrockagentcore-gatewayrule-properties"></a>

`Actions`  <a name="cfn-bedrockagentcore-gatewayrule-actions"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [Action](aws-properties-bedrockagentcore-gatewayrule-action.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Conditions`  <a name="cfn-bedrockagentcore-gatewayrule-conditions"></a>
Property description not available.
*Required*: No
*Type*: Array of [Condition](aws-properties-bedrockagentcore-gatewayrule-condition.md)
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrockagentcore-gatewayrule-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GatewayIdentifier`  <a name="cfn-bedrockagentcore-gatewayrule-gatewayidentifier"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-z][-]?){1,100}-[0-9a-z]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Priority`  <a name="cfn-bedrockagentcore-gatewayrule-priority"></a>
Property description not available.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `1000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-gatewayrule-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-gatewayrule-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-gatewayrule-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrockagentcore-gatewayrule-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`GatewayArn`  <a name="GatewayArn-fn::getatt"></a>
Property description not available.

`RuleId`  <a name="RuleId-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.
