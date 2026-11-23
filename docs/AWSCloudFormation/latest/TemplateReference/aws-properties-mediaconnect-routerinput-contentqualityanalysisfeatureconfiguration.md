---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-contentqualityanalysisfeatureconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput ContentQualityAnalysisFeatureConfiguration

Configures the content quality analysis features for the router input.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-contentqualityanalysisfeatureconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-contentqualityanalysisfeatureconfiguration-syntax.json"></a>

```json
{
  "[BlackFrames](#cfn-mediaconnect-routerinput-contentqualityanalysisfeatureconfiguration-blackframes)" : {{BlackFramesConfiguration}},
  "[FrozenFrames](#cfn-mediaconnect-routerinput-contentqualityanalysisfeatureconfiguration-frozenframes)" : {{FrozenFramesConfiguration}},
  "[SilentAudio](#cfn-mediaconnect-routerinput-contentqualityanalysisfeatureconfiguration-silentaudio)" : {{SilentAudioConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-contentqualityanalysisfeatureconfiguration-syntax.yaml"></a>

```yaml
  [BlackFrames](#cfn-mediaconnect-routerinput-contentqualityanalysisfeatureconfiguration-blackframes): {{
    BlackFramesConfiguration}}
  [FrozenFrames](#cfn-mediaconnect-routerinput-contentqualityanalysisfeatureconfiguration-frozenframes): {{
    FrozenFramesConfiguration}}
  [SilentAudio](#cfn-mediaconnect-routerinput-contentqualityanalysisfeatureconfiguration-silentaudio): {{
    SilentAudioConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-contentqualityanalysisfeatureconfiguration-properties"></a>

`BlackFrames`  <a name="cfn-mediaconnect-routerinput-contentqualityanalysisfeatureconfiguration-blackframes"></a>
Settings for black frames detection.
*Required*: No
*Type*: [BlackFramesConfiguration](aws-properties-mediaconnect-routerinput-blackframesconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FrozenFrames`  <a name="cfn-mediaconnect-routerinput-contentqualityanalysisfeatureconfiguration-frozenframes"></a>
Settings for frozen frames detection.
*Required*: No
*Type*: [FrozenFramesConfiguration](aws-properties-mediaconnect-routerinput-frozenframesconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SilentAudio`  <a name="cfn-mediaconnect-routerinput-contentqualityanalysisfeatureconfiguration-silentaudio"></a>
Settings for silent audio detection.
*Required*: No
*Type*: [SilentAudioConfiguration](aws-properties-mediaconnect-routerinput-silentaudioconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
