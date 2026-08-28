---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ReverseGeocodeFilter.html
---

# ReverseGeocodeFilter
<a name="API_geoplaces_ReverseGeocodeFilter"></a>

The included place types.

## Contents
<a name="API_geoplaces_ReverseGeocodeFilter_Contents"></a>

 ** IncludePlaceTypes **   <a name="location-Type-geoplaces_ReverseGeocodeFilter-IncludePlaceTypes"></a>
 The included place types. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions support only `Street` and `PointAddress` values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 7 items.
Valid Values: `Locality | Intersection | Street | PointAddress | InterpolatedAddress | SecondaryAddress | PointOfInterest`
Required: No

## See Also
<a name="API_geoplaces_ReverseGeocodeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/ReverseGeocodeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/ReverseGeocodeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/ReverseGeocodeFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
