---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-dashdvbfontdownload.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint DashDvbFontDownload
<a name="aws-properties-mediapackagev2-originendpoint-dashdvbfontdownload"></a>

For use with DVB-DASH profiles only. The settings for font downloads that you want AWS Elemental MediaPackage to pass through to the manifest.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-dashdvbfontdownload-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-dashdvbfontdownload-syntax.json"></a>

```
{
  "[FontFamily](#cfn-mediapackagev2-originendpoint-dashdvbfontdownload-fontfamily)" : {{String}},
  "[MimeType](#cfn-mediapackagev2-originendpoint-dashdvbfontdownload-mimetype)" : {{String}},
  "[Url](#cfn-mediapackagev2-originendpoint-dashdvbfontdownload-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-dashdvbfontdownload-syntax.yaml"></a>

```
  [FontFamily](#cfn-mediapackagev2-originendpoint-dashdvbfontdownload-fontfamily): {{String}}
  [MimeType](#cfn-mediapackagev2-originendpoint-dashdvbfontdownload-mimetype): {{String}}
  [Url](#cfn-mediapackagev2-originendpoint-dashdvbfontdownload-url): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-dashdvbfontdownload-properties"></a>

`FontFamily`  <a name="cfn-mediapackagev2-originendpoint-dashdvbfontdownload-fontfamily"></a>
The `fontFamily` name for subtitles, as described in [EBU-TT-D Subtitling Distribution Format](https://tech.ebu.ch/publications/tech3380).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MimeType`  <a name="cfn-mediapackagev2-originendpoint-dashdvbfontdownload-mimetype"></a>
The `mimeType` of the resource that's at the font download URL.
For information about font MIME types, see the [MPEG-DASH Profile for Transport of ISO BMFF Based DVB Services over IP Based Networks](https://dvb.org/wp-content/uploads/2021/06/A168r4_MPEG-DASH-Profile-for-Transport-of-ISO-BMFF-Based-DVB-Services_Draft-ts_103-285-v140_November_2021.pdf) document.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_/-]*[a-zA-Z0-9]$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-mediapackagev2-originendpoint-dashdvbfontdownload-url"></a>
The URL for downloading fonts for subtitles.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
