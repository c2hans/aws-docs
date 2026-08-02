---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_FilterConfiguration.html
---

# FilterConfiguration
<a name="API_FilterConfiguration"></a>

Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.

## Contents
<a name="API_FilterConfiguration_Contents"></a>

 ** ClipStartTime **   <a name="mediapackage-Type-FilterConfiguration-ClipStartTime"></a>
Optionally specify the clip start time for all of your manifest egress requests. When you include clip start time, note that you cannot use clip start time query parameters for this manifest's endpoint URL.
Type: Timestamp
Required: No

 ** DrmSettings **   <a name="mediapackage-Type-FilterConfiguration-DrmSettings"></a>
Optionally specify one or more DRM settings for all of your manifest egress requests. When you include a DRM setting, note that you cannot use an identical DRM setting query parameter for this manifest's endpoint URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** End **   <a name="mediapackage-Type-FilterConfiguration-End"></a>
Optionally specify the end time for all of your manifest egress requests. When you include end time, note that you cannot use end time query parameters for this manifest's endpoint URL.
Type: Timestamp
Required: No

 ** ManifestFilter **   <a name="mediapackage-Type-FilterConfiguration-ManifestFilter"></a>
Optionally specify one or more manifest filters for all of your manifest egress requests. When you include a manifest filter, note that you cannot use an identical manifest filter query parameter for this manifest's endpoint URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Start **   <a name="mediapackage-Type-FilterConfiguration-Start"></a>
Optionally specify the start time for all of your manifest egress requests. When you include start time, note that you cannot use start time query parameters for this manifest's endpoint URL.
Type: Timestamp
Required: No

 ** TimeDelaySeconds **   <a name="mediapackage-Type-FilterConfiguration-TimeDelaySeconds"></a>
Optionally specify the time delay for all of your manifest egress requests. Enter a value that is smaller than your endpoint's startover window. When you include time delay, note that you cannot use time delay query parameters for this manifest's endpoint URL.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1209600.
Required: No

## See Also
<a name="API_FilterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/FilterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/FilterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/FilterConfiguration)
