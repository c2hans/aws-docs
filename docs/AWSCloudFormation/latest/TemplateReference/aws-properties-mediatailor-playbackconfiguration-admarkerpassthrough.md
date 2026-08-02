---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-admarkerpassthrough.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration AdMarkerPassthrough
<a name="aws-properties-mediatailor-playbackconfiguration-admarkerpassthrough"></a>

For HLS, when set to `true`, MediaTailor passes through `EXT-X-CUE-IN`, `EXT-X-CUE-OUT`, and `EXT-X-SPLICEPOINT-SCTE35` ad markers from the origin manifest to the MediaTailor personalized manifest.

No logic is applied to these ad markers. For example, if `EXT-X-CUE-OUT` has a value of `60`, but no ads are filled for that ad break, MediaTailor will not set the value to `0`.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-admarkerpassthrough-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-admarkerpassthrough-syntax.json"></a>

```
{
  "[Enabled](#cfn-mediatailor-playbackconfiguration-admarkerpassthrough-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-admarkerpassthrough-syntax.yaml"></a>

```
  [Enabled](#cfn-mediatailor-playbackconfiguration-admarkerpassthrough-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-admarkerpassthrough-properties"></a>

`Enabled`  <a name="cfn-mediatailor-playbackconfiguration-admarkerpassthrough-enabled"></a>
Enables ad marker passthrough for your configuration.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
