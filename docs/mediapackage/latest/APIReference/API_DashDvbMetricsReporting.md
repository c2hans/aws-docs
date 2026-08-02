---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashDvbMetricsReporting.html
---

# DashDvbMetricsReporting
<a name="API_DashDvbMetricsReporting"></a>

For use with DVB-DASH profiles only. The settings for error reporting from the playback device that you want AWS Elemental MediaPackage to pass through to the manifest.

## Contents
<a name="API_DashDvbMetricsReporting_Contents"></a>

 ** ReportingUrl **   <a name="mediapackage-Type-DashDvbMetricsReporting-ReportingUrl"></a>
The URL where playback devices send error reports.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** Probability **   <a name="mediapackage-Type-DashDvbMetricsReporting-Probability"></a>
The number of playback devices per 1000 that will send error reports to the reporting URL. This represents the probability that a playback device will be a reporting player for this session.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

## See Also
<a name="API_DashDvbMetricsReporting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/DashDvbMetricsReporting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/DashDvbMetricsReporting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/DashDvbMetricsReporting)
