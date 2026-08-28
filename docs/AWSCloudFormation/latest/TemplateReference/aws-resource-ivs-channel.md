---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ivs-channel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::Channel
<a name="aws-resource-ivs-channel"></a>

The `AWS::IVS::Channel` resource specifies an Amazon IVS channel. A channel stores configuration information related to your live stream. For more information, see [CreateChannel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateChannel.html) in the *Amazon IVS Low-Latency Streaming API Reference*.

**Note**
 By default, the IVS API CreateChannel endpoint creates a stream key in addition to a channel. The Amazon IVS Channel resource *does not* create a stream key; to create a stream key, use the StreamKey resource instead.

## Syntax
<a name="aws-resource-ivs-channel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ivs-channel-syntax.json"></a>

```
{
  "Type" : "AWS::IVS::Channel",
  "Properties" : {
      "[Authorized](#cfn-ivs-channel-authorized)" : {{Boolean}},
      "[ContainerFormat](#cfn-ivs-channel-containerformat)" : {{String}},
      "[InsecureIngest](#cfn-ivs-channel-insecureingest)" : {{Boolean}},
      "[LatencyMode](#cfn-ivs-channel-latencymode)" : {{String}},
      "[MultitrackInputConfiguration](#cfn-ivs-channel-multitrackinputconfiguration)" : {{MultitrackInputConfiguration}},
      "[Name](#cfn-ivs-channel-name)" : {{String}},
      "[Preset](#cfn-ivs-channel-preset)" : {{String}},
      "[RecordingConfigurationArn](#cfn-ivs-channel-recordingconfigurationarn)" : {{String}},
      "[Tags](#cfn-ivs-channel-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-ivs-channel-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ivs-channel-syntax.yaml"></a>

```
Type: AWS::IVS::Channel
Properties:
  [Authorized](#cfn-ivs-channel-authorized): {{Boolean}}
  [ContainerFormat](#cfn-ivs-channel-containerformat): {{String}}
  [InsecureIngest](#cfn-ivs-channel-insecureingest): {{Boolean}}
  [LatencyMode](#cfn-ivs-channel-latencymode): {{String}}
  [MultitrackInputConfiguration](#cfn-ivs-channel-multitrackinputconfiguration): {{
    MultitrackInputConfiguration}}
  [Name](#cfn-ivs-channel-name): {{String}}
  [Preset](#cfn-ivs-channel-preset): {{String}}
  [RecordingConfigurationArn](#cfn-ivs-channel-recordingconfigurationarn): {{String}}
  [Tags](#cfn-ivs-channel-tags): {{
    - Tag}}
  [Type](#cfn-ivs-channel-type): {{String}}
```

## Properties
<a name="aws-resource-ivs-channel-properties"></a>

`Authorized`  <a name="cfn-ivs-channel-authorized"></a>
Whether the channel is authorized.
*Default*: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerFormat`  <a name="cfn-ivs-channel-containerformat"></a>
Indicates which content-packaging format is used (MPEG-TS or fMP4). If `multitrackInputConfiguration` is specified and `enabled` is `true`, then `containerFormat` is required and must be set to `FRAGMENTED_MP4`. Otherwise, `containerFormat` may be set to `TS` or `FRAGMENTED_MP4`. Default: `TS`.
*Required*: No
*Type*: String
*Allowed values*: `TS | FRAGMENTED_MP4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InsecureIngest`  <a name="cfn-ivs-channel-insecureingest"></a>
Whether the channel allows insecure RTMP ingest.
*Default*: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LatencyMode`  <a name="cfn-ivs-channel-latencymode"></a>
Channel latency mode. Valid values:
+ `NORMAL`: Use NORMAL to broadcast and deliver live video up to Full HD.
+ `LOW`: Use LOW for near real-time interactions with viewers.
In the Amazon IVS console, `LOW` and `NORMAL` correspond to `Ultra-low` and `Standard`, respectively.
*Default*: `LOW`
*Required*: No
*Type*: String
*Allowed values*: `NORMAL | LOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultitrackInputConfiguration`  <a name="cfn-ivs-channel-multitrackinputconfiguration"></a>
Object specifying multitrack input configuration. Default: no multitrack input configuration is specified.
*Required*: No
*Type*: [MultitrackInputConfiguration](aws-properties-ivs-channel-multitrackinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ivs-channel-name"></a>
Channel name.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]*$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Preset`  <a name="cfn-ivs-channel-preset"></a>
An optional transcode preset for the channel. This is selectable only for `ADVANCED_HD` and `ADVANCED_SD` channel types. For those channel types, the default preset is `HIGHER_BANDWIDTH_DELIVERY`. For other channel types (`BASIC` and `STANDARD`), `preset` is the empty string ("").
*Required*: No
*Type*: String
*Allowed values*: ` | HIGHER_BANDWIDTH_DELIVERY | CONSTRAINED_BANDWIDTH_DELIVERY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordingConfigurationArn`  <a name="cfn-ivs-channel-recordingconfigurationarn"></a>
The ARN of a RecordingConfiguration resource. An empty string indicates that recording is disabled for the channel. A RecordingConfiguration ARN indicates that recording is enabled using the specified recording configuration. See the [ RecordingConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html) resource for more information and an example.
*Default*: "" (empty string, recording is disabled)
*Required*: No
*Type*: String
*Pattern*: `^$|arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ivs-channel-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-channel-tag.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-ivs-channel-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-ivs-channel-type"></a>
The channel type, which determines the allowable resolution and bitrate. *If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.* For details, see [Channel Types](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/channel-types.html).
*Default*: `STANDARD`
*Required*: No
*Type*: String
*Allowed values*: `STANDARD | BASIC | ADVANCED_SD | ADVANCED_HD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ivs-channel-return-values"></a>

### Ref
<a name="aws-resource-ivs-channel-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the channel ARN. For example:

 `{ "Ref": "myChannel" }`

For the Amazon IVS channel `myChannel`, `Ref` returns the channel ARN.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ivs-channel-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ivs-channel-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The channel ARN. For example: `arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`

`IngestEndpoint`  <a name="IngestEndpoint-fn::getatt"></a>
Channel ingest endpoint, part of the definition of an ingest server, used when you set up streaming software.
For example: `a1b2c3d4e5f6.global-contribute.live-video.net`

`PlaybackUrl`  <a name="PlaybackUrl-fn::getatt"></a>
Channel playback URL. For example: `https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8`

## Examples
<a name="aws-resource-ivs-channel--examples"></a>

### Channel and Stream Key Template Examples
<a name="aws-resource-ivs-channel--examples--Channel_and_Stream_Key_Template_Examples"></a>

The following examples specify an Amazon IVS channel and stream key.

#### JSON
<a name="aws-resource-ivs-channel--examples--Channel_and_Stream_Key_Template_Examples--json"></a>

```
{
     "AWSTemplateFormatVersion": "2010-09-09",
     "Resources": {
         "Channel": {
             "Type": "AWS::IVS::Channel",
             "Properties": {
                 "Name": "MyChannel",
                 "Tags": [
                     {
                         "Key": "MyKey",
                         "Value": "MyValue"
                     }
                 ],
                 "InsecureIngest": true
             }
         },
         "StreamKey": {
             "Type": "AWS::IVS::StreamKey",
             "Properties": {
                 "ChannelArn": {"Ref": "Channel"},
                 "Tags": [
                     {
                         "Key": "MyKey",
                         "Value": "MyValue"
                     }
                 ]
             }
         }
     },
     "Outputs": {
         "ChannelArn": {
             "Value": {"Ref": "Channel"}
         },
         "ChannelIngestEndpoint": {
             "Value": {
                 "Fn::GetAtt": [
                     "Channel",
                     "IngestEndpoint"
                 ]
             }
         },
         "ChannelPlaybackUrl": {
             "Value": {
                 "Fn::GetAtt": [
                     "Channel",
                     "PlaybackUrl"
                 ]
             }
         },
         "StreamKeyArn": {
             "Value": {"Ref": "StreamKey"}
         }
     }
 }
```

#### YAML
<a name="aws-resource-ivs-channel--examples--Channel_and_Stream_Key_Template_Examples--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  Channel:
    Type: AWS::IVS::Channel
    Properties:
      Name: MyChannel
      Tags:
        - Key: MyKey
          Value: MyValue
      InsecureIngest: true
  StreamKey:
    Type: AWS::IVS::StreamKey
    Properties:
      ChannelArn: !Ref Channel
      Tags:
        - Key: MyKey
          Value: MyValue
Outputs:
  ChannelArn:
    Value: !Ref Channel
  ChannelIngestEndpoint:
    Value: !GetAtt Channel.IngestEndpoint
  ChannelPlaybackUrl:
    Value: !GetAtt Channel.PlaybackUrl
  StreamKeyArn:
    Value: !Ref StreamKey
```

## See also
<a name="aws-resource-ivs-channel--seealso"></a>
+  [Getting Started with IVS Low-Latency Streaming](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started.html)
+ [Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_Channel.html) data type
+ [CreateChannel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateChannel.html) API endpoint

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
