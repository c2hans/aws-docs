---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_WorkloadInsightsTopContributorsDataPoint.html
---

# WorkloadInsightsTopContributorsDataPoint
<a name="API_WorkloadInsightsTopContributorsDataPoint"></a>

A data point for a top contributor network flow in a scope. Network Flow Monitor returns information about the network flows with the top values for each metric type, which are called top contributors.

## Contents
<a name="API_WorkloadInsightsTopContributorsDataPoint_Contents"></a>

 ** label **   <a name="networkflowmonitor-Type-WorkloadInsightsTopContributorsDataPoint-label"></a>
The label identifying the data point.
Type: String
Required: Yes

 ** timestamps **   <a name="networkflowmonitor-Type-WorkloadInsightsTopContributorsDataPoint-timestamps"></a>
An array of the timestamps for the data point.
Type: Array of timestamps
Required: Yes

 ** values **   <a name="networkflowmonitor-Type-WorkloadInsightsTopContributorsDataPoint-values"></a>
The values for the data point.
Type: Array of doubles
Required: Yes

## See Also
<a name="API_WorkloadInsightsTopContributorsDataPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/WorkloadInsightsTopContributorsDataPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/WorkloadInsightsTopContributorsDataPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/WorkloadInsightsTopContributorsDataPoint)
