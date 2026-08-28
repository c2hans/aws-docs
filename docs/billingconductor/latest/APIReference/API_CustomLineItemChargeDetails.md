---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CustomLineItemChargeDetails.html
---

# CustomLineItemChargeDetails
<a name="API_CustomLineItemChargeDetails"></a>

The charge details of a custom line item. It should contain only one of `Flat` or `Percentage`.

## Contents
<a name="API_CustomLineItemChargeDetails_Contents"></a>

 ** Type **   <a name="billingconductor-Type-CustomLineItemChargeDetails-Type"></a>
The type of the custom line item that indicates whether the charge is a fee or credit.
Type: String
Valid Values: `CREDIT | FEE`
Required: Yes

 ** Flat **   <a name="billingconductor-Type-CustomLineItemChargeDetails-Flat"></a>
A `CustomLineItemFlatChargeDetails` that describes the charge details of a flat custom line item.
Type: [CustomLineItemFlatChargeDetails](API_CustomLineItemFlatChargeDetails.md) object
Required: No

 ** LineItemFilters **   <a name="billingconductor-Type-CustomLineItemChargeDetails-LineItemFilters"></a>
A representation of the line item filter.
Type: Array of [LineItemFilter](API_LineItemFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** Percentage **   <a name="billingconductor-Type-CustomLineItemChargeDetails-Percentage"></a>
A `CustomLineItemPercentageChargeDetails` that describes the charge details of a percentage custom line item.
Type: [CustomLineItemPercentageChargeDetails](API_CustomLineItemPercentageChargeDetails.md) object
Required: No

## See Also
<a name="API_CustomLineItemChargeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/CustomLineItemChargeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/CustomLineItemChargeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/CustomLineItemChargeDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
