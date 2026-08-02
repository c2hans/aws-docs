---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListTrackersResponseEntry.html
---

# ListTrackersResponseEntry
<a name="API_WaypointTracking_ListTrackersResponseEntry"></a>

Contains the tracker resource details.

## Contents
<a name="API_WaypointTracking_ListTrackersResponseEntry_Contents"></a>

 ** CreateTime **   <a name="location-Type-WaypointTracking_ListTrackersResponseEntry-CreateTime"></a>
The timestamp for when the tracker resource was created in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp
Required: Yes

 ** Description **   <a name="location-Type-WaypointTracking_ListTrackersResponseEntry-Description"></a>
The description for the tracker resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** TrackerName **   <a name="location-Type-WaypointTracking_ListTrackersResponseEntry-TrackerName"></a>
The name of the tracker resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** UpdateTime **   <a name="location-Type-WaypointTracking_ListTrackersResponseEntry-UpdateTime"></a>
The timestamp at which the device's position was determined. Uses [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp
Required: Yes

 ** PricingPlan **   <a name="location-Type-WaypointTracking_ListTrackersResponseEntry-PricingPlan"></a>
 *This member has been deprecated.*
Always returns `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`
Required: No

 ** PricingPlanDataSource **   <a name="location-Type-WaypointTracking_ListTrackersResponseEntry-PricingPlanDataSource"></a>
 *This member has been deprecated.*
No longer used. Always returns an empty string.
Type: String
Required: No

## See Also
<a name="API_WaypointTracking_ListTrackersResponseEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointtracking-2020-11-19/ListTrackersResponseEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointtracking-2020-11-19/ListTrackersResponseEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointtracking-2020-11-19/ListTrackersResponseEntry)
