---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-multiplexcontainersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MultiplexContainerSettings
<a name="aws-properties-medialive-channel-multiplexcontainersettings"></a>

Multiplex container settings.

The parent of this entity is MultiplexOutputSettings.

## Syntax
<a name="aws-properties-medialive-channel-multiplexcontainersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-multiplexcontainersettings-syntax.json"></a>

```
{
  "[MultiplexM2tsSettings](#cfn-medialive-channel-multiplexcontainersettings-multiplexm2tssettings)" : {{MultiplexM2tsSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-multiplexcontainersettings-syntax.yaml"></a>

```
  [MultiplexM2tsSettings](#cfn-medialive-channel-multiplexcontainersettings-multiplexm2tssettings): {{
    MultiplexM2tsSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-multiplexcontainersettings-properties"></a>

`MultiplexM2tsSettings`  <a name="cfn-medialive-channel-multiplexcontainersettings-multiplexm2tssettings"></a>
Multiplex M2TS settings for the container.
*Required*: No
*Type*: [MultiplexM2tsSettings](aws-properties-medialive-channel-multiplexm2tssettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
