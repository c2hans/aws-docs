---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListInsightsStatusFilter.html
---

# ListInsightsStatusFilter
<a name="API_ListInsightsStatusFilter"></a>

 A filter used by `ListInsights` to specify which insights to return.

## Contents
<a name="API_ListInsightsStatusFilter_Contents"></a>

 ** Any **   <a name="DevOpsGuru-Type-ListInsightsStatusFilter-Any"></a>
 A `ListInsightsAnyStatusFilter` that specifies insights of any status that are either `REACTIVE` or `PROACTIVE`.
Type: [ListInsightsAnyStatusFilter](API_ListInsightsAnyStatusFilter.md) object
Required: No

 ** Closed **   <a name="DevOpsGuru-Type-ListInsightsStatusFilter-Closed"></a>
 A `ListInsightsClosedStatusFilter` that specifies closed insights that are either `REACTIVE` or `PROACTIVE`.
Type: [ListInsightsClosedStatusFilter](API_ListInsightsClosedStatusFilter.md) object
Required: No

 ** Ongoing **   <a name="DevOpsGuru-Type-ListInsightsStatusFilter-Ongoing"></a>
 A `ListInsightsAnyStatusFilter` that specifies ongoing insights that are either `REACTIVE` or `PROACTIVE`.
Type: [ListInsightsOngoingStatusFilter](API_ListInsightsOngoingStatusFilter.md) object
Required: No

## See Also
<a name="API_ListInsightsStatusFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ListInsightsStatusFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ListInsightsStatusFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ListInsightsStatusFilter)
