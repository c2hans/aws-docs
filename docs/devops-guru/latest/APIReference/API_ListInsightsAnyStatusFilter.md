---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListInsightsAnyStatusFilter.html
---

# ListInsightsAnyStatusFilter
<a name="API_ListInsightsAnyStatusFilter"></a>

 Used to filter for insights that have any status.

## Contents
<a name="API_ListInsightsAnyStatusFilter_Contents"></a>

 ** StartTimeRange **   <a name="DevOpsGuru-Type-ListInsightsAnyStatusFilter-StartTimeRange"></a>
 A time range used to specify when the behavior of the filtered insights started.
Type: [StartTimeRange](API_StartTimeRange.md) object
Required: Yes

 ** Type **   <a name="DevOpsGuru-Type-ListInsightsAnyStatusFilter-Type"></a>
 Use to filter for either `REACTIVE` or `PROACTIVE` insights.
Type: String
Valid Values: `REACTIVE | PROACTIVE`
Required: Yes

## See Also
<a name="API_ListInsightsAnyStatusFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ListInsightsAnyStatusFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ListInsightsAnyStatusFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ListInsightsAnyStatusFilter)
