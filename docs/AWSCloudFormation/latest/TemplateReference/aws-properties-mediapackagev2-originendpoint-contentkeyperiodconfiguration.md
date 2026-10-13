---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-contentkeyperiodconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint ContentKeyPeriodConfiguration
<a name="aws-properties-mediapackagev2-originendpoint-contentkeyperiodconfiguration"></a>

The configuration that controls the content key period timing information that MediaPackage signals to your DRM key provider.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-contentkeyperiodconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-contentkeyperiodconfiguration-syntax.json"></a>

```
{
  "[ContentKeyPeriodTiming](#cfn-mediapackagev2-originendpoint-contentkeyperiodconfiguration-contentkeyperiodtiming)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-contentkeyperiodconfiguration-syntax.yaml"></a>

```
  [ContentKeyPeriodTiming](#cfn-mediapackagev2-originendpoint-contentkeyperiodconfiguration-contentkeyperiodtiming): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-contentkeyperiodconfiguration-properties"></a>

`ContentKeyPeriodTiming`  <a name="cfn-mediapackagev2-originendpoint-contentkeyperiodconfiguration-contentkeyperiodtiming"></a>
Specifies what timing information MediaPackage signals in the `ContentKeyPeriod` to your DRM key provider. If you don't specify a value, the default is `INDEX_ONLY`. Signaling start and end times (`START_END_ONLY` or `INDEX_WITH_START_END`) also requires key rotation to be enabled.
The allowed values are:
+ `INDEX_ONLY` - Signals only the content key index. This is the default and matches the current behavior. It's supported for both SPEKE Version 2.0 and 2.1.
+ `START_END_ONLY` - Signals only the start and end times the key is used for. Requires `SpekeVersion``V2_1`.
+ `INDEX_WITH_START_END` - Signals both the content key index and the start and end times the key is used for. Requires `SpekeVersion``V2_1`.
*Required*: No
*Type*: String
*Allowed values*: `INDEX_ONLY | START_END_ONLY | INDEX_WITH_START_END`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
