---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BillingViewHealthStatus.html
---

# BillingViewHealthStatus
<a name="API_billing_BillingViewHealthStatus"></a>

 Represents the health status of a billing view, including a status code and optional reasons for the status.

## Contents
<a name="API_billing_BillingViewHealthStatus_Contents"></a>

 ** statusCode **   <a name="awscostmanagement-Type-billing_BillingViewHealthStatus-statusCode"></a>
The current health status code of the billing view.
Type: String
Valid Values: `HEALTHY | UNHEALTHY | CREATING | UPDATING`
Required: No

 ** statusReasons **   <a name="awscostmanagement-Type-billing_BillingViewHealthStatus-statusReasons"></a>
A list of reasons explaining the current health status, if applicable.
Type: Array of strings
Valid Values: `SOURCE_VIEW_UNHEALTHY | SOURCE_VIEW_UPDATING | SOURCE_VIEW_ACCESS_DENIED | SOURCE_VIEW_NOT_FOUND | CYCLIC_DEPENDENCY | SOURCE_VIEW_DEPTH_EXCEEDED | AGGREGATE_SOURCE | VIEW_OWNER_NOT_MANAGEMENT_ACCOUNT`
Required: No

## See Also
<a name="API_billing_BillingViewHealthStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/BillingViewHealthStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/BillingViewHealthStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/BillingViewHealthStatus)
