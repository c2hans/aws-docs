---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_MetricFilterV2.html
---

# MetricFilterV2
<a name="API_MetricFilterV2"></a>

Contains information about the filter used when retrieving metrics. `MetricFiltersV2` can be used on the following metrics: `AVG_AGENT_CONNECTING_TIME`, `CONTACTS_CREATED`, `CONTACTS_HANDLED`, `SUM_CONTACTS_DISCONNECTED`.

## Contents
<a name="API_MetricFilterV2_Contents"></a>

 ** MetricFilterKey **   <a name="connect-Type-MetricFilterV2-MetricFilterKey"></a>
The key to use for filtering data.
Valid metric filter keys:
+ ANSWERING\_MACHINE\_DETECTION\_STATUS
+ CASE\_STATUS
+ DISCONNECT\_REASON
+ FLOWS\_ACTION\_IDENTIFIER
+ FLOWS\_NEXT\_ACTION\_IDENTIFIER
+ FLOWS\_OUTCOME\_TYPE
+ FLOWS\_RESOURCE\_TYPE
+ INITIATION\_METHOD
Type: String
Required: No

 ** MetricFilterValues **   <a name="connect-Type-MetricFilterV2-MetricFilterValues"></a>
The values to use for filtering data. Values for metric-level filters can be either a fixed set of values or a customized list, depending on the use case.
For valid values of metric-level filters `INITIATION_METHOD`, `DISCONNECT_REASON`, and `ANSWERING_MACHINE_DETECTION_STATUS`, see [ContactTraceRecord](https://docs.aws.amazon.com/connect/latest/adminguide/ctr-data-model.html#ctr-ContactTraceRecord) in the *Connect Customer Administrator Guide*.
For valid values of the metric-level filter `FLOWS_OUTCOME_TYPE`, see the description for the [Flow outcome](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#flows-outcome) metric in the *Connect Customer Administrator Guide*.
For valid values of the metric-level filter `BOT_CONVERSATION_OUTCOME_TYPE`, see the description for the [Bot conversations completed](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#bot-conversations-completed-metric) in the *Connect Customer Administrator Guide*.
For valid values of the metric-level filter `BOT_INTENT_OUTCOME_TYPE`, see the description for the [Bot intents completed](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#bot-intents-completed-metric) metric in the *Connect Customer Administrator Guide*.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** Negate **   <a name="connect-Type-MetricFilterV2-Negate"></a>
If set to `true`, the API response contains results that filter out the results matched by the metric-level filters condition. By default, `Negate` is set to `false`.
Type: Boolean
Required: No

## See Also
<a name="API_MetricFilterV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/MetricFilterV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/MetricFilterV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/MetricFilterV2)
