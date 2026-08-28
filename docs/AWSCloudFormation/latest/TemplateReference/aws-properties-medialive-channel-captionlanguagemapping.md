---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-captionlanguagemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel CaptionLanguageMapping
<a name="aws-properties-medialive-channel-captionlanguagemapping"></a>

Maps a captions channel to an ISO 693-2 language code (http://www.loc.gov/standards/iso639-2), with an optional description.

The parent of this entity is HlsGroupSettings.

## Syntax
<a name="aws-properties-medialive-channel-captionlanguagemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-captionlanguagemapping-syntax.json"></a>

```
{
  "[CaptionChannel](#cfn-medialive-channel-captionlanguagemapping-captionchannel)" : {{Integer}},
  "[LanguageCode](#cfn-medialive-channel-captionlanguagemapping-languagecode)" : {{String}},
  "[LanguageDescription](#cfn-medialive-channel-captionlanguagemapping-languagedescription)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-captionlanguagemapping-syntax.yaml"></a>

```
  [CaptionChannel](#cfn-medialive-channel-captionlanguagemapping-captionchannel): {{Integer}}
  [LanguageCode](#cfn-medialive-channel-captionlanguagemapping-languagecode): {{String}}
  [LanguageDescription](#cfn-medialive-channel-captionlanguagemapping-languagedescription): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-captionlanguagemapping-properties"></a>

`CaptionChannel`  <a name="cfn-medialive-channel-captionlanguagemapping-captionchannel"></a>
The closed caption channel being described by this CaptionLanguageMapping. Each channel mapping must have a unique channel number (maximum of 4).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LanguageCode`  <a name="cfn-medialive-channel-captionlanguagemapping-languagecode"></a>
A three-character ISO 639-2 language code (see http://www.loc.gov/standards/iso639-2).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LanguageDescription`  <a name="cfn-medialive-channel-captionlanguagemapping-languagedescription"></a>
The textual description of language.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
