---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BillingPreferenceSummary.html
---

# BillingPreferenceSummary
<a name="API_billing_BillingPreferenceSummary"></a>

A single billing preference entry returned by `GetBillingPreferences`.

## Contents
<a name="API_billing_BillingPreferenceSummary_Contents"></a>

 ** feature **   <a name="awscostmanagement-Type-billing_BillingPreferenceSummary-feature"></a>
The feature this preference belongs to.
Type: String
Valid Values: `RI_SHARING | RI_SHARING_HISTORY | CREDIT_SHARING | CREDIT_SHARING_HISTORY | CREDIT_LEVEL_SHARING | BILLING_ALERTS | CREDIT_PREFERENCE_OPTIONS`
Required: Yes

 ** key **   <a name="awscostmanagement-Type-billing_BillingPreferenceSummary-key"></a>
The preference key. Format depends on the feature.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2148.
Pattern: `[a-zA-Z0-9-\/\*: ]+`
Required: Yes

 ** value **   <a name="awscostmanagement-Type-billing_BillingPreferenceSummary-value"></a>
The preference value. Valid values: `ENABLED` or `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** accountId **   <a name="awscostmanagement-Type-billing_BillingPreferenceSummary-accountId"></a>
The associated AWS account ID. Populated for account-list keys; `null` otherwise.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** accountName **   <a name="awscostmanagement-Type-billing_BillingPreferenceSummary-accountName"></a>
The display name of the account. Populated together with `accountId`; `null` otherwise.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** billingPeriod **   <a name="awscostmanagement-Type-billing_BillingPreferenceSummary-billingPeriod"></a>
The billing period associated with the preference change. Populated only for the history features `RI_SHARING_HISTORY` and `CREDIT_SHARING_HISTORY`.
Type: [BillingPeriod](API_billing_BillingPeriod.md) object
Required: No

## See Also
<a name="API_billing_BillingPreferenceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/BillingPreferenceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/BillingPreferenceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/BillingPreferenceSummary)
