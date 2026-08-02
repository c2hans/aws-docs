---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianNotice.html
---

# RoutePedestrianNotice
<a name="API_RoutePedestrianNotice"></a>

Notices are additional information returned that indicate issues that occurred during route calculation.

## Contents
<a name="API_RoutePedestrianNotice_Contents"></a>

 ** Code **   <a name="location-Type-RoutePedestrianNotice-Code"></a>
Code corresponding to the issue.
Type: String
Valid Values: `AccuratePolylineUnavailable | Other | ViolatedAvoidDirtRoad | ViolatedAvoidTunnel | ViolatedPedestrianOption | ViolatedAvoidAreas`
Required: Yes

 ** Impact **   <a name="location-Type-RoutePedestrianNotice-Impact"></a>
Impact corresponding to the issue. While Low impact notices can be safely ignored, High impact notices must be evaluated further to determine the impact.
Type: String
Valid Values: `High | Low`
Required: No

## See Also
<a name="API_RoutePedestrianNotice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RoutePedestrianNotice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RoutePedestrianNotice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RoutePedestrianNotice)
