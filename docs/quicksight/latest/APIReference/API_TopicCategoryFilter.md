---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicCategoryFilter.html
---

# TopicCategoryFilter
<a name="API_TopicCategoryFilter"></a>

A structure that represents a category filter.

## Contents
<a name="API_TopicCategoryFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CategoryFilterFunction **   <a name="QS-Type-TopicCategoryFilter-CategoryFilterFunction"></a>
The category filter function. Valid values for this structure are `EXACT` and `CONTAINS`.
Type: String
Valid Values: `EXACT | CONTAINS`
Required: No

 ** CategoryFilterType **   <a name="QS-Type-TopicCategoryFilter-CategoryFilterType"></a>
The category filter type. This element is used to specify whether a filter is a simple category filter or an inverse category filter.
Type: String
Valid Values: `CUSTOM_FILTER | CUSTOM_FILTER_LIST | FILTER_LIST`
Required: No

 ** Constant **   <a name="QS-Type-TopicCategoryFilter-Constant"></a>
The constant used in a category filter.
Type: [TopicCategoryFilterConstant](API_TopicCategoryFilterConstant.md) object
Required: No

 ** Inverse **   <a name="QS-Type-TopicCategoryFilter-Inverse"></a>
A Boolean value that indicates if the filter is inverse.
Type: Boolean
Required: No

 ** NullFilter **   <a name="QS-Type-TopicCategoryFilter-NullFilter"></a>
The `null` filter that is applied to the category filter.
Type: String
Valid Values: `ALL_VALUES | NON_NULLS_ONLY | NULLS_ONLY`
Required: No

## See Also
<a name="API_TopicCategoryFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicCategoryFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicCategoryFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicCategoryFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
