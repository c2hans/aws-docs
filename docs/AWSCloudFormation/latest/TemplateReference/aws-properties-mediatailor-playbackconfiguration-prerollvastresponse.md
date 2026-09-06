---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-prerollvastresponse.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration PreRollVastResponse
<a name="aws-properties-mediatailor-playbackconfiguration-prerollvastresponse"></a>

The settings that control how MediaTailor processes VAST responses from the ad decision server for live pre-roll ad breaks.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-prerollvastresponse-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-prerollvastresponse-syntax.json"></a>

```
{
  "[AdSequencingMode](#cfn-mediatailor-playbackconfiguration-prerollvastresponse-adsequencingmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-prerollvastresponse-syntax.yaml"></a>

```
  [AdSequencingMode](#cfn-mediatailor-playbackconfiguration-prerollvastresponse-adsequencingmode): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-prerollvastresponse-properties"></a>

`AdSequencingMode`  <a name="cfn-mediatailor-playbackconfiguration-prerollvastresponse-adsequencingmode"></a>
The ad sequencing mode for live pre-roll ads. `FOLLOW_AD_SEQUENCE` inserts sequenced ads in increasing order and uses standalone ads only as replacements when a sequenced ad fails. `IGNORE_AD_SEQUENCE` inserts ads in the order they appear in the VAST response, regardless of sequence attributes. The default behavior is `IGNORE_AD_SEQUENCE`.
*Required*: No
*Type*: String
*Allowed values*: `FOLLOW_AD_SEQUENCE | IGNORE_AD_SEQUENCE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
