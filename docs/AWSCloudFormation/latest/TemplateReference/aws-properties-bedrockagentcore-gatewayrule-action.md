---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule Action
<a name="aws-properties-bedrockagentcore-gatewayrule-action"></a>

An action to take when a gateway rule's conditions are met.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-action-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-action-syntax.json"></a>

```
{
  "[ConfigurationBundle](#cfn-bedrockagentcore-gatewayrule-action-configurationbundle)" : {{ConfigurationBundleAction}},
  "[RouteToTarget](#cfn-bedrockagentcore-gatewayrule-action-routetotarget)" : {{RouteToTargetAction}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-action-syntax.yaml"></a>

```
  [ConfigurationBundle](#cfn-bedrockagentcore-gatewayrule-action-configurationbundle): {{
    ConfigurationBundleAction}}
  [RouteToTarget](#cfn-bedrockagentcore-gatewayrule-action-routetotarget): {{
    RouteToTargetAction}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-action-properties"></a>

`ConfigurationBundle`  <a name="cfn-bedrockagentcore-gatewayrule-action-configurationbundle"></a>
An action that applies a configuration bundle override to the request.
*Required*: No
*Type*: [ConfigurationBundleAction](aws-properties-bedrockagentcore-gatewayrule-configurationbundleaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RouteToTarget`  <a name="cfn-bedrockagentcore-gatewayrule-action-routetotarget"></a>
An action that routes the request to a specific target.
*Required*: No
*Type*: [RouteToTargetAction](aws-properties-bedrockagentcore-gatewayrule-routetotargetaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
