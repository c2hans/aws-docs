---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-sourcemonitoringconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow SourceMonitoringConfig
<a name="aws-properties-mediaconnect-flow-sourcemonitoringconfig"></a>

The `SourceMonitoringConfig` property type specifies the source monitoring settings for an `AWS::MediaConnect::Flow`.

## Syntax
<a name="aws-properties-mediaconnect-flow-sourcemonitoringconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-sourcemonitoringconfig-syntax.json"></a>

```
{
  "[AudioMonitoringSettings](#cfn-mediaconnect-flow-sourcemonitoringconfig-audiomonitoringsettings)" : {{[ AudioMonitoringSetting, ... ]}},
  "[ContentQualityAnalysisState](#cfn-mediaconnect-flow-sourcemonitoringconfig-contentqualityanalysisstate)" : {{String}},
  "[ThumbnailState](#cfn-mediaconnect-flow-sourcemonitoringconfig-thumbnailstate)" : {{String}},
  "[VideoMonitoringSettings](#cfn-mediaconnect-flow-sourcemonitoringconfig-videomonitoringsettings)" : {{[ VideoMonitoringSetting, ... ]}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-sourcemonitoringconfig-syntax.yaml"></a>

```
  [AudioMonitoringSettings](#cfn-mediaconnect-flow-sourcemonitoringconfig-audiomonitoringsettings): {{
    - AudioMonitoringSetting}}
  [ContentQualityAnalysisState](#cfn-mediaconnect-flow-sourcemonitoringconfig-contentqualityanalysisstate): {{String}}
  [ThumbnailState](#cfn-mediaconnect-flow-sourcemonitoringconfig-thumbnailstate): {{String}}
  [VideoMonitoringSettings](#cfn-mediaconnect-flow-sourcemonitoringconfig-videomonitoringsettings): {{
    - VideoMonitoringSetting}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-sourcemonitoringconfig-properties"></a>

`AudioMonitoringSettings`  <a name="cfn-mediaconnect-flow-sourcemonitoringconfig-audiomonitoringsettings"></a>
Contains the settings for audio stream metrics monitoring.
*Required*: No
*Type*: Array of [AudioMonitoringSetting](aws-properties-mediaconnect-flow-audiomonitoringsetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContentQualityAnalysisState`  <a name="cfn-mediaconnect-flow-sourcemonitoringconfig-contentqualityanalysisstate"></a>
Indicates whether content quality analysis is enabled or disabled.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThumbnailState`  <a name="cfn-mediaconnect-flow-sourcemonitoringconfig-thumbnailstate"></a>
The current state of the thumbnail monitoring.
+ If you don't explicitly specify a value when creating a flow, no thumbnail state will be set.
+ If you update an existing flow and remove a previously set thumbnail state, the value will change to `DISABLED`.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VideoMonitoringSettings`  <a name="cfn-mediaconnect-flow-sourcemonitoringconfig-videomonitoringsettings"></a>
Contains the settings for video stream metrics monitoring.
*Required*: No
*Type*: Array of [VideoMonitoringSetting](aws-properties-mediaconnect-flow-videomonitoringsetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
