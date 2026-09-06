---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-medialive-channel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel
<a name="aws-resource-medialive-channel"></a>

The AWS::MediaLive::Channel resource is a MediaLive resource type that creates a channel.

A MediaLive channel ingests and transcodes (decodes and encodes) source content from the inputs that are attached to that channel, and packages the new content into outputs.

## Syntax
<a name="aws-resource-medialive-channel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-medialive-channel-syntax.json"></a>

```
{
  "Type" : "AWS::MediaLive::Channel",
  "Properties" : {
      "[AnywhereSettings](#cfn-medialive-channel-anywheresettings)" : {{AnywhereSettings}},
      "[CdiInputSpecification](#cfn-medialive-channel-cdiinputspecification)" : {{CdiInputSpecification}},
      "[ChannelClass](#cfn-medialive-channel-channelclass)" : {{String}},
      "[ChannelEngineVersion](#cfn-medialive-channel-channelengineversion)" : {{ChannelEngineVersionRequest}},
      "[ChannelSecurityGroups](#cfn-medialive-channel-channelsecuritygroups)" : {{[ String, ... ]}},
      "[Destinations](#cfn-medialive-channel-destinations)" : {{[ OutputDestination, ... ]}},
      "[DryRun](#cfn-medialive-channel-dryrun)" : {{Boolean}},
      "[EncoderSettings](#cfn-medialive-channel-encodersettings)" : {{EncoderSettings}},
      "[InferenceSettings](#cfn-medialive-channel-inferencesettings)" : {{InferenceSettings}},
      "[InputAttachments](#cfn-medialive-channel-inputattachments)" : {{[ InputAttachment, ... ]}},
      "[InputSpecification](#cfn-medialive-channel-inputspecification)" : {{InputSpecification}},
      "[LinkedChannelSettings](#cfn-medialive-channel-linkedchannelsettings)" : {{LinkedChannelSettings}},
      "[LogLevel](#cfn-medialive-channel-loglevel)" : {{String}},
      "[Maintenance](#cfn-medialive-channel-maintenance)" : {{MaintenanceCreateSettings}},
      "[Name](#cfn-medialive-channel-name)" : {{String}},
      "[RoleArn](#cfn-medialive-channel-rolearn)" : {{String}},
      "[Tags](#cfn-medialive-channel-tags)" : {{[ [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html), ... ]}},
      "[Vpc](#cfn-medialive-channel-vpc)" : {{VpcOutputSettings}}
    }
}
```

### YAML
<a name="aws-resource-medialive-channel-syntax.yaml"></a>

```
Type: AWS::MediaLive::Channel
Properties:
  [AnywhereSettings](#cfn-medialive-channel-anywheresettings): {{
    AnywhereSettings}}
  [CdiInputSpecification](#cfn-medialive-channel-cdiinputspecification): {{
    CdiInputSpecification}}
  [ChannelClass](#cfn-medialive-channel-channelclass): {{String}}
  [ChannelEngineVersion](#cfn-medialive-channel-channelengineversion): {{
    ChannelEngineVersionRequest}}
  [ChannelSecurityGroups](#cfn-medialive-channel-channelsecuritygroups): {{
    - String}}
  [Destinations](#cfn-medialive-channel-destinations): {{
    - OutputDestination}}
  [DryRun](#cfn-medialive-channel-dryrun): {{Boolean}}
  [EncoderSettings](#cfn-medialive-channel-encodersettings): {{
    EncoderSettings}}
  [InferenceSettings](#cfn-medialive-channel-inferencesettings): {{
    InferenceSettings}}
  [InputAttachments](#cfn-medialive-channel-inputattachments): {{
    - InputAttachment}}
  [InputSpecification](#cfn-medialive-channel-inputspecification): {{
    InputSpecification}}
  [LinkedChannelSettings](#cfn-medialive-channel-linkedchannelsettings): {{
    LinkedChannelSettings}}
  [LogLevel](#cfn-medialive-channel-loglevel): {{String}}
  [Maintenance](#cfn-medialive-channel-maintenance): {{
    MaintenanceCreateSettings}}
  [Name](#cfn-medialive-channel-name): {{String}}
  [RoleArn](#cfn-medialive-channel-rolearn): {{String}}
  [Tags](#cfn-medialive-channel-tags): {{
    - [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)}}
  [Vpc](#cfn-medialive-channel-vpc): {{
    VpcOutputSettings}}
```

## Properties
<a name="aws-resource-medialive-channel-properties"></a>

`AnywhereSettings`  <a name="cfn-medialive-channel-anywheresettings"></a>
The Elemental Anywhere settings for this channel.
*Required*: No
*Type*: [AnywhereSettings](aws-properties-medialive-channel-anywheresettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CdiInputSpecification`  <a name="cfn-medialive-channel-cdiinputspecification"></a>
Specification of CDI inputs for this channel.
*Required*: No
*Type*: [CdiInputSpecification](aws-properties-medialive-channel-cdiinputspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChannelClass`  <a name="cfn-medialive-channel-channelclass"></a>
The class for this channel. For a channel with two pipelines, the class is STANDARD. For a channel with one pipeline, the class is SINGLE\_PIPELINE.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChannelEngineVersion`  <a name="cfn-medialive-channel-channelengineversion"></a>
The desired engine version for this channel.
*Required*: No
*Type*: [ChannelEngineVersionRequest](aws-properties-medialive-channel-channelengineversionrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChannelSecurityGroups`  <a name="cfn-medialive-channel-channelsecuritygroups"></a>
A list of IDs for all the Input Security Groups attached to the channel.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Destinations`  <a name="cfn-medialive-channel-destinations"></a>
The settings that identify the destination for the outputs in this MediaLive output package.
*Required*: No
*Type*: Array of [OutputDestination](aws-properties-medialive-channel-outputdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DryRun`  <a name="cfn-medialive-channel-dryrun"></a>
Validates the channel configuration without creating the channel.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncoderSettings`  <a name="cfn-medialive-channel-encodersettings"></a>
The encoding configuration for the output content.
*Required*: No
*Type*: [EncoderSettings](aws-properties-medialive-channel-encodersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InferenceSettings`  <a name="cfn-medialive-channel-inferencesettings"></a>
Include this setting to include Elemental Inference features in this channel.
*Required*: No
*Type*: [InferenceSettings](aws-properties-medialive-channel-inferencesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputAttachments`  <a name="cfn-medialive-channel-inputattachments"></a>
The list of input attachments for the channel.
*Required*: No
*Type*: Array of [InputAttachment](aws-properties-medialive-channel-inputattachment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputSpecification`  <a name="cfn-medialive-channel-inputspecification"></a>
The input specification for this channel. It specifies the key characteristics of the inputs for this channel: the maximum bitrate, the resolution, and the codec.
*Required*: No
*Type*: [InputSpecification](aws-properties-medialive-channel-inputspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinkedChannelSettings`  <a name="cfn-medialive-channel-linkedchannelsettings"></a>
The linked channel settings for the channel.
*Required*: No
*Type*: [LinkedChannelSettings](aws-properties-medialive-channel-linkedchannelsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogLevel`  <a name="cfn-medialive-channel-loglevel"></a>
The verbosity for logging activity for this channel. Charges for logging (which are generated through Amazon CloudWatch Logging) are higher for higher verbosities.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Maintenance`  <a name="cfn-medialive-channel-maintenance"></a>
Maintenance settings for this channel.
*Required*: No
*Type*: [MaintenanceCreateSettings](aws-properties-medialive-channel-maintenancecreatesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-medialive-channel-name"></a>
Name of channel.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-medialive-channel-rolearn"></a>
The IAM role for MediaLive to assume when running this channel. The role is identified by its ARN.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-medialive-channel-tags"></a>
A collection of tags for this channel. Each tag is a key-value pair.
*Required*: No
*Type*: Array of [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Vpc`  <a name="cfn-medialive-channel-vpc"></a>
Settings to enable VPC mode in the channel, so that the endpoints for all outputs are in your VPC.
*Required*: No
*Type*: [VpcOutputSettings](aws-properties-medialive-channel-vpcoutputsettings.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-medialive-channel-return-values"></a>

### Ref
<a name="aws-resource-medialive-channel-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the channel.

For example: `{ "Ref": "myChannel" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-medialive-channel-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-medialive-channel-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the MediaLive channel. For example: arn:aws:medialive:us-west-1:111122223333:channel:1234567

`Id`  <a name="Id-fn::getatt"></a>
User-specified id. This is used in an output group or an output.

`Inputs`  <a name="Inputs-fn::getatt"></a>
The inputs that are attached to this channel. The inputs are identified by their IDs (not by their names or their ARNs).
