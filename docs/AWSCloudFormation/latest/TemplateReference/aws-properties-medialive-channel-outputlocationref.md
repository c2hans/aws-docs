---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-outputlocationref.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel OutputLocationRef
<a name="aws-properties-medialive-channel-outputlocationref"></a>

A reference to an OutputDestination ID that is defined in the channel.

This entity is used by ArchiveGroupSettings, FrameCaptureGroupSettings, HlsGroupSettings, MediaPackageGroupSettings, MSSmoothGroupSettings, RtmpOutputSettings, and UdpOutputSettings.

## Syntax
<a name="aws-properties-medialive-channel-outputlocationref-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-outputlocationref-syntax.json"></a>

```
{
  "[DestinationRefId](#cfn-medialive-channel-outputlocationref-destinationrefid)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-outputlocationref-syntax.yaml"></a>

```
  [DestinationRefId](#cfn-medialive-channel-outputlocationref-destinationrefid): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-outputlocationref-properties"></a>

`DestinationRefId`  <a name="cfn-medialive-channel-outputlocationref-destinationrefid"></a>
A reference ID for this destination.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
