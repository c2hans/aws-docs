---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-cmafingestcaptionlanguagemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel CmafIngestCaptionLanguageMapping
<a name="aws-properties-medialive-channel-cmafingestcaptionlanguagemapping"></a>

Add an array item for each language. Follow the order of the caption descriptions.

## Syntax
<a name="aws-properties-medialive-channel-cmafingestcaptionlanguagemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-cmafingestcaptionlanguagemapping-syntax.json"></a>

```
{
  "[CaptionChannel](#cfn-medialive-channel-cmafingestcaptionlanguagemapping-captionchannel)" : {{Integer}},
  "[LanguageCode](#cfn-medialive-channel-cmafingestcaptionlanguagemapping-languagecode)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-cmafingestcaptionlanguagemapping-syntax.yaml"></a>

```
  [CaptionChannel](#cfn-medialive-channel-cmafingestcaptionlanguagemapping-captionchannel): {{Integer}}
  [LanguageCode](#cfn-medialive-channel-cmafingestcaptionlanguagemapping-languagecode): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-cmafingestcaptionlanguagemapping-properties"></a>

`CaptionChannel`  <a name="cfn-medialive-channel-cmafingestcaptionlanguagemapping-captionchannel"></a>
A number for the channel for this caption, 1 to 4.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LanguageCode`  <a name="cfn-medialive-channel-cmafingestcaptionlanguagemapping-languagecode"></a>
Language code for the language of the caption in this channel. For example, ger/deu.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
