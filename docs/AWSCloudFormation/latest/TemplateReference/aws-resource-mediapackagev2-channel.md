---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediapackagev2-channel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::Channel
<a name="aws-resource-mediapackagev2-channel"></a>

Creates a channel to receive content.

After it's created, a channel provides static input URLs. These URLs remain the same throughout the lifetime of the channel, regardless of any failures or upgrades that might occur. Use these URLs to configure the outputs of your upstream encoder.

## Syntax
<a name="aws-resource-mediapackagev2-channel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediapackagev2-channel-syntax.json"></a>

```
{
  "Type" : "AWS::MediaPackageV2::Channel",
  "Properties" : {
      "[ChannelGroupName](#cfn-mediapackagev2-channel-channelgroupname)" : {{String}},
      "[ChannelName](#cfn-mediapackagev2-channel-channelname)" : {{String}},
      "[Description](#cfn-mediapackagev2-channel-description)" : {{String}},
      "[InputSwitchConfiguration](#cfn-mediapackagev2-channel-inputswitchconfiguration)" : {{InputSwitchConfiguration}},
      "[InputType](#cfn-mediapackagev2-channel-inputtype)" : {{String}},
      "[OutputHeaderConfiguration](#cfn-mediapackagev2-channel-outputheaderconfiguration)" : {{OutputHeaderConfiguration}},
      "[OutputLockingMode](#cfn-mediapackagev2-channel-outputlockingmode)" : {{String}},
      "[Tags](#cfn-mediapackagev2-channel-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-mediapackagev2-channel-syntax.yaml"></a>

```
Type: AWS::MediaPackageV2::Channel
Properties:
  [ChannelGroupName](#cfn-mediapackagev2-channel-channelgroupname): {{String}}
  [ChannelName](#cfn-mediapackagev2-channel-channelname): {{String}}
  [Description](#cfn-mediapackagev2-channel-description): {{String}}
  [InputSwitchConfiguration](#cfn-mediapackagev2-channel-inputswitchconfiguration): {{
    InputSwitchConfiguration}}
  [InputType](#cfn-mediapackagev2-channel-inputtype): {{String}}
  [OutputHeaderConfiguration](#cfn-mediapackagev2-channel-outputheaderconfiguration): {{
    OutputHeaderConfiguration}}
  [OutputLockingMode](#cfn-mediapackagev2-channel-outputlockingmode): {{String}}
  [Tags](#cfn-mediapackagev2-channel-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-mediapackagev2-channel-properties"></a>

`ChannelGroupName`  <a name="cfn-mediapackagev2-channel-channelgroupname"></a>
The name of the channel group associated with the channel configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ChannelName`  <a name="cfn-mediapackagev2-channel-channelname"></a>
The name of the channel.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-mediapackagev2-channel-description"></a>
The description of the channel.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputSwitchConfiguration`  <a name="cfn-mediapackagev2-channel-inputswitchconfiguration"></a>
The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive.
*Required*: No
*Type*: [InputSwitchConfiguration](aws-properties-mediapackagev2-channel-inputswitchconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputType`  <a name="cfn-mediapackagev2-channel-inputtype"></a>
The input type will be an immutable field which will be used to define whether the channel will allow CMAF ingest or HLS ingest. If unprovided, it will default to HLS to preserve current behavior.
The allowed values are:
+ `HLS` - The HLS streaming specification (which defines M3U8 manifests and TS segments).
+ `CMAF` - The DASH-IF CMAF Ingest specification (which defines CMAF segments with optional DASH manifests).
*Required*: No
*Type*: String
*Allowed values*: `HLS | CMAF`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputHeaderConfiguration`  <a name="cfn-mediapackagev2-channel-outputheaderconfiguration"></a>
The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN.
*Required*: No
*Type*: [OutputHeaderConfiguration](aws-properties-mediapackagev2-channel-outputheaderconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputLockingMode`  <a name="cfn-mediapackagev2-channel-outputlockingmode"></a>
The output locking mode configured for the channel.
The allowed values are:
+ `EPOCH_LOCKED` - The channel uses epoch-locked behavior with deterministic sequence numbering and fixed segment boundaries aligned to epoch time.
+ `NON_EPOCH_LOCKED` - The channel uses non-epoch-locked behavior with duration-based segment combining and monotonically increasing sequence numbers starting from 0.
*Required*: No
*Type*: String
*Allowed values*: `EPOCH_LOCKED | NON_EPOCH_LOCKED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-mediapackagev2-channel-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-mediapackagev2-channel-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediapackagev2-channel-return-values"></a>

### Ref
<a name="aws-resource-mediapackagev2-channel-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns`arn:aws:mediapackagev2:region:AccountId:ChannelGroup/ChannelGroupName/Channel/ChannelName`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-mediapackagev2-channel-return-values-fn--getatt"></a>

The attributes of the channels. You can only use the `GetAtt` function for `readOnly` properties. For example, you can use the `GetAtt` function to retrieve the read-only `CreatedAt` property.

####
<a name="aws-resource-mediapackagev2-channel-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the channel.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of the creation of the channel.

`IngestEndpoints`  <a name="IngestEndpoints-fn::getatt"></a>
The ingest endpoints associated with the channel.

`IngestEndpointUrls`  <a name="IngestEndpointUrls-fn::getatt"></a>
The ingest domain URL where the source stream should be sent.

`ModifiedAt`  <a name="ModifiedAt-fn::getatt"></a>
The timestamp of the modification of the channel.
