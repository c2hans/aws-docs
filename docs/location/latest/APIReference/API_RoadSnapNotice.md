---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RoadSnapNotice.html
---

# RoadSnapNotice
<a name="API_RoadSnapNotice"></a>

Notices provide information around factors that may have influenced snapping in a manner atypical to the standard use cases.

## Contents
<a name="API_RoadSnapNotice_Contents"></a>

 ** Code **   <a name="location-Type-RoadSnapNotice-Code"></a>
Code corresponding to the issue.
Type: String
Valid Values: `TracePointsHeadingIgnored | TracePointsIgnored | TracePointsMovedByLargeDistance | TracePointsNotMatched | TracePointsOutOfSequence | TracePointsSpeedEstimated | TracePointsSpeedIgnored`
Required: Yes

 ** Title **   <a name="location-Type-RoadSnapNotice-Title"></a>
The notice title.
Type: String
Required: Yes

 ** TracePointIndexes **   <a name="location-Type-RoadSnapNotice-TracePointIndexes"></a>
TracePoint indices for which the provided notice code corresponds to.
Type: Array of integers
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Required: Yes

## See Also
<a name="API_RoadSnapNotice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RoadSnapNotice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RoadSnapNotice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RoadSnapNotice)
