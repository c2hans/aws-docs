---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-weightedoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule WeightedOverride
<a name="aws-properties-bedrockagentcore-gatewayrule-weightedoverride"></a>

A weighted configuration bundle override that splits traffic between multiple bundle versions.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-weightedoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-weightedoverride-syntax.json"></a>

```
{
  "[TrafficSplit](#cfn-bedrockagentcore-gatewayrule-weightedoverride-trafficsplit)" : {{[ TrafficSplitEntry, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-weightedoverride-syntax.yaml"></a>

```
  [TrafficSplit](#cfn-bedrockagentcore-gatewayrule-weightedoverride-trafficsplit): {{
    - TrafficSplitEntry}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-weightedoverride-properties"></a>

`TrafficSplit`  <a name="cfn-bedrockagentcore-gatewayrule-weightedoverride-trafficsplit"></a>
The traffic split entries defining how traffic is distributed between configuration bundle versions.
*Required*: Yes
*Type*: Array of [TrafficSplitEntry](aws-properties-bedrockagentcore-gatewayrule-trafficsplitentry.md)
*Minimum*: `2`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
