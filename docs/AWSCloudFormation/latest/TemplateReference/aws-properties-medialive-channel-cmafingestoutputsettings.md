---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-cmafingestoutputsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel CmafIngestOutputSettings
<a name="aws-properties-medialive-channel-cmafingestoutputsettings"></a>

Cmaf Ingest Output Settings

## Syntax
<a name="aws-properties-medialive-channel-cmafingestoutputsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-cmafingestoutputsettings-syntax.json"></a>

```
{
  "[NameModifier](#cfn-medialive-channel-cmafingestoutputsettings-namemodifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-cmafingestoutputsettings-syntax.yaml"></a>

```
  [NameModifier](#cfn-medialive-channel-cmafingestoutputsettings-namemodifier): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-cmafingestoutputsettings-properties"></a>

`NameModifier`  <a name="cfn-medialive-channel-cmafingestoutputsettings-namemodifier"></a>
String concatenated to the end of the destination filename. Required for multiple outputs of the same type.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
