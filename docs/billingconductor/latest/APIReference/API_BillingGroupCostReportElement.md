---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_BillingGroupCostReportElement.html
---

# BillingGroupCostReportElement
<a name="API_BillingGroupCostReportElement"></a>

A summary report of actual AWS charges and calculated AWS charges, based on the associated pricing plan of a billing group.

## Contents
<a name="API_BillingGroupCostReportElement_Contents"></a>

 ** Arn **   <a name="billingconductor-Type-BillingGroupCostReportElement-Arn"></a>
The Amazon Resource Name (ARN) of a billing group.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}`
Required: No

 ** AWSCost **   <a name="billingconductor-Type-BillingGroupCostReportElement-AWSCost"></a>
The actual AWS charges for the billing group.
Type: String
Required: No

 ** Currency **   <a name="billingconductor-Type-BillingGroupCostReportElement-Currency"></a>
The displayed currency.
Type: String
Required: No

 ** Margin **   <a name="billingconductor-Type-BillingGroupCostReportElement-Margin"></a>
The billing group margin.
Type: String
Required: No

 ** MarginPercentage **   <a name="billingconductor-Type-BillingGroupCostReportElement-MarginPercentage"></a>
The percentage of billing group margin.
Type: String
Required: No

 ** ProformaCost **   <a name="billingconductor-Type-BillingGroupCostReportElement-ProformaCost"></a>
The hypothetical AWS charges based on the associated pricing plan of a billing group.
Type: String
Required: No

## See Also
<a name="API_BillingGroupCostReportElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/BillingGroupCostReportElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/BillingGroupCostReportElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/BillingGroupCostReportElement)
