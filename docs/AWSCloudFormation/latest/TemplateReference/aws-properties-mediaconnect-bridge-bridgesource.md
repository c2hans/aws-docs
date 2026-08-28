---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-bridge-bridgesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Bridge BridgeSource
<a name="aws-properties-mediaconnect-bridge-bridgesource"></a>

 The bridge's source.

## Syntax
<a name="aws-properties-mediaconnect-bridge-bridgesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-bridge-bridgesource-syntax.json"></a>

```
{
  "[FlowSource](#cfn-mediaconnect-bridge-bridgesource-flowsource)" : {{BridgeFlowSource}},
  "[NetworkSource](#cfn-mediaconnect-bridge-bridgesource-networksource)" : {{BridgeNetworkSource}}
}
```

### YAML
<a name="aws-properties-mediaconnect-bridge-bridgesource-syntax.yaml"></a>

```
  [FlowSource](#cfn-mediaconnect-bridge-bridgesource-flowsource): {{
    BridgeFlowSource}}
  [NetworkSource](#cfn-mediaconnect-bridge-bridgesource-networksource): {{
    BridgeNetworkSource}}
```

## Properties
<a name="aws-properties-mediaconnect-bridge-bridgesource-properties"></a>

`FlowSource`  <a name="cfn-mediaconnect-bridge-bridgesource-flowsource"></a>
The source of the bridge. A flow source originates in MediaConnect as an existing cloud flow.
*Required*: No
*Type*: [BridgeFlowSource](aws-properties-mediaconnect-bridge-bridgeflowsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkSource`  <a name="cfn-mediaconnect-bridge-bridgesource-networksource"></a>
The source of the bridge. A network source originates at your premises.
*Required*: No
*Type*: [BridgeNetworkSource](aws-properties-mediaconnect-bridge-bridgenetworksource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
