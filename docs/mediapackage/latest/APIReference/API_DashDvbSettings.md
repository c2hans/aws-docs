---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashDvbSettings.html
---

# DashDvbSettings
<a name="API_DashDvbSettings"></a>

For endpoints that use the DVB-DASH profile only. The font download and error reporting information that you want MediaPackage to pass through to the manifest.

## Contents
<a name="API_DashDvbSettings_Contents"></a>

 ** ErrorMetrics **   <a name="mediapackage-Type-DashDvbSettings-ErrorMetrics"></a>
Playback device error reporting settings.
Type: Array of [DashDvbMetricsReporting](API_DashDvbMetricsReporting.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** FontDownload **   <a name="mediapackage-Type-DashDvbSettings-FontDownload"></a>
Subtitle font settings.
Type: [DashDvbFontDownload](API_DashDvbFontDownload.md) object
Required: No

## See Also
<a name="API_DashDvbSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/DashDvbSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/DashDvbSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/DashDvbSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
