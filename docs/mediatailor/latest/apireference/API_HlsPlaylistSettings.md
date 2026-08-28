---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_HlsPlaylistSettings.html
---

# HlsPlaylistSettings
<a name="API_HlsPlaylistSettings"></a>

HLS playlist configuration parameters.

## Contents
<a name="API_HlsPlaylistSettings_Contents"></a>

 ** AdMarkupType **   <a name="mediatailor-Type-HlsPlaylistSettings-AdMarkupType"></a>
Determines the type of SCTE 35 tags to use in ad markup. Specify `DATERANGE` to use `DATERANGE` tags (for live or VOD content). Specify `SCTE35_ENHANCED` to use `EXT-X-CUE-OUT` and `EXT-X-CUE-IN` tags (for VOD content only).
Type: Array of strings
Valid Values: `DATERANGE | SCTE35_ENHANCED`
Required: No

 ** ManifestWindowSeconds **   <a name="mediatailor-Type-HlsPlaylistSettings-ManifestWindowSeconds"></a>
The total duration (in seconds) of each manifest. Minimum value: `30` seconds. Maximum value: `3600` seconds.
Type: Integer
Required: No

## See Also
<a name="API_HlsPlaylistSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/HlsPlaylistSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/HlsPlaylistSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/HlsPlaylistSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
