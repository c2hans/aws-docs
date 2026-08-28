---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_ListPlaceIndexesResponseEntry.html
---

# ListPlaceIndexesResponseEntry
<a name="API_ListPlaceIndexesResponseEntry"></a>

A place index resource listed in your AWS account.

## Contents
<a name="API_ListPlaceIndexesResponseEntry_Contents"></a>

 ** CreateTime **   <a name="location-Type-ListPlaceIndexesResponseEntry-CreateTime"></a>
The timestamp for when the place index resource was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp
Required: Yes

 ** DataSource **   <a name="location-Type-ListPlaceIndexesResponseEntry-DataSource"></a>
The data provider of geospatial data. Values can be one of the following:
+  `Esri`
+  `Grab`
+  `Here`
For more information about data providers, see [Amazon Location Service data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html).
Type: String
Required: Yes

 ** Description **   <a name="location-Type-ListPlaceIndexesResponseEntry-Description"></a>
The optional description for the place index resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** IndexName **   <a name="location-Type-ListPlaceIndexesResponseEntry-IndexName"></a>
The name of the place index resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** UpdateTime **   <a name="location-Type-ListPlaceIndexesResponseEntry-UpdateTime"></a>
The timestamp for when the place index resource was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp
Required: Yes

 ** PricingPlan **   <a name="location-Type-ListPlaceIndexesResponseEntry-PricingPlan"></a>
 *This member has been deprecated.*
No longer used. Always returns `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`
Required: No

## See Also
<a name="API_ListPlaceIndexesResponseEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/ListPlaceIndexesResponseEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/ListPlaceIndexesResponseEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/ListPlaceIndexesResponseEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
