---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BusinessSupportDiscount.html
---

# BusinessSupportDiscount
<a name="API_billing_BusinessSupportDiscount"></a>

A discount applied to a Business Support account charge, including the discount amount, percentage, type, and source.

## Contents
<a name="API_billing_BusinessSupportDiscount_Contents"></a>

 ** discountAmount **   <a name="awscostmanagement-Type-billing_BusinessSupportDiscount-discountAmount"></a>
The discount amount applied to the Business Support charge. This value is negative, representing a reduction in the charge.
Type: String
Required: No

 ** discountPercentage **   <a name="awscostmanagement-Type-billing_BusinessSupportDiscount-discountPercentage"></a>
The discount percentage applied to the Business Support charge, expressed as a decimal (for example, `0.12` for a 12% discount).
Type: String
Required: No

 ** discountSource **   <a name="awscostmanagement-Type-billing_BusinessSupportDiscount-discountSource"></a>
The source or program through which the discount was applied.
Type: String
Required: No

 ** discountType **   <a name="awscostmanagement-Type-billing_BusinessSupportDiscount-discountType"></a>
The type of discount applied. Valid values: `Distributor_Discount` (a discount applied through a distributor arrangement), `SPP_Discount` (a discount applied through the Solution Provider Program).
Type: String
Required: No

## See Also
<a name="API_billing_BusinessSupportDiscount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/BusinessSupportDiscount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/BusinessSupportDiscount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/BusinessSupportDiscount)
