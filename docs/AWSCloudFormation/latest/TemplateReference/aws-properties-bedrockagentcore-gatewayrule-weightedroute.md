---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-weightedroute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule WeightedRoute
<a name="aws-properties-bedrockagentcore-gatewayrule-weightedroute"></a>

A weighted route that splits traffic between multiple gateway targets.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-weightedroute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-weightedroute-syntax.json"></a>

```
{
  "[TrafficSplit](#cfn-bedrockagentcore-gatewayrule-weightedroute-trafficsplit)" : {{[ TargetTrafficSplitEntry, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-weightedroute-syntax.yaml"></a>

```
  [TrafficSplit](#cfn-bedrockagentcore-gatewayrule-weightedroute-trafficsplit): {{
    - TargetTrafficSplitEntry}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-weightedroute-properties"></a>

`TrafficSplit`  <a name="cfn-bedrockagentcore-gatewayrule-weightedroute-trafficsplit"></a>
The traffic split entries defining how traffic is distributed between targets.
*Required*: Yes
*Type*: Array of [TargetTrafficSplitEntry](aws-properties-bedrockagentcore-gatewayrule-targettrafficsplitentry.md)
*Minimum*: `2`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
