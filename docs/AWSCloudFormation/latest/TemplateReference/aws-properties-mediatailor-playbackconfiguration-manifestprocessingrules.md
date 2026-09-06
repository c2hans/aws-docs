---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-manifestprocessingrules.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration ManifestProcessingRules
<a name="aws-properties-mediatailor-playbackconfiguration-manifestprocessingrules"></a>

The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-manifestprocessingrules-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-manifestprocessingrules-syntax.json"></a>

```
{
  "[AdMarkerPassthrough](#cfn-mediatailor-playbackconfiguration-manifestprocessingrules-admarkerpassthrough)" : {{AdMarkerPassthrough}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-manifestprocessingrules-syntax.yaml"></a>

```
  [AdMarkerPassthrough](#cfn-mediatailor-playbackconfiguration-manifestprocessingrules-admarkerpassthrough): {{
    AdMarkerPassthrough}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-manifestprocessingrules-properties"></a>

`AdMarkerPassthrough`  <a name="cfn-mediatailor-playbackconfiguration-manifestprocessingrules-admarkerpassthrough"></a>
For HLS, when set to `true`, MediaTailor passes through `EXT-X-CUE-IN`, `EXT-X-CUE-OUT`, and `EXT-X-SPLICEPOINT-SCTE35` ad markers from the origin manifest to the MediaTailor personalized manifest.
No logic is applied to these ad markers. For example, if `EXT-X-CUE-OUT` has a value of `60`, but no ads are filled for that ad break, MediaTailor will not set the value to `0`.
*Required*: No
*Type*: [AdMarkerPassthrough](aws-properties-mediatailor-playbackconfiguration-admarkerpassthrough.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
