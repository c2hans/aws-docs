---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_FulfillmentDetails.html
---

# FulfillmentDetails
<a name="API_benefits_FulfillmentDetails"></a>

Contains comprehensive information about how a benefit allocation is fulfilled across different fulfillment types.

## Contents
<a name="API_benefits_FulfillmentDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AccessDetails **   <a name="AWSPartnerCentral-Type-benefits_FulfillmentDetails-AccessDetails"></a>
Details about access-based fulfillment, if applicable to this benefit allocation.
Type: [AccessDetails](API_benefits_AccessDetails.md) object
Required: No

 ** ConsumableDetails **   <a name="AWSPartnerCentral-Type-benefits_FulfillmentDetails-ConsumableDetails"></a>
Details about consumable-based fulfillment, if applicable to this benefit allocation.
Type: [ConsumableDetails](API_benefits_ConsumableDetails.md) object
Required: No

 ** CreditDetails **   <a name="AWSPartnerCentral-Type-benefits_FulfillmentDetails-CreditDetails"></a>
Details about credit-based fulfillment, if applicable to this benefit allocation.
Type: [CreditDetails](API_benefits_CreditDetails.md) object
Required: No

 ** DisbursementDetails **   <a name="AWSPartnerCentral-Type-benefits_FulfillmentDetails-DisbursementDetails"></a>
Details about disbursement-based fulfillment, if applicable to this benefit allocation.
Type: [DisbursementDetails](API_benefits_DisbursementDetails.md) object
Required: No

## See Also
<a name="API_benefits_FulfillmentDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/FulfillmentDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/FulfillmentDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/FulfillmentDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
