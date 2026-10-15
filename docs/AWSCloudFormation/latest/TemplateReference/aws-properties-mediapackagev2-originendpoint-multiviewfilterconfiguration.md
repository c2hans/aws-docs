---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-multiviewfilterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint MultiviewFilterConfiguration
<a name="aws-properties-mediapackagev2-originendpoint-multiviewfilterconfiguration"></a>

The multiview combination for a pinned manifest. MediaPackage serves the manifest with this layout and these sources, so players request it without an `aws.multiview` query parameter.

If a request for a pinned manifest also includes an `aws.multiview` query parameter, MediaPackage rejects the request, even when that parameter requests the same combination.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-multiviewfilterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-multiviewfilterconfiguration-syntax.json"></a>

```
{
  "[Layout](#cfn-mediapackagev2-originendpoint-multiviewfilterconfiguration-layout)" : {{String}},
  "[Sources](#cfn-mediapackagev2-originendpoint-multiviewfilterconfiguration-sources)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-multiviewfilterconfiguration-syntax.yaml"></a>

```
  [Layout](#cfn-mediapackagev2-originendpoint-multiviewfilterconfiguration-layout): {{String}}
  [Sources](#cfn-mediapackagev2-originendpoint-multiviewfilterconfiguration-sources): {{
    - String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-multiviewfilterconfiguration-properties"></a>

`Layout`  <a name="cfn-mediapackagev2-originendpoint-multiviewfilterconfiguration-layout"></a>
The layout that MediaPackage uses to composite the tiles into a single output. This layout must be one of the `AvailableLayouts` of the channel that this origin endpoint is on.
*Required*: Yes
*Type*: String
*Allowed values*: `LAYOUT_2EH | LAYOUT_2PL | LAYOUT_3EL | LAYOUT_3PL | LAYOUT_4E | LAYOUT_4PL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sources`  <a name="cfn-mediapackagev2-originendpoint-multiviewfilterconfiguration-sources"></a>
The source channels to composite, in tile order. Each channel must be one of the `AvailableSources` of the channel that this origin endpoint is on, and the number of channels must equal the number of tiles in `Layout`.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `256 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
