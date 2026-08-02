---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CustomLineItemVersionListElement.html
---

# CustomLineItemVersionListElement
<a name="API_CustomLineItemVersionListElement"></a>

A representation of a custom line item version.

## Contents
<a name="API_CustomLineItemVersionListElement_Contents"></a>

 ** AccountId **   <a name="billingconductor-Type-CustomLineItemVersionListElement-AccountId"></a>
The AWS account in which this custom line item will be applied to.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** Arn **   <a name="billingconductor-Type-CustomLineItemVersionListElement-Arn"></a>
 A list of custom line item Amazon Resource Names (ARNs) to retrieve information.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:customlineitem/)?[a-zA-Z0-9]{10}`
Required: No

 ** AssociationSize **   <a name="billingconductor-Type-CustomLineItemVersionListElement-AssociationSize"></a>
The number of resources that are associated with the custom line item.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** BillingGroupArn **   <a name="billingconductor-Type-CustomLineItemVersionListElement-BillingGroupArn"></a>
The Amazon Resource Name (ARN) of the billing group that the custom line item applies to.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}`
Required: No

 ** ChargeDetails **   <a name="billingconductor-Type-CustomLineItemVersionListElement-ChargeDetails"></a>
 A representation of the charge details of a custom line item.
Type: [ListCustomLineItemChargeDetails](API_ListCustomLineItemChargeDetails.md) object
Required: No

 ** ComputationRule **   <a name="billingconductor-Type-CustomLineItemVersionListElement-ComputationRule"></a>
 The computation rule for a specific version of a custom line item, determining how charges are computed and reflected in the bill.
Type: String
Valid Values: `ITEMIZED | CONSOLIDATED`
Required: No

 ** CreationTime **   <a name="billingconductor-Type-CustomLineItemVersionListElement-CreationTime"></a>
The time when the custom line item version was created.
Type: Long
Required: No

 ** CurrencyCode **   <a name="billingconductor-Type-CustomLineItemVersionListElement-CurrencyCode"></a>
The charge value currency of the custom line item.
Type: String
Valid Values: `USD | CNY`
Required: No

 ** Description **   <a name="billingconductor-Type-CustomLineItemVersionListElement-Description"></a>
The description of the custom line item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** EndBillingPeriod **   <a name="billingconductor-Type-CustomLineItemVersionListElement-EndBillingPeriod"></a>
The end billing period of the custom line item version.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`
Required: No

 ** LastModifiedTime **   <a name="billingconductor-Type-CustomLineItemVersionListElement-LastModifiedTime"></a>
The most recent time that the custom line item version was modified.
Type: Long
Required: No

 ** Name **   <a name="billingconductor-Type-CustomLineItemVersionListElement-Name"></a>
The name of the custom line item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@]+`
Required: No

 ** PresentationDetails **   <a name="billingconductor-Type-CustomLineItemVersionListElement-PresentationDetails"></a>
 Presentation configuration for a specific version of a custom line item, specifying how charges are displayed in the bill.
Type: [PresentationObject](API_PresentationObject.md) object
Required: No

 ** ProductCode **   <a name="billingconductor-Type-CustomLineItemVersionListElement-ProductCode"></a>
The product code that’s associated with the custom line item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 29.
Required: No

 ** StartBillingPeriod **   <a name="billingconductor-Type-CustomLineItemVersionListElement-StartBillingPeriod"></a>
The start billing period of the custom line item version.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`
Required: No

 ** StartTime **   <a name="billingconductor-Type-CustomLineItemVersionListElement-StartTime"></a>
 The inclusive start time.
Type: Long
Required: No

## See Also
<a name="API_CustomLineItemVersionListElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/CustomLineItemVersionListElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/CustomLineItemVersionListElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/CustomLineItemVersionListElement)
