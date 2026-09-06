---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-audionormalizationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AudioNormalizationSettings
<a name="aws-properties-medialive-channel-audionormalizationsettings"></a>

The settings for normalizing video.

The parent of this entity is AudioDescription.

## Syntax
<a name="aws-properties-medialive-channel-audionormalizationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-audionormalizationsettings-syntax.json"></a>

```
{
  "[Algorithm](#cfn-medialive-channel-audionormalizationsettings-algorithm)" : {{String}},
  "[AlgorithmControl](#cfn-medialive-channel-audionormalizationsettings-algorithmcontrol)" : {{String}},
  "[PeakCalculation](#cfn-medialive-channel-audionormalizationsettings-peakcalculation)" : {{String}},
  "[PeakLimiterThreshold](#cfn-medialive-channel-audionormalizationsettings-peaklimiterthreshold)" : {{Number}},
  "[TargetLkfs](#cfn-medialive-channel-audionormalizationsettings-targetlkfs)" : {{Number}}
}
```

### YAML
<a name="aws-properties-medialive-channel-audionormalizationsettings-syntax.yaml"></a>

```
  [Algorithm](#cfn-medialive-channel-audionormalizationsettings-algorithm): {{String}}
  [AlgorithmControl](#cfn-medialive-channel-audionormalizationsettings-algorithmcontrol): {{String}}
  [PeakCalculation](#cfn-medialive-channel-audionormalizationsettings-peakcalculation): {{String}}
  [PeakLimiterThreshold](#cfn-medialive-channel-audionormalizationsettings-peaklimiterthreshold): {{Number}}
  [TargetLkfs](#cfn-medialive-channel-audionormalizationsettings-targetlkfs): {{Number}}
```

## Properties
<a name="aws-properties-medialive-channel-audionormalizationsettings-properties"></a>

`Algorithm`  <a name="cfn-medialive-channel-audionormalizationsettings-algorithm"></a>
The audio normalization algorithm to use. itu17701 conforms to the CALM Act specification. itu17702 conforms to the EBU R-128 specification.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AlgorithmControl`  <a name="cfn-medialive-channel-audionormalizationsettings-algorithmcontrol"></a>
When set to correctAudio, the output audio is corrected using the chosen algorithm. If set to measureOnly, the audio is measured but not adjusted.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PeakCalculation`  <a name="cfn-medialive-channel-audionormalizationsettings-peakcalculation"></a>
Specifies whether to calculate true peak loudness for each output audio track. When set to TRUE\_PEAK, the service calculates true peak values for every output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PeakLimiterThreshold`  <a name="cfn-medialive-channel-audionormalizationsettings-peaklimiterthreshold"></a>
The peak limiter threshold, in decibels relative to true peak (dBTP), when TRUE\_PEAK peak calculation is enabled. When TRUE\_PEAK is not enabled, the threshold applies as decibels relative to full scale (dBFS).
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetLkfs`  <a name="cfn-medialive-channel-audionormalizationsettings-targetlkfs"></a>
The Target LKFS(loudness) to adjust volume to. If no value is entered, a default value is used according to the chosen algorithm. The CALM Act (1770-1) recommends a target of -24 LKFS. The EBU R-128 specification (1770-2) recommends a target of -23 LKFS.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
