---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-medialivechannelrouterinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput MediaLiveChannelRouterInputConfiguration

Configuration settings for connecting a router input to a MediaLive channel output.

To connect the router input to the MediaLive channel output, specify all three of `MediaLiveChannelArn`, `MediaLivePipelineId`, and `MediaLiveChannelOutputName`. To disconnect it, update the stack without these properties and keep the `MediaLiveChannel` configuration.

**Note**
The `EncryptionKeyType` of `SourceTransitDecryption` must match the `EncryptionType` of the MediaLive channel output. If you change `SourceTransitDecryption` while the router input is connected, CloudFormation temporarily disconnects the router input before it applies the update.
To change the key type, first update the stack to disconnect the router input. Then give the channel output (`AWS::MediaLive::Channel`) a new `OutputName`, and set the new `EncryptionType` in its `MediaConnectRouterOutputDestinationSettings`. Finally, update the router input with the new `SourceTransitDecryption` and all three properties, using the new output name. This reconnects it in the same update.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-syntax.json"></a>

```json
{
  "[MediaLiveChannelArn](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivechannelarn)" : {{String}},
  "[MediaLiveChannelOutputName](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivechanneloutputname)" : {{String}},
  "[MediaLivePipelineId](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivepipelineid)" : {{String}},
  "[SourceTransitDecryption](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-sourcetransitdecryption)" : {{MediaLiveTransitEncryption}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-syntax.yaml"></a>

```yaml
  [MediaLiveChannelArn](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivechannelarn): {{String}}
  [MediaLiveChannelOutputName](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivechanneloutputname): {{String}}
  [MediaLivePipelineId](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivepipelineid): {{String}}
  [SourceTransitDecryption](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-sourcetransitdecryption): {{
    MediaLiveTransitEncryption}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-properties"></a>

`MediaLiveChannelArn`  <a name="cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivechannelarn"></a>
The ARN of the MediaLive channel to connect to this router input.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):medialive:[a-z0-9-]+:[0-9]{12}:channel:[a-zA-Z0-9]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaLiveChannelOutputName`  <a name="cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivechanneloutputname"></a>
The name of the MediaLive channel output to connect to this router input.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaLivePipelineId`  <a name="cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivepipelineid"></a>
The index of the MediaLive pipeline to connect to this router input.
*Required*: No
*Type*: String
*Allowed values*: `PIPELINE_0 | PIPELINE_1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceTransitDecryption`  <a name="cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-sourcetransitdecryption"></a>
The decryption configuration for the MediaLive channel source when connected to this router input.
*Required*: Yes
*Type*: [MediaLiveTransitEncryption](aws-properties-mediaconnect-routerinput-medialivetransitencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
