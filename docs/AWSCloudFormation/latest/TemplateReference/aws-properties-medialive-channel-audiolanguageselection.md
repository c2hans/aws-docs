---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-audiolanguageselection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AudioLanguageSelection
<a name="aws-properties-medialive-channel-audiolanguageselection"></a>

Information about the audio language to extract.

The parent of this entity is AudioSelectorSettings.

## Syntax
<a name="aws-properties-medialive-channel-audiolanguageselection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-audiolanguageselection-syntax.json"></a>

```
{
  "[LanguageCode](#cfn-medialive-channel-audiolanguageselection-languagecode)" : {{String}},
  "[LanguageSelectionPolicy](#cfn-medialive-channel-audiolanguageselection-languageselectionpolicy)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-audiolanguageselection-syntax.yaml"></a>

```
  [LanguageCode](#cfn-medialive-channel-audiolanguageselection-languagecode): {{String}}
  [LanguageSelectionPolicy](#cfn-medialive-channel-audiolanguageselection-languageselectionpolicy): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-audiolanguageselection-properties"></a>

`LanguageCode`  <a name="cfn-medialive-channel-audiolanguageselection-languagecode"></a>
Selects a specific three-letter language code from within an audio source.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LanguageSelectionPolicy`  <a name="cfn-medialive-channel-audiolanguageselection-languageselectionpolicy"></a>
When set to "strict," the transport stream demux strictly identifies audio streams by their language descriptor. If a PMT update occurs such that an audio stream matching the initially selected language is no longer present, then mute is encoded until the language returns. If set to "loose," then on a PMT update the demux chooses another audio stream in the program with the same stream type if it can't find one with the same language.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
