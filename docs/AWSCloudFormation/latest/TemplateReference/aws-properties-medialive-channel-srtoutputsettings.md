---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-srtoutputsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel SrtOutputSettings
<a name="aws-properties-medialive-channel-srtoutputsettings"></a>

Srt Output Settings

## Syntax
<a name="aws-properties-medialive-channel-srtoutputsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-srtoutputsettings-syntax.json"></a>

```
{
  "[BufferMsec](#cfn-medialive-channel-srtoutputsettings-buffermsec)" : {{Integer}},
  "[ContainerSettings](#cfn-medialive-channel-srtoutputsettings-containersettings)" : {{UdpContainerSettings}},
  "[Destination](#cfn-medialive-channel-srtoutputsettings-destination)" : {{OutputLocationRef}},
  "[EncryptionType](#cfn-medialive-channel-srtoutputsettings-encryptiontype)" : {{String}},
  "[Latency](#cfn-medialive-channel-srtoutputsettings-latency)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-srtoutputsettings-syntax.yaml"></a>

```
  [BufferMsec](#cfn-medialive-channel-srtoutputsettings-buffermsec): {{Integer}}
  [ContainerSettings](#cfn-medialive-channel-srtoutputsettings-containersettings): {{
    UdpContainerSettings}}
  [Destination](#cfn-medialive-channel-srtoutputsettings-destination): {{
    OutputLocationRef}}
  [EncryptionType](#cfn-medialive-channel-srtoutputsettings-encryptiontype): {{String}}
  [Latency](#cfn-medialive-channel-srtoutputsettings-latency): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-srtoutputsettings-properties"></a>

`BufferMsec`  <a name="cfn-medialive-channel-srtoutputsettings-buffermsec"></a>
SRT output buffering in milliseconds. A higher value increases latency through the encoder. But the benefits are that it helps to maintain a constant, low-jitter SRT output, and it accommodates clock recovery, input switching, input disruptions, picture reordering, and so on. Range: 0-10000 milliseconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerSettings`  <a name="cfn-medialive-channel-srtoutputsettings-containersettings"></a>
The container settings for the SRT output.
*Required*: No
*Type*: [UdpContainerSettings](aws-properties-medialive-channel-udpcontainersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Destination`  <a name="cfn-medialive-channel-srtoutputsettings-destination"></a>
Reference to an OutputDestination ID defined in the channel.
*Required*: No
*Type*: [OutputLocationRef](aws-properties-medialive-channel-outputlocationref.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionType`  <a name="cfn-medialive-channel-srtoutputsettings-encryptiontype"></a>
The encryption level for the content. Valid values are AES128, AES192, AES256. You and the downstream system should plan how to set this field because the values must not conflict with each other.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Latency`  <a name="cfn-medialive-channel-srtoutputsettings-latency"></a>
The latency value, in milliseconds, that is proposed during the SRT connection handshake. SRT will choose the maximum of the values proposed by the sender and receiver. Range: 40-16000 milliseconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
