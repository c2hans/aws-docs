---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint HlsManifestConfiguration
<a name="aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration"></a>

The HLS manifest configuration associated with the origin endpoint.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration-syntax.json"></a>

```
{
  "[ChildManifestName](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-childmanifestname)" : {{String}},
  "[FilterConfiguration](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-filterconfiguration)" : {{FilterConfiguration}},
  "[ManifestName](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-manifestname)" : {{String}},
  "[ManifestWindowSeconds](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-manifestwindowseconds)" : {{Integer}},
  "[ProgramDateTimeIntervalSeconds](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-programdatetimeintervalseconds)" : {{Integer}},
  "[ScteHls](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-sctehls)" : {{ScteHls}},
  "[StartTag](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-starttag)" : {{StartTag}},
  "[UriPathType](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-uripathtype)" : {{String}},
  "[Url](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-url)" : {{String}},
  "[UrlEncodeChildManifest](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-urlencodechildmanifest)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration-syntax.yaml"></a>

```
  [ChildManifestName](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-childmanifestname): {{String}}
  [FilterConfiguration](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-filterconfiguration): {{
    FilterConfiguration}}
  [ManifestName](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-manifestname): {{String}}
  [ManifestWindowSeconds](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-manifestwindowseconds): {{Integer}}
  [ProgramDateTimeIntervalSeconds](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-programdatetimeintervalseconds): {{Integer}}
  [ScteHls](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-sctehls): {{
    ScteHls}}
  [StartTag](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-starttag): {{
    StartTag}}
  [UriPathType](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-uripathtype): {{String}}
  [Url](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-url): {{String}}
  [UrlEncodeChildManifest](#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-urlencodechildmanifest): {{Boolean}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration-properties"></a>

`ChildManifestName`  <a name="cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-childmanifestname"></a>
The name of the child manifest associated with the HLS manifest configuration.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterConfiguration`  <a name="cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-filterconfiguration"></a>
Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.
*Required*: No
*Type*: [FilterConfiguration](aws-properties-mediapackagev2-originendpoint-filterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestName`  <a name="cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-manifestname"></a>
The name of the manifest associated with the HLS manifest configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestWindowSeconds`  <a name="cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-manifestwindowseconds"></a>
The duration of the manifest window, in seconds, for the HLS manifest configuration.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProgramDateTimeIntervalSeconds`  <a name="cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-programdatetimeintervalseconds"></a>
The `EXT-X-PROGRAM-DATE-TIME` interval, in seconds, associated with the HLS manifest configuration.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScteHls`  <a name="cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-sctehls"></a>
THE SCTE-35 HLS configuration associated with the HLS manifest configuration.
*Required*: No
*Type*: [ScteHls](aws-properties-mediapackagev2-originendpoint-sctehls.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTag`  <a name="cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-starttag"></a>
To insert an EXT-X-START tag in your HLS playlist, specify a StartTag configuration object with a valid TimeOffset. When you do, you can also optionally specify whether to include a PRECISE value in the EXT-X-START tag.
*Required*: No
*Type*: [StartTag](aws-properties-mediapackagev2-originendpoint-starttag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UriPathType`  <a name="cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-uripathtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `LEAF | ROOT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-url"></a>
The URL of the HLS manifest configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UrlEncodeChildManifest`  <a name="cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-urlencodechildmanifest"></a>
When enabled, MediaPackage URL-encodes the query string for API requests for HLS child manifests to comply with AWS Signature Version 4 (SigV4) signature signing protocol. For more information, see [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in *AWS Identity and Access Management User Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
