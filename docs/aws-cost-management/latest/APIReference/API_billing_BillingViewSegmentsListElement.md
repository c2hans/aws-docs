---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BillingViewSegmentsListElement.html
---

# BillingViewSegmentsListElement
<a name="API_billing_BillingViewSegmentsListElement"></a>

 A billing view segment. A segment represents a time range during which the billing domain and account relationships for a billing view remained unchanged.

## Contents
<a name="API_billing_BillingViewSegmentsListElement_Contents"></a>

 ** billingGroupPrimaryAccountId **   <a name="awscostmanagement-Type-billing_BillingViewSegmentsListElement-billingGroupPrimaryAccountId"></a>
 The billing group primary account ID. The response includes this field for billing group members. Compare this value to your own account ID to determine whether you are the primary account.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** billingTransferAccountId **   <a name="awscostmanagement-Type-billing_BillingViewSegmentsListElement-billingTransferAccountId"></a>
 The billing transfer account ID. The response includes this field only when the caller is a billing transfer source account. The response omits this field for billing group billing views.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** domain **   <a name="awscostmanagement-Type-billing_BillingViewSegmentsListElement-domain"></a>
The billing domain for this segment. The following values are valid:
+  `PRO_FORMA` - Data shaped by AWS Billing Conductor that doesn't reflect the final charges owed to AWS.
+  `BILLABLE` - Data that represents the final charges owed to AWS.
Type: String
Valid Values: `BILLABLE | PRO_FORMA`
Required: No

 ** managementAccountId **   <a name="awscostmanagement-Type-billing_BillingViewSegmentsListElement-managementAccountId"></a>
 The management account ID of the organization. The response includes this field for organization member accounts.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** timeRange **   <a name="awscostmanagement-Type-billing_BillingViewSegmentsListElement-timeRange"></a>
 The time range during which this segment is effective.
Type: [BillingViewSegmentTimeRange](API_billing_BillingViewSegmentTimeRange.md) object
Required: No

## See Also
<a name="API_billing_BillingViewSegmentsListElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/BillingViewSegmentsListElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/BillingViewSegmentsListElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/BillingViewSegmentsListElement)
