---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-framecapturecdnsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel FrameCaptureCdnSettings
<a name="aws-properties-medialive-channel-framecapturecdnsettings"></a>

Settings to configure the destination of a Frame Capture output.

The parent of this entity is FrameCaptureGroupSettings.

## Syntax
<a name="aws-properties-medialive-channel-framecapturecdnsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-framecapturecdnsettings-syntax.json"></a>

```
{
  "[FrameCaptureS3Settings](#cfn-medialive-channel-framecapturecdnsettings-framecaptures3settings)" : {{ArchiveFrameCaptureHlsS3Settings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-framecapturecdnsettings-syntax.yaml"></a>

```
  [FrameCaptureS3Settings](#cfn-medialive-channel-framecapturecdnsettings-framecaptures3settings): {{
    ArchiveFrameCaptureHlsS3Settings}}
```

## Properties
<a name="aws-properties-medialive-channel-framecapturecdnsettings-properties"></a>

`FrameCaptureS3Settings`  <a name="cfn-medialive-channel-framecapturecdnsettings-framecaptures3settings"></a>
Sets up Amazon S3 as the destination for this Frame Capture output.
*Required*: No
*Type*: [ArchiveFrameCaptureHlsS3Settings](aws-properties-medialive-channel-archiveframecapturehlss3settings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
