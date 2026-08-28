---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_DimensionValues.html
---

# DimensionValues
<a name="API_billing_DimensionValues"></a>

 The metadata that you can use to filter and group your results.

## Contents
<a name="API_billing_DimensionValues_Contents"></a>

 ** key **   <a name="awscostmanagement-Type-billing_DimensionValues-key"></a>
 The names of the metadata types that you can use to filter and group your results.
Type: String
Valid Values: `LINKED_ACCOUNT`
Required: Yes

 ** values **   <a name="awscostmanagement-Type-billing_DimensionValues-values"></a>
 The metadata values that you can use to filter and group your results.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

## See Also
<a name="API_billing_DimensionValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/DimensionValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/DimensionValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/DimensionValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
