---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BillingFeatureFilter.html
---

# BillingFeatureFilter
<a name="API_billing_BillingFeatureFilter"></a>

A filter that narrows the set of preferences returned by `GetBillingPreferences`.

## Contents
<a name="API_billing_BillingFeatureFilter_Contents"></a>

 ** name **   <a name="awscostmanagement-Type-billing_BillingFeatureFilter-name"></a>
The filter name. Currently the only supported value is `PREFERENCE_KEY`.
Type: String
Valid Values: `PREFERENCE_KEY`
Required: No

 ** value **   <a name="awscostmanagement-Type-billing_BillingFeatureFilter-value"></a>
The filter values to match. For `PREFERENCE_KEY`, supply 1 to 10 preference key values to match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-/]+`
Required: No

## See Also
<a name="API_billing_BillingFeatureFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/BillingFeatureFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/BillingFeatureFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/BillingFeatureFilter)
