---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicNullFilter.html
---

# TopicNullFilter
<a name="API_TopicNullFilter"></a>

The structure that represents a null filter.

## Contents
<a name="API_TopicNullFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Constant **   <a name="QS-Type-TopicNullFilter-Constant"></a>
A structure that represents a singular filter constant, used in filters to specify a single value to match against.
Type: [TopicSingularFilterConstant](API_TopicSingularFilterConstant.md) object
Required: No

 ** Inverse **   <a name="QS-Type-TopicNullFilter-Inverse"></a>
A Boolean value that indicates if the filter is inverse.
Type: Boolean
Required: No

 ** NullFilterType **   <a name="QS-Type-TopicNullFilter-NullFilterType"></a>
The type of the null filter. Valid values for this type are `NULLS_ONLY`, `NON_NULLS_ONLY`, and `ALL_VALUES`.
Type: String
Valid Values: `ALL_VALUES | NON_NULLS_ONLY | NULLS_ONLY`
Required: No

## See Also
<a name="API_TopicNullFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicNullFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicNullFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicNullFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
