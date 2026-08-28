---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flowsource-gatewaybridgesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::FlowSource GatewayBridgeSource
<a name="aws-properties-mediaconnect-flowsource-gatewaybridgesource"></a>

 The source configuration for cloud flows receiving a stream from a bridge.

## Syntax
<a name="aws-properties-mediaconnect-flowsource-gatewaybridgesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flowsource-gatewaybridgesource-syntax.json"></a>

```
{
  "[BridgeArn](#cfn-mediaconnect-flowsource-gatewaybridgesource-bridgearn)" : {{String}},
  "[VpcInterfaceAttachment](#cfn-mediaconnect-flowsource-gatewaybridgesource-vpcinterfaceattachment)" : {{VpcInterfaceAttachment}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flowsource-gatewaybridgesource-syntax.yaml"></a>

```
  [BridgeArn](#cfn-mediaconnect-flowsource-gatewaybridgesource-bridgearn): {{String}}
  [VpcInterfaceAttachment](#cfn-mediaconnect-flowsource-gatewaybridgesource-vpcinterfaceattachment): {{
    VpcInterfaceAttachment}}
```

## Properties
<a name="aws-properties-mediaconnect-flowsource-gatewaybridgesource-properties"></a>

`BridgeArn`  <a name="cfn-mediaconnect-flowsource-gatewaybridgesource-bridgearn"></a>
 The ARN of the bridge feeding this flow.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:bridge:[a-zA-Z0-9-]+:[a-zA-Z0-9_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcInterfaceAttachment`  <a name="cfn-mediaconnect-flowsource-gatewaybridgesource-vpcinterfaceattachment"></a>
 The name of the VPC interface attachment to use for this bridge source.
*Required*: No
*Type*: [VpcInterfaceAttachment](aws-properties-mediaconnect-flowsource-vpcinterfaceattachment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
