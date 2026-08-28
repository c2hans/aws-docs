---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-dvbsubsourcesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel DvbSubSourceSettings
<a name="aws-properties-medialive-channel-dvbsubsourcesettings"></a>

Information about the DVB Sub captions to extract from the input.

The parent of this entity is CaptionSelectorSettings.

## Syntax
<a name="aws-properties-medialive-channel-dvbsubsourcesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-dvbsubsourcesettings-syntax.json"></a>

```
{
  "[OcrLanguage](#cfn-medialive-channel-dvbsubsourcesettings-ocrlanguage)" : {{String}},
  "[Pid](#cfn-medialive-channel-dvbsubsourcesettings-pid)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-dvbsubsourcesettings-syntax.yaml"></a>

```
  [OcrLanguage](#cfn-medialive-channel-dvbsubsourcesettings-ocrlanguage): {{String}}
  [Pid](#cfn-medialive-channel-dvbsubsourcesettings-pid): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-dvbsubsourcesettings-properties"></a>

`OcrLanguage`  <a name="cfn-medialive-channel-dvbsubsourcesettings-ocrlanguage"></a>
If you will configure a WebVTT caption description that references this caption selector, use this field to provide the language to consider when translating the image-based source to text.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Pid`  <a name="cfn-medialive-channel-dvbsubsourcesettings-pid"></a>
When using DVB-Sub with burn-in or SMPTE-TT, use this PID for the source content. It is unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
