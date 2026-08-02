---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Segment.html
---

# Segment
<a name="API_Segment"></a>

Defines a non-overlapping region of a table's partitions, allowing multiple requests to be run in parallel.

## Contents
<a name="API_Segment_Contents"></a>

 ** SegmentNumber **   <a name="Glue-Type-Segment-SegmentNumber"></a>
The zero-based index number of the segment. For example, if the total number of segments is 4, `SegmentNumber` values range from 0 through 3.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** TotalSegments **   <a name="Glue-Type-Segment-TotalSegments"></a>
The total number of segments.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: Yes

## See Also
<a name="API_Segment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Segment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Segment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Segment)
