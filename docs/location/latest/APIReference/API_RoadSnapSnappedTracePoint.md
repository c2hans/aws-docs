---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RoadSnapSnappedTracePoint.html
---

# RoadSnapSnappedTracePoint
<a name="API_RoadSnapSnappedTracePoint"></a>

TracePoints snapped onto the road network.

## Contents
<a name="API_RoadSnapSnappedTracePoint_Contents"></a>

 ** Confidence **   <a name="location-Type-RoadSnapSnappedTracePoint-Confidence"></a>
Confidence value for the correctness of this point match.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

 ** OriginalPosition **   <a name="location-Type-RoadSnapSnappedTracePoint-OriginalPosition"></a>
Position of the TracePoint provided within the request, at the same index.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** SnappedPosition **   <a name="location-Type-RoadSnapSnappedTracePoint-SnappedPosition"></a>
Snapped position of the TracePoint provided within the request, at the same index.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

## See Also
<a name="API_RoadSnapSnappedTracePoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RoadSnapSnappedTracePoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RoadSnapSnappedTracePoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RoadSnapSnappedTracePoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
