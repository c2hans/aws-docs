---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListPricingPlansFilter.html
---

# ListPricingPlansFilter
<a name="API_ListPricingPlansFilter"></a>

The filter that specifies the Amazon Resource Names (ARNs) of pricing plans, to retrieve pricing plan information.

## Contents
<a name="API_ListPricingPlansFilter_Contents"></a>

 ** Arns **   <a name="billingconductor-Type-ListPricingPlansFilter-Arns"></a>
A list of pricing plan Amazon Resource Names (ARNs) to retrieve information.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `(arn:aws(-cn)?:billingconductor::(aws|[0-9]{12}):pricingplan/)?(BasicPricingPlan|Passthrough|[a-zA-Z0-9]{10})`
Required: No

## See Also
<a name="API_ListPricingPlansFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListPricingPlansFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListPricingPlansFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListPricingPlansFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
