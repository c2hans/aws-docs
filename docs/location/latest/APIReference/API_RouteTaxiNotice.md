---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTaxiNotice.html
---

# RouteTaxiNotice
<a name="API_RouteTaxiNotice"></a>

A notice that indicates an issue that occurred during route calculation.

## Contents
<a name="API_RouteTaxiNotice_Contents"></a>

 ** Code **   <a name="location-Type-RouteTaxiNotice-Code"></a>
Code corresponding to the issue.
Type: String
Valid Values: `AccuratePolylineUnavailable | Other`
Required: Yes

 ** Impact **   <a name="location-Type-RouteTaxiNotice-Impact"></a>
Impact corresponding to the issue. While Low impact notices can be safely ignored, High impact notices must be evaluated further to determine the impact.
Type: String
Valid Values: `High | Low`
Required: No

## See Also
<a name="API_RouteTaxiNotice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTaxiNotice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTaxiNotice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTaxiNotice)
