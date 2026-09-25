---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_EdgeTrafficStats.html
---

# EdgeTrafficStats
<a name="API_EdgeTrafficStats"></a>

Additive traffic counters accumulated over an edge's observation window. Which counters are populated depends on what produced the edge.

## Contents
<a name="API_EdgeTrafficStats_Contents"></a>

 ** bytes **   <a name="cloudwatchomni-Type-EdgeTrafficStats-bytes"></a>
Total bytes observed across the edge.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** flows **   <a name="cloudwatchomni-Type-EdgeTrafficStats-flows"></a>
Total network flows observed across the edge.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** packets **   <a name="cloudwatchomni-Type-EdgeTrafficStats-packets"></a>
Total packets observed across the edge.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** receivedBytes **   <a name="cloudwatchomni-Type-EdgeTrafficStats-receivedBytes"></a>
Total bytes received from the destination.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** sentBytes **   <a name="cloudwatchomni-Type-EdgeTrafficStats-sentBytes"></a>
Total bytes sent to the destination.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_EdgeTrafficStats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/EdgeTrafficStats)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/EdgeTrafficStats)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/EdgeTrafficStats)
