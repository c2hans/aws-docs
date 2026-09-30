---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BusinessSupportServiceSpend.html
---

# BusinessSupportServiceSpend
<a name="API_billing_BusinessSupportServiceSpend"></a>

A service-level spend entry contributing to Business Support eligible spend.

## Contents
<a name="API_billing_BusinessSupportServiceSpend_Contents"></a>

 ** chargeAmount **   <a name="awscostmanagement-Type-billing_BusinessSupportServiceSpend-chargeAmount"></a>
The Support-eligible spend amount for this service.
Type: String
Required: Yes

 ** contributingService **   <a name="awscostmanagement-Type-billing_BusinessSupportServiceSpend-contributingService"></a>
The name of the AWS service contributing to the Support-eligible spend.
Type: String
Required: Yes

 ** currency **   <a name="awscostmanagement-Type-billing_BusinessSupportServiceSpend-currency"></a>
The ISO 4217 currency code for the charge amount (for example, `USD`).
Type: String
Required: Yes

 ** itemType **   <a name="awscostmanagement-Type-billing_BusinessSupportServiceSpend-itemType"></a>
The type of the line item. Valid values: `Usage`.
Type: String
Required: Yes

 ** description **   <a name="awscostmanagement-Type-billing_BusinessSupportServiceSpend-description"></a>
A human-readable description of the service spend entry.
Type: String
Required: No

## See Also
<a name="API_billing_BusinessSupportServiceSpend_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/BusinessSupportServiceSpend)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/BusinessSupportServiceSpend)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/BusinessSupportServiceSpend)
