---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-captiondescription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel CaptionDescription
<a name="aws-properties-medialive-channel-captiondescription"></a>

The encoding information for output captions.

The parent of this entity is EncoderSettings.

## Syntax
<a name="aws-properties-medialive-channel-captiondescription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-captiondescription-syntax.json"></a>

```
{
  "[Accessibility](#cfn-medialive-channel-captiondescription-accessibility)" : {{String}},
  "[CaptionDashRoles](#cfn-medialive-channel-captiondescription-captiondashroles)" : {{[ String, ... ]}},
  "[CaptionSelectorName](#cfn-medialive-channel-captiondescription-captionselectorname)" : {{String}},
  "[DestinationSettings](#cfn-medialive-channel-captiondescription-destinationsettings)" : {{CaptionDestinationSettings}},
  "[DvbDashAccessibility](#cfn-medialive-channel-captiondescription-dvbdashaccessibility)" : {{String}},
  "[LanguageCode](#cfn-medialive-channel-captiondescription-languagecode)" : {{String}},
  "[LanguageDescription](#cfn-medialive-channel-captiondescription-languagedescription)" : {{String}},
  "[Name](#cfn-medialive-channel-captiondescription-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-captiondescription-syntax.yaml"></a>

```
  [Accessibility](#cfn-medialive-channel-captiondescription-accessibility): {{String}}
  [CaptionDashRoles](#cfn-medialive-channel-captiondescription-captiondashroles): {{
    - String}}
  [CaptionSelectorName](#cfn-medialive-channel-captiondescription-captionselectorname): {{String}}
  [DestinationSettings](#cfn-medialive-channel-captiondescription-destinationsettings): {{
    CaptionDestinationSettings}}
  [DvbDashAccessibility](#cfn-medialive-channel-captiondescription-dvbdashaccessibility): {{String}}
  [LanguageCode](#cfn-medialive-channel-captiondescription-languagecode): {{String}}
  [LanguageDescription](#cfn-medialive-channel-captiondescription-languagedescription): {{String}}
  [Name](#cfn-medialive-channel-captiondescription-name): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-captiondescription-properties"></a>

`Accessibility`  <a name="cfn-medialive-channel-captiondescription-accessibility"></a>
Indicates whether the caption track implements accessibility features such as written descriptions of spoken dialog, music, and sounds. This signaling is added to HLS output group and MediaPackage output group.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CaptionDashRoles`  <a name="cfn-medialive-channel-captiondescription-captiondashroles"></a>
Identifies the DASH roles to assign to this captions output. Applies only when the captions output is configured for DVB DASH accessibility signaling.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CaptionSelectorName`  <a name="cfn-medialive-channel-captiondescription-captionselectorname"></a>
Specifies which input captions selector to use as a captions source when generating output captions. This field should match a captionSelector name.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationSettings`  <a name="cfn-medialive-channel-captiondescription-destinationsettings"></a>
Additional settings for a captions destination that depend on the destination type.
*Required*: No
*Type*: [CaptionDestinationSettings](aws-properties-medialive-channel-captiondestinationsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DvbDashAccessibility`  <a name="cfn-medialive-channel-captiondescription-dvbdashaccessibility"></a>
Identifies DVB DASH accessibility signaling in this captions output. Used in Microsoft Smooth Streaming outputs to signal accessibility information to packagers.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LanguageCode`  <a name="cfn-medialive-channel-captiondescription-languagecode"></a>
An ISO 639-2 three-digit code. For more information, see http://www.loc.gov/standards/iso639-2/.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LanguageDescription`  <a name="cfn-medialive-channel-captiondescription-languagedescription"></a>
Human-readable information to indicate the captions that are available for players (for example, English or Spanish).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-medialive-channel-captiondescription-name"></a>
The name of the captions description. The name is used to associate a captions description with an output. Names must be unique within a channel.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
