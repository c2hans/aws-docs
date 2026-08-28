---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-archivecdnsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel ArchiveCdnSettings
<a name="aws-properties-medialive-channel-archivecdnsettings"></a>

Settings to configure the destination of an Archive output.

The parent of this entity is ArchiveGroupSettings.

## Syntax
<a name="aws-properties-medialive-channel-archivecdnsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-archivecdnsettings-syntax.json"></a>

```
{
  "[ArchiveS3Settings](#cfn-medialive-channel-archivecdnsettings-archives3settings)" : {{ArchiveS3Settings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-archivecdnsettings-syntax.yaml"></a>

```
  [ArchiveS3Settings](#cfn-medialive-channel-archivecdnsettings-archives3settings): {{
    ArchiveS3Settings}}
```

## Properties
<a name="aws-properties-medialive-channel-archivecdnsettings-properties"></a>

`ArchiveS3Settings`  <a name="cfn-medialive-channel-archivecdnsettings-archives3settings"></a>
Sets up Amazon S3 as the destination for this Archive output.
*Required*: No
*Type*: [ArchiveS3Settings](aws-properties-medialive-channel-archives3settings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
