---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-vastresponse.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration VastResponse
<a name="aws-properties-mediatailor-playbackconfiguration-vastresponse"></a>

The settings that control how MediaTailor processes VAST responses from the ad decision server.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-vastresponse-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-vastresponse-syntax.json"></a>

```
{
  "[AdSequencingMode](#cfn-mediatailor-playbackconfiguration-vastresponse-adsequencingmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-vastresponse-syntax.yaml"></a>

```
  [AdSequencingMode](#cfn-mediatailor-playbackconfiguration-vastresponse-adsequencingmode): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-vastresponse-properties"></a>

`AdSequencingMode`  <a name="cfn-mediatailor-playbackconfiguration-vastresponse-adsequencingmode"></a>
The ad sequencing mode that controls how MediaTailor handles sequenced and standalone ads in VAST responses. `FOLLOW_AD_SEQUENCE` inserts sequenced ads in increasing order for both live and VOD workflows, using standalone ads only as replacements when a sequenced ad fails. `FOLLOW_AD_SEQUENCE_ONLY_LIVE` enables ad sequencing for live workflows only. `FOLLOW_AD_SEQUENCE_ONLY_VOD` enables ad sequencing for VOD workflows only. `IGNORE_AD_SEQUENCE` inserts ads in the order they appear in the VAST response, regardless of sequence attributes. The default behavior is `IGNORE_AD_SEQUENCE`.
*Required*: No
*Type*: String
*Allowed values*: `FOLLOW_AD_SEQUENCE | IGNORE_AD_SEQUENCE | FOLLOW_AD_SEQUENCE_ONLY_LIVE | FOLLOW_AD_SEQUENCE_ONLY_VOD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
