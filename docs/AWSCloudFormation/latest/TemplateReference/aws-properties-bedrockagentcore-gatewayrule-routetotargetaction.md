---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-routetotargetaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule RouteToTargetAction
<a name="aws-properties-bedrockagentcore-gatewayrule-routetotargetaction"></a>

An action that routes requests to a gateway target, either statically or with weighted traffic splitting.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-routetotargetaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-routetotargetaction-syntax.json"></a>

```
{
  "[StaticRoute](#cfn-bedrockagentcore-gatewayrule-routetotargetaction-staticroute)" : {{StaticRoute}},
  "[WeightedRoute](#cfn-bedrockagentcore-gatewayrule-routetotargetaction-weightedroute)" : {{WeightedRoute}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-routetotargetaction-syntax.yaml"></a>

```
  [StaticRoute](#cfn-bedrockagentcore-gatewayrule-routetotargetaction-staticroute): {{
    StaticRoute}}
  [WeightedRoute](#cfn-bedrockagentcore-gatewayrule-routetotargetaction-weightedroute): {{
    WeightedRoute}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-routetotargetaction-properties"></a>

`StaticRoute`  <a name="cfn-bedrockagentcore-gatewayrule-routetotargetaction-staticroute"></a>
A static route that sends all matching requests to a single target.
*Required*: No
*Type*: [StaticRoute](aws-properties-bedrockagentcore-gatewayrule-staticroute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeightedRoute`  <a name="cfn-bedrockagentcore-gatewayrule-routetotargetaction-weightedroute"></a>
A weighted route that splits traffic between multiple targets.
*Required*: No
*Type*: [WeightedRoute](aws-properties-bedrockagentcore-gatewayrule-weightedroute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
