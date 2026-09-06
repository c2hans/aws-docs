---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-hlsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration HlsConfiguration
<a name="aws-properties-mediatailor-playbackconfiguration-hlsconfiguration"></a>

The configuration for HLS content.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-hlsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-hlsconfiguration-syntax.json"></a>

```
{
  "[ManifestEndpointPrefix](#cfn-mediatailor-playbackconfiguration-hlsconfiguration-manifestendpointprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-hlsconfiguration-syntax.yaml"></a>

```
  [ManifestEndpointPrefix](#cfn-mediatailor-playbackconfiguration-hlsconfiguration-manifestendpointprefix): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-hlsconfiguration-properties"></a>

`ManifestEndpointPrefix`  <a name="cfn-mediatailor-playbackconfiguration-hlsconfiguration-manifestendpointprefix"></a>
The URL that is used to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
