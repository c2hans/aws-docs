---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-routeroutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput RouterOutputConfiguration
<a name="aws-properties-mediaconnect-routeroutput-routeroutputconfiguration"></a>

The configuration settings for a router output.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-routeroutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-routeroutputconfiguration-syntax.json"></a>

```
{
  "[MediaConnectFlow](#cfn-mediaconnect-routeroutput-routeroutputconfiguration-mediaconnectflow)" : {{MediaConnectFlowRouterOutputConfiguration}},
  "[MediaLiveInput](#cfn-mediaconnect-routeroutput-routeroutputconfiguration-medialiveinput)" : {{MediaLiveInputRouterOutputConfiguration}},
  "[SourceEndpoint](#cfn-mediaconnect-routeroutput-routeroutputconfiguration-sourceendpoint)" : {{SourceEndpointRouterOutputConfiguration}},
  "[Standard](#cfn-mediaconnect-routeroutput-routeroutputconfiguration-standard)" : {{StandardRouterOutputConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-routeroutputconfiguration-syntax.yaml"></a>

```
  [MediaConnectFlow](#cfn-mediaconnect-routeroutput-routeroutputconfiguration-mediaconnectflow): {{
    MediaConnectFlowRouterOutputConfiguration}}
  [MediaLiveInput](#cfn-mediaconnect-routeroutput-routeroutputconfiguration-medialiveinput): {{
    MediaLiveInputRouterOutputConfiguration}}
  [SourceEndpoint](#cfn-mediaconnect-routeroutput-routeroutputconfiguration-sourceendpoint): {{
    SourceEndpointRouterOutputConfiguration}}
  [Standard](#cfn-mediaconnect-routeroutput-routeroutputconfiguration-standard): {{
    StandardRouterOutputConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-routeroutputconfiguration-properties"></a>

`MediaConnectFlow`  <a name="cfn-mediaconnect-routeroutput-routeroutputconfiguration-mediaconnectflow"></a>
Configuration settings for connecting a router output to a MediaConnect flow source.
To connect the router output to the flow source, provide both `flowArn` and `flowSourceArn`. To disconnect it, call the update operation and omit both fields while keeping this configuration object.
You can't change `destinationTransitEncryption` while the router output is connected to a flow source. To change it, first disconnect the router output, then update the encryption.
*Required*: No
*Type*: [MediaConnectFlowRouterOutputConfiguration](aws-properties-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaLiveInput`  <a name="cfn-mediaconnect-routeroutput-routeroutputconfiguration-medialiveinput"></a>
Configuration settings for connecting a router output to a MediaLive input.
To connect the router output to the MediaLive input, provide both `mediaLiveInputArn` and `mediaLivePipelineId`. To disconnect it, call the update operation and omit both fields while keeping this configuration object.
You can't change `destinationTransitEncryption` while the router output is connected to a MediaLive input. To change it, first disconnect the router output, then update the encryption.
*Required*: No
*Type*: [MediaLiveInputRouterOutputConfiguration](aws-properties-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceEndpoint`  <a name="cfn-mediaconnect-routeroutput-routeroutputconfiguration-sourceendpoint"></a>
Property description not available.
*Required*: No
*Type*: [SourceEndpointRouterOutputConfiguration](aws-properties-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Standard`  <a name="cfn-mediaconnect-routeroutput-routeroutputconfiguration-standard"></a>
The configuration settings for a standard router output, including the protocol, protocol-specific configuration, network interface, and availability zone.
*Required*: No
*Type*: [StandardRouterOutputConfiguration](aws-properties-mediaconnect-routeroutput-standardrouteroutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
