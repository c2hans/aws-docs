---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-archivegroupsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel ArchiveGroupSettings
<a name="aws-properties-medialive-channel-archivegroupsettings"></a>

The settings for an archive output group.

The parent of this entity is OutputGroupSettings.

## Syntax
<a name="aws-properties-medialive-channel-archivegroupsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-archivegroupsettings-syntax.json"></a>

```
{
  "[ArchiveCdnSettings](#cfn-medialive-channel-archivegroupsettings-archivecdnsettings)" : {{ArchiveCdnSettings}},
  "[Destination](#cfn-medialive-channel-archivegroupsettings-destination)" : {{OutputLocationRef}},
  "[RolloverInterval](#cfn-medialive-channel-archivegroupsettings-rolloverinterval)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-archivegroupsettings-syntax.yaml"></a>

```
  [ArchiveCdnSettings](#cfn-medialive-channel-archivegroupsettings-archivecdnsettings): {{
    ArchiveCdnSettings}}
  [Destination](#cfn-medialive-channel-archivegroupsettings-destination): {{
    OutputLocationRef}}
  [RolloverInterval](#cfn-medialive-channel-archivegroupsettings-rolloverinterval): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-archivegroupsettings-properties"></a>

`ArchiveCdnSettings`  <a name="cfn-medialive-channel-archivegroupsettings-archivecdnsettings"></a>
Settings to configure the destination of an Archive output.
*Required*: No
*Type*: [ArchiveCdnSettings](aws-properties-medialive-channel-archivecdnsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Destination`  <a name="cfn-medialive-channel-archivegroupsettings-destination"></a>
A directory and base file name where archive files should be written.
*Required*: No
*Type*: [OutputLocationRef](aws-properties-medialive-channel-outputlocationref.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RolloverInterval`  <a name="cfn-medialive-channel-archivegroupsettings-rolloverinterval"></a>
The number of seconds to write to an archive file before closing and starting a new one.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
