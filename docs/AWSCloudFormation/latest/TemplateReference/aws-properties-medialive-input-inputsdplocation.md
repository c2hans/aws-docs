---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-inputsdplocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input InputSdpLocation
<a name="aws-properties-medialive-input-inputsdplocation"></a>

The location of the SDP file for one of the SMPTE 2110 streams in a receiver group.

The parent of this entity is Smpte2110ReceiverGroupSdpSettings.

## Syntax
<a name="aws-properties-medialive-input-inputsdplocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-inputsdplocation-syntax.json"></a>

```
{
  "[MediaIndex](#cfn-medialive-input-inputsdplocation-mediaindex)" : {{Integer}},
  "[SdpUrl](#cfn-medialive-input-inputsdplocation-sdpurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-inputsdplocation-syntax.yaml"></a>

```
  [MediaIndex](#cfn-medialive-input-inputsdplocation-mediaindex): {{Integer}}
  [SdpUrl](#cfn-medialive-input-inputsdplocation-sdpurl): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-inputsdplocation-properties"></a>

`MediaIndex`  <a name="cfn-medialive-input-inputsdplocation-mediaindex"></a>
The index of the media stream in the SDP file for one SMPTE 2110 stream.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SdpUrl`  <a name="cfn-medialive-input-inputsdplocation-sdpurl"></a>
The URL of the SDP file for one SMPTE 2110 stream.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
