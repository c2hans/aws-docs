---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BillingPreferenceForKey.html
---

# BillingPreferenceForKey
<a name="API_billing_BillingPreferenceForKey"></a>

A single key/value entry used to update a billing preference.

## Contents
<a name="API_billing_BillingPreferenceForKey_Contents"></a>

 ** key **   <a name="awscostmanagement-Type-billing_BillingPreferenceForKey-key"></a>
The preference key. Format depends on the feature being updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2148.
Pattern: `[a-zA-Z0-9-\/\*: ]+`
Required: Yes

 ** value **   <a name="awscostmanagement-Type-billing_BillingPreferenceForKey-value"></a>
The preference value. Valid values: `ENABLED` or `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## See Also
<a name="API_billing_BillingPreferenceForKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/BillingPreferenceForKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/BillingPreferenceForKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/BillingPreferenceForKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
