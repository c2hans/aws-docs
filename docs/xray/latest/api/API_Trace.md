---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_Trace.html
---

# Trace
<a name="API_Trace"></a>

A collection of segment documents with matching trace IDs.

## Contents
<a name="API_Trace_Contents"></a>

 ** Duration **   <a name="xray-Type-Trace-Duration"></a>
The length of time in seconds between the start time of the earliest segment that started and the end time of the last segment that completed.
Type: Double
Required: No

 ** Id **   <a name="xray-Type-Trace-Id"></a>
The unique identifier for the request that generated the trace's segments and subsegments.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 35.
Required: No

 ** LimitExceeded **   <a name="xray-Type-Trace-LimitExceeded"></a>
LimitExceeded is set to true when the trace has exceeded the `Trace document size` limit. For more information about this limit and other X-Ray limits and quotas, see [AWS X-Ray endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/xray.html).
Type: Boolean
Required: No

 ** Segments **   <a name="xray-Type-Trace-Segments"></a>
Segment documents for the segments and subsegments that comprise the trace.
Type: Array of [Segment](API_Segment.md) objects
Required: No

## See Also
<a name="API_Trace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/Trace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/Trace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/Trace)
