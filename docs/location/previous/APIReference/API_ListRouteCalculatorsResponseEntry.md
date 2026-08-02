---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_ListRouteCalculatorsResponseEntry.html
---

# ListRouteCalculatorsResponseEntry
<a name="API_ListRouteCalculatorsResponseEntry"></a>

A route calculator resource listed in your AWS account.

## Contents
<a name="API_ListRouteCalculatorsResponseEntry_Contents"></a>

 ** CalculatorName **   <a name="location-Type-ListRouteCalculatorsResponseEntry-CalculatorName"></a>
The name of the route calculator resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** CreateTime **   <a name="location-Type-ListRouteCalculatorsResponseEntry-CreateTime"></a>
The timestamp when the route calculator resource was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
+ For example, `2020–07-2T12:15:20.000Z+01:00`
Type: Timestamp
Required: Yes

 ** DataSource **   <a name="location-Type-ListRouteCalculatorsResponseEntry-DataSource"></a>
The data provider of traffic and road network data. Indicates one of the available providers:
+  `Esri`
+  `Grab`
+  `Here`
For more information about data providers, see [Amazon Location Service data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html).
Type: String
Required: Yes

 ** Description **   <a name="location-Type-ListRouteCalculatorsResponseEntry-Description"></a>
The optional description of the route calculator resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** UpdateTime **   <a name="location-Type-ListRouteCalculatorsResponseEntry-UpdateTime"></a>
The timestamp when the route calculator resource was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
+ For example, `2020–07-2T12:15:20.000Z+01:00`
Type: Timestamp
Required: Yes

 ** PricingPlan **   <a name="location-Type-ListRouteCalculatorsResponseEntry-PricingPlan"></a>
 *This member has been deprecated.*
Always returns `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`
Required: No

## See Also
<a name="API_ListRouteCalculatorsResponseEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/ListRouteCalculatorsResponseEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/ListRouteCalculatorsResponseEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/ListRouteCalculatorsResponseEntry)
