---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_QueryRange.html
---

# QueryRange
<a name="API_QueryRange"></a>

Defines a time range for dependency query data.

## Contents
<a name="API_QueryRange_Contents"></a>

 ** dataPoints **   <a name="ngresiliencehub-Type-QueryRange-dataPoints"></a>
The data points within the query range.
Type: Array of [QueryDataPoint](API_QueryDataPoint.md) objects
Array Members: Minimum number of 7 items. Maximum number of 24 items.
Required: Yes

 ** endTime **   <a name="ngresiliencehub-Type-QueryRange-endTime"></a>
The end time of the query range.
Type: Timestamp
Required: Yes

 ** granularity **   <a name="ngresiliencehub-Type-QueryRange-granularity"></a>
The granularity of the query range data points.
Type: String
Valid Values: `HOURLY | DAILY`
Required: Yes

 ** startTime **   <a name="ngresiliencehub-Type-QueryRange-startTime"></a>
The start time of the query range.
Type: Timestamp
Required: Yes

## See Also
<a name="API_QueryRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/QueryRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/QueryRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/QueryRange)
