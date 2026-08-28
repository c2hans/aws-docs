---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_BillingAndCostManagementRecommendedActions_ActionFilter.html
---

# ActionFilter
<a name="API_BillingAndCostManagementRecommendedActions_ActionFilter"></a>

Describes a filter that returns a more specific list of recommended actions.

## Contents
<a name="API_BillingAndCostManagementRecommendedActions_ActionFilter_Contents"></a>

 ** key **   <a name="awscostmanagement-Type-BillingAndCostManagementRecommendedActions_ActionFilter-key"></a>
The category to filter on. Valid values are `FEATURE` for feature type, `SEVERITY` for severity level, and `TYPE` for recommendation type.
Type: String
Valid Values: `FEATURE | SEVERITY | TYPE`
Required: Yes

 ** matchOption **   <a name="awscostmanagement-Type-BillingAndCostManagementRecommendedActions_ActionFilter-matchOption"></a>
Specifies how to apply the filter. Use `EQUALS` to include matching results or `NOT_EQUALS` to exclude matching results.
Type: String
Valid Values: `EQUALS | NOT_EQUALS`
Required: Yes

 ** values **   <a name="awscostmanagement-Type-BillingAndCostManagementRecommendedActions_ActionFilter-values"></a>
One or more values to match against the specified key.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*[\S\s]*.*`
Required: Yes

## See Also
<a name="API_BillingAndCostManagementRecommendedActions_ActionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-recommended-actions-2024-11-14/ActionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-recommended-actions-2024-11-14/ActionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-recommended-actions-2024-11-14/ActionFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
