---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-clientsidebeaconingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration ClientSideBeaconingConfiguration
<a name="aws-properties-mediatailor-playbackconfiguration-clientsidebeaconingconfiguration"></a>

<a name="aws-properties-mediatailor-playbackconfiguration-clientsidebeaconingconfiguration-description"></a>The `ClientSideBeaconingConfiguration` property type specifies Property description not available. for an [AWS::MediaTailor::PlaybackConfiguration](aws-resource-mediatailor-playbackconfiguration.md).

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-clientsidebeaconingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-clientsidebeaconingconfiguration-syntax.json"></a>

```
{
  "[AdditionalEventTypes](#cfn-mediatailor-playbackconfiguration-clientsidebeaconingconfiguration-additionaleventtypes)" : {{[ String, ... ]}},
  "[ReportingMode](#cfn-mediatailor-playbackconfiguration-clientsidebeaconingconfiguration-reportingmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-clientsidebeaconingconfiguration-syntax.yaml"></a>

```
  [AdditionalEventTypes](#cfn-mediatailor-playbackconfiguration-clientsidebeaconingconfiguration-additionaleventtypes): {{
    - String}}
  [ReportingMode](#cfn-mediatailor-playbackconfiguration-clientsidebeaconingconfiguration-reportingmode): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-clientsidebeaconingconfiguration-properties"></a>

`AdditionalEventTypes`  <a name="cfn-mediatailor-playbackconfiguration-clientsidebeaconingconfiguration-additionaleventtypes"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Allowed values*: `MUTE | UNMUTE | PAUSE | SKIP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReportingMode`  <a name="cfn-mediatailor-playbackconfiguration-clientsidebeaconingconfiguration-reportingmode"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `DISABLED | INSIGHTS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
