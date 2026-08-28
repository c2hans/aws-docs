---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CustomLineItemListElement.html
---

# CustomLineItemListElement
<a name="API_CustomLineItemListElement"></a>

A representation of a custom line item.

## Contents
<a name="API_CustomLineItemListElement_Contents"></a>

 ** AccountId **   <a name="billingconductor-Type-CustomLineItemListElement-AccountId"></a>
The AWS account in which this custom line item will be applied to.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** Arn **   <a name="billingconductor-Type-CustomLineItemListElement-Arn"></a>
The Amazon Resource Names (ARNs) for custom line items.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:customlineitem/)?[a-zA-Z0-9]{10}`
Required: No

 ** AssociationSize **   <a name="billingconductor-Type-CustomLineItemListElement-AssociationSize"></a>
The number of resources that are associated to the custom line item.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** BillingGroupArn **   <a name="billingconductor-Type-CustomLineItemListElement-BillingGroupArn"></a>
The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}`
Required: No

 ** ChargeDetails **   <a name="billingconductor-Type-CustomLineItemListElement-ChargeDetails"></a>
A `ListCustomLineItemChargeDetails` that describes the charge details of a custom line item.
Type: [ListCustomLineItemChargeDetails](API_ListCustomLineItemChargeDetails.md) object
Required: No

 ** ComputationRule **   <a name="billingconductor-Type-CustomLineItemListElement-ComputationRule"></a>
 The computation rule that determines how the custom line item charges are computed and reflected in the bill.
Type: String
Valid Values: `ITEMIZED | CONSOLIDATED`
Required: No

 ** CreationTime **   <a name="billingconductor-Type-CustomLineItemListElement-CreationTime"></a>
The time created.
Type: Long
Required: No

 ** CurrencyCode **   <a name="billingconductor-Type-CustomLineItemListElement-CurrencyCode"></a>
The custom line item's charge value currency. Only one of the valid values can be used.
Type: String
Valid Values: `USD | CNY`
Required: No

 ** Description **   <a name="billingconductor-Type-CustomLineItemListElement-Description"></a>
The custom line item's description. This is shown on the Bills page in association with the charge value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** LastModifiedTime **   <a name="billingconductor-Type-CustomLineItemListElement-LastModifiedTime"></a>
The most recent time when the custom line item was modified.
Type: Long
Required: No

 ** Name **   <a name="billingconductor-Type-CustomLineItemListElement-Name"></a>
The custom line item's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@]+`
Required: No

 ** PresentationDetails **   <a name="billingconductor-Type-CustomLineItemListElement-PresentationDetails"></a>
 Configuration details specifying how the custom line item charges are presented, including which service the charges are shown under.
Type: [PresentationObject](API_PresentationObject.md) object
Required: No

 ** ProductCode **   <a name="billingconductor-Type-CustomLineItemListElement-ProductCode"></a>
The product code that's associated with the custom line item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 29.
Required: No

## See Also
<a name="API_CustomLineItemListElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/CustomLineItemListElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/CustomLineItemListElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/CustomLineItemListElement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
