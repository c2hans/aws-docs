---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_TrafficSplitOptions.html
---

# TrafficSplitOptions
<a name="API_TrafficSplitOptions"></a>

The traffic split and status for a cloned blue/green upgrade.

## Contents
<a name="API_TrafficSplitOptions_Contents"></a>

 ** Current **   <a name="opensearchservice-Type-TrafficSplitOptions-Current"></a>
The traffic split currently in effect.
Type: [TrafficPercents](API_TrafficPercents.md) object
Required: Yes

 ** Status **   <a name="opensearchservice-Type-TrafficSplitOptions-Status"></a>
The status of the traffic shift.
Type: String
Valid Values: `InProgress | Completed | Failed`
Required: Yes

 ** Target **   <a name="opensearchservice-Type-TrafficSplitOptions-Target"></a>
The requested traffic split.
Type: [TrafficPercents](API_TrafficPercents.md) object
Required: Yes

## See Also
<a name="API_TrafficSplitOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/TrafficSplitOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/TrafficSplitOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/TrafficSplitOptions)
