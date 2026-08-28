---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListPricingRulesFilter.html
---

# ListPricingRulesFilter
<a name="API_ListPricingRulesFilter"></a>

 The filter that specifies criteria that the pricing rules returned by the `ListPricingRules` API will adhere to.

## Contents
<a name="API_ListPricingRulesFilter_Contents"></a>

 ** Arns **   <a name="billingconductor-Type-ListPricingRulesFilter-Arns"></a>
A list containing the pricing rule Amazon Resource Names (ARNs) to include in the API response.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:pricingrule/)?[a-zA-Z0-9]{10}`
Required: No

## See Also
<a name="API_ListPricingRulesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListPricingRulesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListPricingRulesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListPricingRulesFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
