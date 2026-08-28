---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_ListTrackersResponseEntry.html
---

# ListTrackersResponseEntry
<a name="API_ListTrackersResponseEntry"></a>

Contains the tracker resource details.

## Contents
<a name="API_ListTrackersResponseEntry_Contents"></a>

 ** CreateTime **   <a name="location-Type-ListTrackersResponseEntry-CreateTime"></a>
The timestamp for when the tracker resource was created in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp
Required: Yes

 ** Description **   <a name="location-Type-ListTrackersResponseEntry-Description"></a>
The description for the tracker resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** TrackerName **   <a name="location-Type-ListTrackersResponseEntry-TrackerName"></a>
The name of the tracker resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** UpdateTime **   <a name="location-Type-ListTrackersResponseEntry-UpdateTime"></a>
The timestamp at which the device's position was determined. Uses [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp
Required: Yes

 ** PricingPlan **   <a name="location-Type-ListTrackersResponseEntry-PricingPlan"></a>
 *This member has been deprecated.*
Always returns `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`
Required: No

 ** PricingPlanDataSource **   <a name="location-Type-ListTrackersResponseEntry-PricingPlanDataSource"></a>
 *This member has been deprecated.*
No longer used. Always returns an empty string.
Type: String
Required: No

## See Also
<a name="API_ListTrackersResponseEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/ListTrackersResponseEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/ListTrackersResponseEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/ListTrackersResponseEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
