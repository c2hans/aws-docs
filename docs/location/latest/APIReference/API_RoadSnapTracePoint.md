---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RoadSnapTracePoint.html
---

# RoadSnapTracePoint
<a name="API_RoadSnapTracePoint"></a>

TracePoint indices for which the provided notice code corresponds to.

## Contents
<a name="API_RoadSnapTracePoint_Contents"></a>

 ** Position **   <a name="location-Type-RoadSnapTracePoint-Position"></a>
Position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** Heading **   <a name="location-Type-RoadSnapTracePoint-Heading"></a>
GPS Heading at the position.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 360.0.
Required: No

 ** Speed **   <a name="location-Type-RoadSnapTracePoint-Speed"></a>
Speed at the specified trace point .
 **Unit**: `kilometers per hour`
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

 ** Timestamp **   <a name="location-Type-RoadSnapTracePoint-Timestamp"></a>
Timestamp of the event.
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: No

## See Also
<a name="API_RoadSnapTracePoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RoadSnapTracePoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RoadSnapTracePoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RoadSnapTracePoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
