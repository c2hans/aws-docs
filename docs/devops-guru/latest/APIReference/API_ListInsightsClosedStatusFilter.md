---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListInsightsClosedStatusFilter.html
---

# ListInsightsClosedStatusFilter
<a name="API_ListInsightsClosedStatusFilter"></a>

 Used to filter for insights that have the status `CLOSED`.

## Contents
<a name="API_ListInsightsClosedStatusFilter_Contents"></a>

 ** EndTimeRange **   <a name="DevOpsGuru-Type-ListInsightsClosedStatusFilter-EndTimeRange"></a>
 A time range used to specify when the behavior of the filtered insights ended.
Type: [EndTimeRange](API_EndTimeRange.md) object
Required: Yes

 ** Type **   <a name="DevOpsGuru-Type-ListInsightsClosedStatusFilter-Type"></a>
 Use to filter for either `REACTIVE` or `PROACTIVE` insights.
Type: String
Valid Values: `REACTIVE | PROACTIVE`
Required: Yes

## See Also
<a name="API_ListInsightsClosedStatusFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ListInsightsClosedStatusFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ListInsightsClosedStatusFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ListInsightsClosedStatusFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
