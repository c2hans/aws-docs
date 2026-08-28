---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeRepositoryAggregation.html
---

# CodeRepositoryAggregation
<a name="API_CodeRepositoryAggregation"></a>

The details that define an aggregation based on code repositories.

## Contents
<a name="API_CodeRepositoryAggregation_Contents"></a>

 ** projectNames **   <a name="inspector2-Type-CodeRepositoryAggregation-projectNames"></a>
The project names to include in the aggregation results.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** providerTypes **   <a name="inspector2-Type-CodeRepositoryAggregation-providerTypes"></a>
The repository provider types to include in the aggregation results.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceIds **   <a name="inspector2-Type-CodeRepositoryAggregation-resourceIds"></a>
The resource IDs to include in the aggregation results.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** sortBy **   <a name="inspector2-Type-CodeRepositoryAggregation-sortBy"></a>
The value to sort results by in the code repository aggregation.
Type: String
Valid Values: `CRITICAL | HIGH | ALL`
Required: No

 ** sortOrder **   <a name="inspector2-Type-CodeRepositoryAggregation-sortOrder"></a>
The order to sort results by (ascending or descending) in the code repository aggregation.
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_CodeRepositoryAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CodeRepositoryAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CodeRepositoryAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CodeRepositoryAggregation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
