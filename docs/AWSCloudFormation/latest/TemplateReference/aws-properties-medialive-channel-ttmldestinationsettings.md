---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-ttmldestinationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel TtmlDestinationSettings
<a name="aws-properties-medialive-channel-ttmldestinationsettings"></a>

The setup of TTML captions in the output.

The parent of this entity is CaptionDestinationSettings.

## Syntax
<a name="aws-properties-medialive-channel-ttmldestinationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-ttmldestinationsettings-syntax.json"></a>

```
{
  "[StyleControl](#cfn-medialive-channel-ttmldestinationsettings-stylecontrol)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-ttmldestinationsettings-syntax.yaml"></a>

```
  [StyleControl](#cfn-medialive-channel-ttmldestinationsettings-stylecontrol): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-ttmldestinationsettings-properties"></a>

`StyleControl`  <a name="cfn-medialive-channel-ttmldestinationsettings-stylecontrol"></a>
When set to passthrough, passes through style and position information from a TTML-like input source (TTML, SMPTE-TT, CFF-TT) to the CFF-TT output or TTML output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
