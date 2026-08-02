---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-inputattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel InputAttachment
<a name="aws-properties-medialive-channel-inputattachment"></a>

An input to attach to this channel.

This entity is at the top level in the channel.

## Syntax
<a name="aws-properties-medialive-channel-inputattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-inputattachment-syntax.json"></a>

```
{
  "[AutomaticInputFailoverSettings](#cfn-medialive-channel-inputattachment-automaticinputfailoversettings)" : {{AutomaticInputFailoverSettings}},
  "[InputAttachmentName](#cfn-medialive-channel-inputattachment-inputattachmentname)" : {{String}},
  "[InputId](#cfn-medialive-channel-inputattachment-inputid)" : {{String}},
  "[InputSettings](#cfn-medialive-channel-inputattachment-inputsettings)" : {{InputSettings}},
  "[LogicalInterfaceNames](#cfn-medialive-channel-inputattachment-logicalinterfacenames)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-medialive-channel-inputattachment-syntax.yaml"></a>

```
  [AutomaticInputFailoverSettings](#cfn-medialive-channel-inputattachment-automaticinputfailoversettings): {{
    AutomaticInputFailoverSettings}}
  [InputAttachmentName](#cfn-medialive-channel-inputattachment-inputattachmentname): {{String}}
  [InputId](#cfn-medialive-channel-inputattachment-inputid): {{String}}
  [InputSettings](#cfn-medialive-channel-inputattachment-inputsettings): {{
    InputSettings}}
  [LogicalInterfaceNames](#cfn-medialive-channel-inputattachment-logicalinterfacenames): {{
    - String}}
```

## Properties
<a name="aws-properties-medialive-channel-inputattachment-properties"></a>

`AutomaticInputFailoverSettings`  <a name="cfn-medialive-channel-inputattachment-automaticinputfailoversettings"></a>
Settings to implement automatic input failover in this input.
*Required*: No
*Type*: [AutomaticInputFailoverSettings](aws-properties-medialive-channel-automaticinputfailoversettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputAttachmentName`  <a name="cfn-medialive-channel-inputattachment-inputattachmentname"></a>
A name for the attachment. This is required if you want to use this input in an input switch action.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputId`  <a name="cfn-medialive-channel-inputattachment-inputid"></a>
The ID of the input to attach.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputSettings`  <a name="cfn-medialive-channel-inputattachment-inputsettings"></a>
Information about the content to extract from the input and about the general handling of the content.
*Required*: No
*Type*: [InputSettings](aws-properties-medialive-channel-inputsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogicalInterfaceNames`  <a name="cfn-medialive-channel-inputattachment-logicalinterfacenames"></a>
Optional assignment of an input to a logical interface on the Node. Only applies to on premises channels.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
