---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-configurationbundleaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule ConfigurationBundleAction
<a name="aws-properties-bedrockagentcore-gatewayrule-configurationbundleaction"></a>

An action that applies a configuration bundle override, either as a static override or a weighted split for A/B testing.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-configurationbundleaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-configurationbundleaction-syntax.json"></a>

```
{
  "[StaticOverride](#cfn-bedrockagentcore-gatewayrule-configurationbundleaction-staticoverride)" : {{StaticOverride}},
  "[WeightedOverride](#cfn-bedrockagentcore-gatewayrule-configurationbundleaction-weightedoverride)" : {{WeightedOverride}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-configurationbundleaction-syntax.yaml"></a>

```
  [StaticOverride](#cfn-bedrockagentcore-gatewayrule-configurationbundleaction-staticoverride): {{
    StaticOverride}}
  [WeightedOverride](#cfn-bedrockagentcore-gatewayrule-configurationbundleaction-weightedoverride): {{
    WeightedOverride}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-configurationbundleaction-properties"></a>

`StaticOverride`  <a name="cfn-bedrockagentcore-gatewayrule-configurationbundleaction-staticoverride"></a>
A static configuration bundle override that applies a single bundle version to all matching requests.
*Required*: No
*Type*: [StaticOverride](aws-properties-bedrockagentcore-gatewayrule-staticoverride.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeightedOverride`  <a name="cfn-bedrockagentcore-gatewayrule-configurationbundleaction-weightedoverride"></a>
A weighted configuration bundle override that splits traffic between multiple bundle versions based on configured weights.
*Required*: No
*Type*: [WeightedOverride](aws-properties-bedrockagentcore-gatewayrule-weightedoverride.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
