---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-program-adbreak.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Program AdBreak
<a name="aws-properties-mediatailor-program-adbreak"></a>

Ad break configuration parameters.

## Syntax
<a name="aws-properties-mediatailor-program-adbreak-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-program-adbreak-syntax.json"></a>

```
{
  "[AdBreakMetadata](#cfn-mediatailor-program-adbreak-adbreakmetadata)" : {{[ KeyValuePair, ... ]}},
  "[MessageType](#cfn-mediatailor-program-adbreak-messagetype)" : {{String}},
  "[OffsetMillis](#cfn-mediatailor-program-adbreak-offsetmillis)" : {{Integer}},
  "[Slate](#cfn-mediatailor-program-adbreak-slate)" : {{SlateSource}},
  "[SpliceInsertMessage](#cfn-mediatailor-program-adbreak-spliceinsertmessage)" : {{SpliceInsertMessage}},
  "[TimeSignalMessage](#cfn-mediatailor-program-adbreak-timesignalmessage)" : {{TimeSignalMessage}}
}
```

### YAML
<a name="aws-properties-mediatailor-program-adbreak-syntax.yaml"></a>

```
  [AdBreakMetadata](#cfn-mediatailor-program-adbreak-adbreakmetadata): {{
    - KeyValuePair}}
  [MessageType](#cfn-mediatailor-program-adbreak-messagetype): {{String}}
  [OffsetMillis](#cfn-mediatailor-program-adbreak-offsetmillis): {{Integer}}
  [Slate](#cfn-mediatailor-program-adbreak-slate): {{
    SlateSource}}
  [SpliceInsertMessage](#cfn-mediatailor-program-adbreak-spliceinsertmessage): {{
    SpliceInsertMessage}}
  [TimeSignalMessage](#cfn-mediatailor-program-adbreak-timesignalmessage): {{
    TimeSignalMessage}}
```

## Properties
<a name="aws-properties-mediatailor-program-adbreak-properties"></a>

`AdBreakMetadata`  <a name="cfn-mediatailor-program-adbreak-adbreakmetadata"></a>
Defines a list of key/value pairs that MediaTailor generates within the `EXT-X-ASSET`tag for `SCTE35_ENHANCED` output.
*Required*: No
*Type*: Array of [KeyValuePair](aws-properties-mediatailor-program-keyvaluepair.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageType`  <a name="cfn-mediatailor-program-adbreak-messagetype"></a>
The SCTE-35 ad insertion type. Accepted value: `SPLICE_INSERT`, `TIME_SIGNAL`.
*Required*: No
*Type*: String
*Allowed values*: `SPLICE_INSERT | TIME_SIGNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OffsetMillis`  <a name="cfn-mediatailor-program-adbreak-offsetmillis"></a>
How long (in milliseconds) after the beginning of the program that an ad starts. This value must fall within 100ms of a segment boundary, otherwise the ad break will be skipped.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Slate`  <a name="cfn-mediatailor-program-adbreak-slate"></a>
Ad break slate configuration.
*Required*: No
*Type*: [SlateSource](aws-properties-mediatailor-program-slatesource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpliceInsertMessage`  <a name="cfn-mediatailor-program-adbreak-spliceinsertmessage"></a>
This defines the SCTE-35 `splice_insert()` message inserted around the ad. For information about using `splice_insert()`, see the SCTE-35 specficiaiton, section 9.7.3.1.
*Required*: No
*Type*: [SpliceInsertMessage](aws-properties-mediatailor-program-spliceinsertmessage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeSignalMessage`  <a name="cfn-mediatailor-program-adbreak-timesignalmessage"></a>
Defines the SCTE-35 `time_signal` message inserted around the ad.
Programs on a channel's schedule can be configured with one or more ad breaks. You can attach a `splice_insert` SCTE-35 message to the ad break. This message provides basic metadata about the ad break.
See section 9.7.4 of the 2022 SCTE-35 specification for more information.
*Required*: No
*Type*: [TimeSignalMessage](aws-properties-mediatailor-program-timesignalmessage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
