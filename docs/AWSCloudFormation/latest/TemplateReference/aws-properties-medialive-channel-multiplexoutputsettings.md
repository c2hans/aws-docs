---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-multiplexoutputsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MultiplexOutputSettings
<a name="aws-properties-medialive-channel-multiplexoutputsettings"></a>

Configuration of a Multiplex output.

The parent of this entity is OutputSettings.

## Syntax
<a name="aws-properties-medialive-channel-multiplexoutputsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-multiplexoutputsettings-syntax.json"></a>

```
{
  "[ContainerSettings](#cfn-medialive-channel-multiplexoutputsettings-containersettings)" : {{MultiplexContainerSettings}},
  "[Destination](#cfn-medialive-channel-multiplexoutputsettings-destination)" : {{OutputLocationRef}}
}
```

### YAML
<a name="aws-properties-medialive-channel-multiplexoutputsettings-syntax.yaml"></a>

```
  [ContainerSettings](#cfn-medialive-channel-multiplexoutputsettings-containersettings): {{
    MultiplexContainerSettings}}
  [Destination](#cfn-medialive-channel-multiplexoutputsettings-destination): {{
    OutputLocationRef}}
```

## Properties
<a name="aws-properties-medialive-channel-multiplexoutputsettings-properties"></a>

`ContainerSettings`  <a name="cfn-medialive-channel-multiplexoutputsettings-containersettings"></a>
Multiplex container settings.
*Required*: No
*Type*: [MultiplexContainerSettings](aws-properties-medialive-channel-multiplexcontainersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Destination`  <a name="cfn-medialive-channel-multiplexoutputsettings-destination"></a>
Destination is a Multiplex.
*Required*: No
*Type*: [OutputLocationRef](aws-properties-medialive-channel-outputlocationref.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
