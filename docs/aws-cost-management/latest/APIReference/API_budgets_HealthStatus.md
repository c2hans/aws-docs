---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_HealthStatus.html
---

# HealthStatus
<a name="API_budgets_HealthStatus"></a>

Provides information about the current operational state of a billing view resource, including its ability to access and update based on its associated billing view.

## Contents
<a name="API_budgets_HealthStatus_Contents"></a>

 ** LastUpdatedTime **   <a name="awscostmanagement-Type-budgets_HealthStatus-LastUpdatedTime"></a>
 A generic time stamp. In Java, it's transformed to a `Date` object.
Type: Timestamp
Required: No

 ** Status **   <a name="awscostmanagement-Type-budgets_HealthStatus-Status"></a>
The current status of the billing view resource.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: No

 ** StatusReason **   <a name="awscostmanagement-Type-budgets_HealthStatus-StatusReason"></a>
The reason for the current status.
+  `BILLING_VIEW_NO_ACCESS`: The billing view resource does not grant `billing:GetBillingViewData` permission to this account.
+  `BILLING_VIEW_UNHEALTHY`: The billing view associated with the budget is unhealthy.
+  `FILTER_INVALID`: The filter contains reference to an account you do not have access to.
+  `MULTI_YEAR_HISTORICAL_DATA_DISABLED`: The budget is not being updated. Enable multi-year historical data in your Cost Management preferences.
Type: String
Valid Values: `BILLING_VIEW_NO_ACCESS | BILLING_VIEW_UNHEALTHY | FILTER_INVALID | MULTI_YEAR_HISTORICAL_DATA_DISABLED`
Required: No

## See Also
<a name="API_budgets_HealthStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/HealthStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/HealthStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/HealthStatus)
