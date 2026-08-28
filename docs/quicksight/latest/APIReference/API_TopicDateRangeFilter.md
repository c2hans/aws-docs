---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicDateRangeFilter.html
---

# TopicDateRangeFilter
<a name="API_TopicDateRangeFilter"></a>

A filter used to restrict data based on a range of dates or times.

## Contents
<a name="API_TopicDateRangeFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Constant **   <a name="QS-Type-TopicDateRangeFilter-Constant"></a>
The constant used in a date range filter.
Type: [TopicRangeFilterConstant](API_TopicRangeFilterConstant.md) object
Required: No

 ** Inclusive **   <a name="QS-Type-TopicDateRangeFilter-Inclusive"></a>
A Boolean value that indicates whether the date range filter should include the boundary values. If set to true, the filter includes the start and end dates. If set to false, the filter excludes them.
Type: Boolean
Required: No

 ** NullFilter **   <a name="QS-Type-TopicDateRangeFilter-NullFilter"></a>
The `null` filter that is applied to the date range filter.
Type: String
Valid Values: `ALL_VALUES | NON_NULLS_ONLY | NULLS_ONLY`
Required: No

## See Also
<a name="API_TopicDateRangeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicDateRangeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicDateRangeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicDateRangeFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
