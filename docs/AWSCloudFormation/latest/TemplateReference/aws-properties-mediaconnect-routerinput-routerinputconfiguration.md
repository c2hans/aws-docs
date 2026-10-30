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
  "[DestinationEndpoint](#cfn-mediaconnect-routerinput-routerinputconfiguration-destinationendpoint)" : {{DestinationEndpointRouterInputConfiguration}},
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
  [DestinationEndpoint](#cfn-mediaconnect-routerinput-routerinputconfiguration-destinationendpoint): {{
    DestinationEndpointRouterInputConfiguration}}
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

`DestinationEndpoint`  <a name="cfn-mediaconnect-routerinput-routerinputconfiguration-destinationendpoint"></a>
Property description not available.
*Required*: No
*Type*: [DestinationEndpointRouterInputConfiguration](aws-properties-mediaconnect-routerinput-destinationendpointrouterinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Failover`  <a name="cfn-mediaconnect-routerinput-routerinputconfiguration-failover"></a>
Configuration settings for a failover router input that allows switching between two input sources.
*Required*: No
*Type*: [FailoverRouterInputConfiguration](aws-properties-mediaconnect-routerinput-failoverrouterinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaConnectFlow`  <a name="cfn-mediaconnect-routerinput-routerinputconfiguration-mediaconnectflow"></a>
Configuration settings for connecting a router input to a flow output.
To connect the router input to the flow output, provide both `flowArn` and `flowOutputArn`. To disconnect it, call the update operation and omit both fields while keeping this configuration object.
You can't change `sourceTransitDecryption` while the router input is connected to a flow output. To change it, first disconnect the router input, then update the decryption.
*Required*: No
*Type*: [MediaConnectFlowRouterInputConfiguration](aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaLiveChannel`  <a name="cfn-mediaconnect-routerinput-routerinputconfiguration-medialivechannel"></a>
Configuration settings for connecting a router input to a MediaLive channel output.
To connect the router input to the MediaLive channel output, provide all three of `mediaLiveChannelArn`, `mediaLivePipelineId`, and `mediaLiveChannelOutputName`. To disconnect it, call the update operation and omit all three fields while keeping this configuration object.
You can't change `sourceTransitDecryption` while the router input is connected to a MediaLive channel output. To change it, first disconnect the router input, then update the decryption.
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
