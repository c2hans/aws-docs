---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_TrafficSplitRequestOptions.html
---

# TrafficSplitRequestOptions
<a name="API_TrafficSplitRequestOptions"></a>

The traffic shift to perform for a cloned blue/green upgrade.

## Contents
<a name="API_TrafficSplitRequestOptions_Contents"></a>

 ** CloneReadTrafficPercent **   <a name="opensearchservice-Type-TrafficSplitRequestOptions-CloneReadTrafficPercent"></a>
The percentage of search traffic, from 0 to 100, to send to the cloned cluster. The rest goes to the primary cluster.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

 ** Strategy **   <a name="opensearchservice-Type-TrafficSplitRequestOptions-Strategy"></a>
The traffic shifting strategy. The only valid value is `ShiftReadTrafficPercent`.
Type: String
Valid Values: `ShiftReadTrafficPercent`
Required: Yes

## See Also
<a name="API_TrafficSplitRequestOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/TrafficSplitRequestOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/TrafficSplitRequestOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/TrafficSplitRequestOptions)
