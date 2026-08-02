---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AzElSegments.html
---

# AzElSegments
<a name="API_AzElSegments"></a>

Azimuth elevation segment collection.

Contains five or more time-ordered segments that define antenna pointing angles over the ephemeris validity period.

## Contents
<a name="API_AzElSegments_Contents"></a>

 ** angleUnit **   <a name="groundstation-Type-AzElSegments-angleUnit"></a>
The unit of measure for azimuth and elevation angles. All angles in all segments must use the same unit.
Type: String
Valid Values: `DEGREE_ANGLE | RADIAN`
Required: Yes

 ** azElSegmentList **   <a name="groundstation-Type-AzElSegments-azElSegmentList"></a>
List of azimuth elevation segments.
Must contain between 1 and 100 segments. Segments must be in chronological order with no overlaps.
Type: Array of [AzElSegment](API_AzElSegment.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## See Also
<a name="API_AzElSegments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/AzElSegments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/AzElSegments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/AzElSegments)
