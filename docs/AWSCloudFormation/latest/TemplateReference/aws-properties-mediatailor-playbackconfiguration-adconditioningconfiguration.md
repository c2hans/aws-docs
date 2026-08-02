---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-adconditioningconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration AdConditioningConfiguration
<a name="aws-properties-mediatailor-playbackconfiguration-adconditioningconfiguration"></a>

The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-adconditioningconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-adconditioningconfiguration-syntax.json"></a>

```
{
  "[StreamingMediaFileConditioning](#cfn-mediatailor-playbackconfiguration-adconditioningconfiguration-streamingmediafileconditioning)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-adconditioningconfiguration-syntax.yaml"></a>

```
  [StreamingMediaFileConditioning](#cfn-mediatailor-playbackconfiguration-adconditioningconfiguration-streamingmediafileconditioning): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-adconditioningconfiguration-properties"></a>

`StreamingMediaFileConditioning`  <a name="cfn-mediatailor-playbackconfiguration-adconditioningconfiguration-streamingmediafileconditioning"></a>
For ads that have media files with streaming delivery and supported file extensions, indicates what transcoding action MediaTailor takes when it first receives these ads from the ADS. `TRANSCODE` indicates that MediaTailor must transcode the ads. `NONE` indicates that you have already transcoded the ads outside of MediaTailor and don't need them transcoded as part of the ad insertion workflow. For more information about ad conditioning see [Using preconditioned ads](https://docs.aws.amazon.com/mediatailor/latest/ug/precondition-ads.html) in the AWS Elemental MediaTailor user guide.
*Required*: Yes
*Type*: String
*Allowed values*: `TRANSCODE | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
