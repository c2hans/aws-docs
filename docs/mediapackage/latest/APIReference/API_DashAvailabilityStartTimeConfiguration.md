---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashAvailabilityStartTimeConfiguration.html
---

# DashAvailabilityStartTimeConfiguration
<a name="API_DashAvailabilityStartTimeConfiguration"></a>

The configuration for the DASH `availabilityStartTime` attribute of the Media Presentation Description (MPD). Use this configuration to set a custom availability start time for your DASH manifest.

## Contents
<a name="API_DashAvailabilityStartTimeConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** FixedAvailabilityStartTime **   <a name="mediapackage-Type-DashAvailabilityStartTimeConfiguration-FixedAvailabilityStartTime"></a>
The fixed availability start time for the DASH manifest, in ISO 8601 date-time format. The value must have hourly granularity, meaning that the minutes, seconds, and fractional seconds must be zero. The value must be on or after `2024-01-01T00:00:00Z` and must be at least 14 days before the current time.
Type: Timestamp
Required: No

## See Also
<a name="API_DashAvailabilityStartTimeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/DashAvailabilityStartTimeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/DashAvailabilityStartTimeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/DashAvailabilityStartTimeConfiguration)
