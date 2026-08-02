---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashDvbFontDownload.html
---

# DashDvbFontDownload
<a name="API_DashDvbFontDownload"></a>

For use with DVB-DASH profiles only. The settings for font downloads that you want AWS Elemental MediaPackage to pass through to the manifest.

## Contents
<a name="API_DashDvbFontDownload_Contents"></a>

 ** FontFamily **   <a name="mediapackage-Type-DashDvbFontDownload-FontFamily"></a>
The `fontFamily` name for subtitles, as described in [EBU-TT-D Subtitling Distribution Format](https://tech.ebu.ch/publications/tech3380).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** MimeType **   <a name="mediapackage-Type-DashDvbFontDownload-MimeType"></a>
The `mimeType` of the resource that's at the font download URL.
For information about font MIME types, see the [MPEG-DASH Profile for Transport of ISO BMFF Based DVB Services over IP Based Networks](https://dvb.org/wp-content/uploads/2021/06/A168r4_MPEG-DASH-Profile-for-Transport-of-ISO-BMFF-Based-DVB-Services_Draft-ts_103-285-v140_November_2021.pdf) document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_/-]*[a-zA-Z0-9]`
Required: No

 ** Url **   <a name="mediapackage-Type-DashDvbFontDownload-Url"></a>
The URL for downloading fonts for subtitles.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_DashDvbFontDownload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/DashDvbFontDownload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/DashDvbFontDownload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/DashDvbFontDownload)
