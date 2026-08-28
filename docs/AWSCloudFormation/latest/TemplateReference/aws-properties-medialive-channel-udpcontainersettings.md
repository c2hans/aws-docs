---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-udpcontainersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel UdpContainerSettings
<a name="aws-properties-medialive-channel-udpcontainersettings"></a>

The configuration of a UDP output.

The parent of this entity is UdpOutputSettings.

## Syntax
<a name="aws-properties-medialive-channel-udpcontainersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-udpcontainersettings-syntax.json"></a>

```
{
  "[M2tsSettings](#cfn-medialive-channel-udpcontainersettings-m2tssettings)" : {{M2tsSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-udpcontainersettings-syntax.yaml"></a>

```
  [M2tsSettings](#cfn-medialive-channel-udpcontainersettings-m2tssettings): {{
    M2tsSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-udpcontainersettings-properties"></a>

`M2tsSettings`  <a name="cfn-medialive-channel-udpcontainersettings-m2tssettings"></a>
The M2TS configuration for this UDP output.
*Required*: No
*Type*: [M2tsSettings](aws-properties-medialive-channel-m2tssettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
