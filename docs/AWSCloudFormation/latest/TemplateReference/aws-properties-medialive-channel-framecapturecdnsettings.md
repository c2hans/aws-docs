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
  "[FrameCaptureS3Settings](#cfn-medialive-channel-framecapturecdnsettings-framecaptures3settings)" : {{FrameCaptureS3Settings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-framecapturecdnsettings-syntax.yaml"></a>

```
  [FrameCaptureS3Settings](#cfn-medialive-channel-framecapturecdnsettings-framecaptures3settings): {{
    FrameCaptureS3Settings}}
```

## Properties
<a name="aws-properties-medialive-channel-framecapturecdnsettings-properties"></a>

`FrameCaptureS3Settings`  <a name="cfn-medialive-channel-framecapturecdnsettings-framecaptures3settings"></a>
Sets up Amazon S3 as the destination for this Frame Capture output.
*Required*: No
*Type*: [FrameCaptureS3Settings](aws-properties-medialive-channel-framecaptures3settings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
