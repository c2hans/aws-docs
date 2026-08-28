---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_ConsumableDetails.html
---

# ConsumableDetails
<a name="API_benefits_ConsumableDetails"></a>

Contains information about consumable benefit fulfillment, such as usage quotas or service limits.

## Contents
<a name="API_benefits_ConsumableDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AllocatedAmount **   <a name="AWSPartnerCentral-Type-benefits_ConsumableDetails-AllocatedAmount"></a>
The total amount of the consumable benefit that has been allocated.
Type: [MonetaryValue](API_benefits_MonetaryValue.md) object
Required: No

 ** IssuanceDetails **   <a name="AWSPartnerCentral-Type-benefits_ConsumableDetails-IssuanceDetails"></a>
Detailed information about how the consumable benefit was issued and distributed.
Type: [IssuanceDetail](API_benefits_IssuanceDetail.md) object
Required: No

 ** RemainingAmount **   <a name="AWSPartnerCentral-Type-benefits_ConsumableDetails-RemainingAmount"></a>
The remaining amount of the consumable benefit that is still available for use.
Type: [MonetaryValue](API_benefits_MonetaryValue.md) object
Required: No

 ** UtilizedAmount **   <a name="AWSPartnerCentral-Type-benefits_ConsumableDetails-UtilizedAmount"></a>
The amount of the consumable benefit that has already been used.
Type: [MonetaryValue](API_benefits_MonetaryValue.md) object
Required: No

## See Also
<a name="API_benefits_ConsumableDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/ConsumableDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/ConsumableDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/ConsumableDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
