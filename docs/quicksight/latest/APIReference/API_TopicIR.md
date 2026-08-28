---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicIR.html
---

# TopicIR
<a name="API_TopicIR"></a>

The definition for a `TopicIR`.

## Contents
<a name="API_TopicIR_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContributionAnalysis **   <a name="QS-Type-TopicIR-ContributionAnalysis"></a>
The contribution analysis for the `TopicIR`.
Type: [TopicIRContributionAnalysis](API_TopicIRContributionAnalysis.md) object
Required: No

 ** Filters **   <a name="QS-Type-TopicIR-Filters"></a>
The filters for the `TopicIR`.
Type: Array of arrays of [TopicIRFilterOption](API_TopicIRFilterOption.md) objects
Array Members: Maximum number of 2000 items.
Array Members: Maximum number of 2000 items.
Required: No

 ** GroupByList **   <a name="QS-Type-TopicIR-GroupByList"></a>
The GroupBy list for the `TopicIR`.
Type: Array of [TopicIRGroupBy](API_TopicIRGroupBy.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** Metrics **   <a name="QS-Type-TopicIR-Metrics"></a>
The metrics for the `TopicIR`.
Type: Array of [TopicIRMetric](API_TopicIRMetric.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** Sort **   <a name="QS-Type-TopicIR-Sort"></a>
The sort for the `TopicIR`.
Type: [TopicSortClause](API_TopicSortClause.md) object
Required: No

 ** Visual **   <a name="QS-Type-TopicIR-Visual"></a>
The visual for the `TopicIR`.
Type: [VisualOptions](API_VisualOptions.md) object
Required: No

## See Also
<a name="API_TopicIR_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicIR)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicIR)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicIR)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
