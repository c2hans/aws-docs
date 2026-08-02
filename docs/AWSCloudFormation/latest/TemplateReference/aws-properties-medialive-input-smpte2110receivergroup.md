---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-smpte2110receivergroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input Smpte2110ReceiverGroup
<a name="aws-properties-medialive-input-smpte2110receivergroup"></a>

A receiver group is a collection of video, audio, and ancillary streams that you want to group together and attach to one input.

The parent of this entity is Smpte2110ReceiverGroupSettings.

## Syntax
<a name="aws-properties-medialive-input-smpte2110receivergroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-smpte2110receivergroup-syntax.json"></a>

```
{
  "[SdpSettings](#cfn-medialive-input-smpte2110receivergroup-sdpsettings)" : {{Smpte2110ReceiverGroupSdpSettings}}
}
```

### YAML
<a name="aws-properties-medialive-input-smpte2110receivergroup-syntax.yaml"></a>

```
  [SdpSettings](#cfn-medialive-input-smpte2110receivergroup-sdpsettings): {{
    Smpte2110ReceiverGroupSdpSettings}}
```

## Properties
<a name="aws-properties-medialive-input-smpte2110receivergroup-properties"></a>

`SdpSettings`  <a name="cfn-medialive-input-smpte2110receivergroup-sdpsettings"></a>
The single Smpte2110ReceiverGroupSdpSettings that identify the video, audio, and ancillary streams for this receiver group.
*Required*: No
*Type*: [Smpte2110ReceiverGroupSdpSettings](aws-properties-medialive-input-smpte2110receivergroupsdpsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
