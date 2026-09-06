---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashUtcTiming.html
---

# DashUtcTiming
<a name="API_DashUtcTiming"></a>

Determines the type of UTC timing included in the DASH Media Presentation Description (MPD).

## Contents
<a name="API_DashUtcTiming_Contents"></a>

 ** TimingMode **   <a name="mediapackage-Type-DashUtcTiming-TimingMode"></a>
The UTC timing mode.
Type: String
Valid Values: `HTTP_HEAD | HTTP_ISO | HTTP_XSDATE | UTC_DIRECT`
Required: No

 ** TimingSource **   <a name="mediapackage-Type-DashUtcTiming-TimingSource"></a>
The the method that the player uses to synchronize to coordinated universal time (UTC) wall clock time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_DashUtcTiming_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/DashUtcTiming)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/DashUtcTiming)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/DashUtcTiming)
