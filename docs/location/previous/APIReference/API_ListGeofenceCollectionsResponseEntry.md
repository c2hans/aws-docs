---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_ListGeofenceCollectionsResponseEntry.html
---

# ListGeofenceCollectionsResponseEntry
<a name="API_ListGeofenceCollectionsResponseEntry"></a>

Contains the geofence collection details.

**Note**
The returned geometry will always match the geometry format used when the geofence was created.

## Contents
<a name="API_ListGeofenceCollectionsResponseEntry_Contents"></a>

 ** CollectionName **   <a name="location-Type-ListGeofenceCollectionsResponseEntry-CollectionName"></a>
The name of the geofence collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** CreateTime **   <a name="location-Type-ListGeofenceCollectionsResponseEntry-CreateTime"></a>
The timestamp for when the geofence collection was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`
Type: Timestamp
Required: Yes

 ** Description **   <a name="location-Type-ListGeofenceCollectionsResponseEntry-Description"></a>
The description for the geofence collection
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** UpdateTime **   <a name="location-Type-ListGeofenceCollectionsResponseEntry-UpdateTime"></a>
Specifies a timestamp for when the resource was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`
Type: Timestamp
Required: Yes

 ** PricingPlan **   <a name="location-Type-ListGeofenceCollectionsResponseEntry-PricingPlan"></a>
 *This member has been deprecated.*
No longer used. Always returns `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`
Required: No

 ** PricingPlanDataSource **   <a name="location-Type-ListGeofenceCollectionsResponseEntry-PricingPlanDataSource"></a>
 *This member has been deprecated.*
No longer used. Always returns an empty string.
Type: String
Required: No

## See Also
<a name="API_ListGeofenceCollectionsResponseEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/ListGeofenceCollectionsResponseEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/ListGeofenceCollectionsResponseEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/ListGeofenceCollectionsResponseEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
