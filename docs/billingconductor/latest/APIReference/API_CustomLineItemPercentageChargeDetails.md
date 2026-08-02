---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CustomLineItemPercentageChargeDetails.html
---

# CustomLineItemPercentageChargeDetails
<a name="API_CustomLineItemPercentageChargeDetails"></a>

A representation of the charge details that are associated with a percentage custom line item.

## Contents
<a name="API_CustomLineItemPercentageChargeDetails_Contents"></a>

 ** PercentageValue **   <a name="billingconductor-Type-CustomLineItemPercentageChargeDetails-PercentageValue"></a>
The custom line item's percentage value. This will be multiplied against the combined value of its associated resources to determine its charge value.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: Yes

 ** AssociatedValues **   <a name="billingconductor-Type-CustomLineItemPercentageChargeDetails-AssociatedValues"></a>
A list of resource ARNs to associate to the percentage custom line item.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:(customlineitem|billinggroup)/)?[a-zA-Z0-9]{10,12}`
Required: No

## See Also
<a name="API_CustomLineItemPercentageChargeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/CustomLineItemPercentageChargeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/CustomLineItemPercentageChargeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/CustomLineItemPercentageChargeDetails)
