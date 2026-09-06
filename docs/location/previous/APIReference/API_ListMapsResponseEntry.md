---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_ListMapsResponseEntry.html
---

# ListMapsResponseEntry
<a name="API_ListMapsResponseEntry"></a>

Contains details of an existing map resource in your AWS account.

## Contents
<a name="API_ListMapsResponseEntry_Contents"></a>

 ** CreateTime **   <a name="location-Type-ListMapsResponseEntry-CreateTime"></a>
The timestamp for when the map resource was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp
Required: Yes

 ** DataSource **   <a name="location-Type-ListMapsResponseEntry-DataSource"></a>
Specifies the data provider for the associated map tiles.
Type: String
Required: Yes

 ** Description **   <a name="location-Type-ListMapsResponseEntry-Description"></a>
The description for the map resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** MapName **   <a name="location-Type-ListMapsResponseEntry-MapName"></a>
The name of the associated map resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** UpdateTime **   <a name="location-Type-ListMapsResponseEntry-UpdateTime"></a>
The timestamp for when the map resource was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp
Required: Yes

 ** PricingPlan **   <a name="location-Type-ListMapsResponseEntry-PricingPlan"></a>
 *This member has been deprecated.*
No longer used. Always returns `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`
Required: No

## See Also
<a name="API_ListMapsResponseEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/ListMapsResponseEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/ListMapsResponseEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/ListMapsResponseEntry)
