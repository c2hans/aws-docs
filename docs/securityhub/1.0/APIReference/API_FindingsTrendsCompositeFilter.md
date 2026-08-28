---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FindingsTrendsCompositeFilter.html
---

# FindingsTrendsCompositeFilter
<a name="API_FindingsTrendsCompositeFilter"></a>

A filter structure that contains a logical combination of string filters and nested composite filters for findings trend data.

## Contents
<a name="API_FindingsTrendsCompositeFilter_Contents"></a>

 ** NestedCompositeFilters **   <a name="securityhub-Type-FindingsTrendsCompositeFilter-NestedCompositeFilters"></a>
A list of nested composite filters that you can use to create complex filter conditions for findings trend data.
Type: Array of [FindingsTrendsCompositeFilter](#API_FindingsTrendsCompositeFilter) objects
Required: No

 ** Operator **   <a name="securityhub-Type-FindingsTrendsCompositeFilter-Operator"></a>
The logical operator (AND, OR) to apply between the string filters and nested composite filters.
Type: String
Valid Values: `AND | OR`
Required: No

 ** StringFilters **   <a name="securityhub-Type-FindingsTrendsCompositeFilter-StringFilters"></a>
A list of string filters that apply to findings trend data fields.
Type: Array of [FindingsTrendsStringFilter](API_FindingsTrendsStringFilter.md) objects
Required: No

## See Also
<a name="API_FindingsTrendsCompositeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/FindingsTrendsCompositeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/FindingsTrendsCompositeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/FindingsTrendsCompositeFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
