---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-mediapackageoutputsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MediaPackageOutputSettings
<a name="aws-properties-medialive-channel-mediapackageoutputsettings"></a>

The settings for a MediaPackage output.

The parent of this entity is OutputSettings.

## Syntax
<a name="aws-properties-medialive-channel-mediapackageoutputsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-mediapackageoutputsettings-syntax.json"></a>

```
{
  "[MediaPackageV2DestinationSettings](#cfn-medialive-channel-mediapackageoutputsettings-mediapackagev2destinationsettings)" : {{MediaPackageV2DestinationSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-mediapackageoutputsettings-syntax.yaml"></a>

```
  [MediaPackageV2DestinationSettings](#cfn-medialive-channel-mediapackageoutputsettings-mediapackagev2destinationsettings): {{
    MediaPackageV2DestinationSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-mediapackageoutputsettings-properties"></a>

`MediaPackageV2DestinationSettings`  <a name="cfn-medialive-channel-mediapackageoutputsettings-mediapackagev2destinationsettings"></a>
The MediaPackage V2 destination settings for this output.
*Required*: No
*Type*: [MediaPackageV2DestinationSettings](aws-properties-medialive-channel-mediapackagev2destinationsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
