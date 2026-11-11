---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_TrafficPercents.html
---

# TrafficPercents
<a name="API_TrafficPercents"></a>

The split of search traffic between the primary and cloned clusters.

## Contents
<a name="API_TrafficPercents_Contents"></a>

 ** CloneReadTrafficPercent **   <a name="opensearchservice-Type-TrafficPercents-CloneReadTrafficPercent"></a>
The percentage of search traffic sent to the cloned cluster.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

 ** PrimaryReadTrafficPercent **   <a name="opensearchservice-Type-TrafficPercents-PrimaryReadTrafficPercent"></a>
The percentage of search traffic sent to the primary cluster.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

## See Also
<a name="API_TrafficPercents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/TrafficPercents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/TrafficPercents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/TrafficPercents)
