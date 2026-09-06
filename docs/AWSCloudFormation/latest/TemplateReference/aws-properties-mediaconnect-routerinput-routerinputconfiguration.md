---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-routerinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput RouterInputConfiguration
<a name="aws-properties-mediaconnect-routerinput-routerinputconfiguration"></a>

The configuration settings for a router input.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-routerinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-routerinputconfiguration-syntax.json"></a>

```
{
  "[Failover](#cfn-mediaconnect-routerinput-routerinputconfiguration-failover)" : {{FailoverRouterInputConfiguration}},
  "[MediaConnectFlow](#cfn-mediaconnect-routerinput-routerinputconfiguration-mediaconnectflow)" : {{MediaConnectFlowRouterInputConfiguration}},
  "[MediaLiveChannel](#cfn-mediaconnect-routerinput-routerinputconfiguration-medialivechannel)" : {{MediaLiveChannelRouterInputConfiguration}},
  "[Merge](#cfn-mediaconnect-routerinput-routerinputconfiguration-merge)" : {{MergeRouterInputConfiguration}},
  "[Standard](#cfn-mediaconnect-routerinput-routerinputconfiguration-standard)" : {{StandardRouterInputConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-routerinputconfiguration-syntax.yaml"></a>

```
  [Failover](#cfn-mediaconnect-routerinput-routerinputconfiguration-failover): {{
    FailoverRouterInputConfiguration}}
  [MediaConnectFlow](#cfn-mediaconnect-routerinput-routerinputconfiguration-mediaconnectflow): {{
    MediaConnectFlowRouterInputConfiguration}}
  [MediaLiveChannel](#cfn-mediaconnect-routerinput-routerinputconfiguration-medialivechannel): {{
    MediaLiveChannelRouterInputConfiguration}}
  [Merge](#cfn-mediaconnect-routerinput-routerinputconfiguration-merge): {{
    MergeRouterInputConfiguration}}
  [Standard](#cfn-mediaconnect-routerinput-routerinputconfiguration-standard): {{
    StandardRouterInputConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-routerinputconfiguration-properties"></a>

`Failover`  <a name="cfn-mediaconnect-routerinput-routerinputconfiguration-failover"></a>
Configuration settings for a failover router input that allows switching between two input sources.
*Required*: No
*Type*: [FailoverRouterInputConfiguration](aws-properties-mediaconnect-routerinput-failoverrouterinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaConnectFlow`  <a name="cfn-mediaconnect-routerinput-routerinputconfiguration-mediaconnectflow"></a>
Configuration settings for connecting a router input to a flow output.
*Required*: No
*Type*: [MediaConnectFlowRouterInputConfiguration](aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaLiveChannel`  <a name="cfn-mediaconnect-routerinput-routerinputconfiguration-medialivechannel"></a>
Configuration settings for connecting a router input to a MediaLive channel output.
*Required*: No
*Type*: [MediaLiveChannelRouterInputConfiguration](aws-properties-mediaconnect-routerinput-medialivechannelrouterinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Merge`  <a name="cfn-mediaconnect-routerinput-routerinputconfiguration-merge"></a>
Configuration settings for a merge router input that combines two input sources.
*Required*: No
*Type*: [MergeRouterInputConfiguration](aws-properties-mediaconnect-routerinput-mergerouterinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Standard`  <a name="cfn-mediaconnect-routerinput-routerinputconfiguration-standard"></a>
The configuration settings for a standard router input, including the protocol, protocol-specific configuration, network interface, and availability zone.
*Required*: No
*Type*: [StandardRouterInputConfiguration](aws-properties-mediaconnect-routerinput-standardrouterinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
