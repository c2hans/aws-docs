---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-sctehls.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint ScteHls
<a name="aws-properties-mediapackagev2-originendpoint-sctehls"></a>

The SCTE-35 HLS configuration associated with the origin endpoint.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-sctehls-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-sctehls-syntax.json"></a>

```
{
  "[AdMarkerHls](#cfn-mediapackagev2-originendpoint-sctehls-admarkerhls)" : {{String}},
  "[ScteInManifests](#cfn-mediapackagev2-originendpoint-sctehls-scteinmanifests)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-sctehls-syntax.yaml"></a>

```
  [AdMarkerHls](#cfn-mediapackagev2-originendpoint-sctehls-admarkerhls): {{String}}
  [ScteInManifests](#cfn-mediapackagev2-originendpoint-sctehls-scteinmanifests): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-sctehls-properties"></a>

`AdMarkerHls`  <a name="cfn-mediapackagev2-originendpoint-sctehls-admarkerhls"></a>
The SCTE-35 HLS ad-marker configuration.
*Required*: No
*Type*: String
*Allowed values*: `DATERANGE | SCTE35_ENHANCED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScteInManifests`  <a name="cfn-mediapackagev2-originendpoint-sctehls-scteinmanifests"></a>
Controls which SCTE-35 events appear in HLS manifests. `ALL` includes all non-implicit SCTE-35 events. `MATCHES_FILTER` includes only events whose type matches the configured `ScteFilter`.
If you don't specify a value, the default is `ALL`.
*Required*: No
*Type*: String
*Allowed values*: `ALL | MATCHES_FILTER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
