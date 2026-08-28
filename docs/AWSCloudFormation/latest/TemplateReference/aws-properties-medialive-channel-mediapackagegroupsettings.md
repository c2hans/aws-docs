---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-mediapackagegroupsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MediaPackageGroupSettings
<a name="aws-properties-medialive-channel-mediapackagegroupsettings"></a>

The settings for the MediaPackage group.

The parent of this entity is OutputGroupSettings.

## Syntax
<a name="aws-properties-medialive-channel-mediapackagegroupsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-mediapackagegroupsettings-syntax.json"></a>

```
{
  "[Destination](#cfn-medialive-channel-mediapackagegroupsettings-destination)" : {{OutputLocationRef}},
  "[MediapackageV2GroupSettings](#cfn-medialive-channel-mediapackagegroupsettings-mediapackagev2groupsettings)" : {{MediaPackageV2GroupSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-mediapackagegroupsettings-syntax.yaml"></a>

```
  [Destination](#cfn-medialive-channel-mediapackagegroupsettings-destination): {{
    OutputLocationRef}}
  [MediapackageV2GroupSettings](#cfn-medialive-channel-mediapackagegroupsettings-mediapackagev2groupsettings): {{
    MediaPackageV2GroupSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-mediapackagegroupsettings-properties"></a>

`Destination`  <a name="cfn-medialive-channel-mediapackagegroupsettings-destination"></a>
The MediaPackage channel destination.
*Required*: No
*Type*: [OutputLocationRef](aws-properties-medialive-channel-outputlocationref.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediapackageV2GroupSettings`  <a name="cfn-medialive-channel-mediapackagegroupsettings-mediapackagev2groupsettings"></a>
Parameters that apply only if the destination parameter (for the output group) specifies a channel group and channel name. Use of these two parameters indicates that the output group is for MediaPackage V2 (CMAF Ingest).
*Required*: No
*Type*: [MediaPackageV2GroupSettings](aws-properties-medialive-channel-mediapackagev2groupsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
