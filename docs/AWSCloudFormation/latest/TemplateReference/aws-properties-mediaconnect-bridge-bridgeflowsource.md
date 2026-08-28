---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-bridge-bridgeflowsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Bridge BridgeFlowSource
<a name="aws-properties-mediaconnect-bridge-bridgeflowsource"></a>

 The source of the bridge. A flow source originates in MediaConnect as an existing cloud flow.

## Syntax
<a name="aws-properties-mediaconnect-bridge-bridgeflowsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-bridge-bridgeflowsource-syntax.json"></a>

```
{
  "[FlowArn](#cfn-mediaconnect-bridge-bridgeflowsource-flowarn)" : {{String}},
  "[FlowVpcInterfaceAttachment](#cfn-mediaconnect-bridge-bridgeflowsource-flowvpcinterfaceattachment)" : {{VpcInterfaceAttachment}},
  "[Name](#cfn-mediaconnect-bridge-bridgeflowsource-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-bridge-bridgeflowsource-syntax.yaml"></a>

```
  [FlowArn](#cfn-mediaconnect-bridge-bridgeflowsource-flowarn): {{String}}
  [FlowVpcInterfaceAttachment](#cfn-mediaconnect-bridge-bridgeflowsource-flowvpcinterfaceattachment): {{
    VpcInterfaceAttachment}}
  [Name](#cfn-mediaconnect-bridge-bridgeflowsource-name): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-bridge-bridgeflowsource-properties"></a>

`FlowArn`  <a name="cfn-mediaconnect-bridge-bridgeflowsource-flowarn"></a>
 The ARN of the cloud flow used as a source of this bridge.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlowVpcInterfaceAttachment`  <a name="cfn-mediaconnect-bridge-bridgeflowsource-flowvpcinterfaceattachment"></a>
 The name of the VPC interface attachment to use for this source.
*Required*: No
*Type*: [VpcInterfaceAttachment](aws-properties-mediaconnect-bridge-vpcinterfaceattachment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-mediaconnect-bridge-bridgeflowsource-name"></a>
 The name of the flow source.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
