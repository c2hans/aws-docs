---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_ScheduledQueryInsights.html
---

# ScheduledQueryInsights
<a name="API_query_ScheduledQueryInsights"></a>

Encapsulates settings for enabling `QueryInsights` on an `ExecuteScheduledQueryRequest`.

## Contents
<a name="API_query_ScheduledQueryInsights_Contents"></a>

 ** Mode **   <a name="timestream-Type-query_ScheduledQueryInsights-Mode"></a>
Provides the following modes to enable `ScheduledQueryInsights`:
+  `ENABLED_WITH_RATE_CONTROL` – Enables `ScheduledQueryInsights` for the queries being processed. This mode also includes a rate control mechanism, which limits the `QueryInsights` feature to 1 query per second (QPS).
+  `DISABLED` – Disables `ScheduledQueryInsights`.
Type: String
Valid Values: `ENABLED_WITH_RATE_CONTROL | DISABLED`
Required: Yes

## See Also
<a name="API_query_ScheduledQueryInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/ScheduledQueryInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/ScheduledQueryInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/ScheduledQueryInsights)
