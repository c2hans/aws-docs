---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ChargeSummary.html
---

# ChargeSummary
<a name="API_marketplace-agreements_ChargeSummary"></a>

The `ChargeSummary` provides a detailed breakdown of charges that are associated with an agreement request. This is applicable only when a request is created for a `PurchaseAgreement`.

**Note**
Tax and invoicing fields (such as `estimatedTaxes`, `amountAfterTax`, `newAgreementValueAfterTax`, and `invoicingEntity`) are returned on a best-effort basis and do not cause the request to fail if unavailable.
A `null` tax amount can have two meanings:
Tax estimation was unavailable at the time of the request.
The charge timing is `BILLING_PERIOD`, so the charge amount is not determined at request time. In this case, the tax breakdown may still include the tax `rate` and `type`.

## Contents
<a name="API_marketplace-agreements_ChargeSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ChargeSummary-currencyCode"></a>
The three-letter currency code for all charges (e.g., USD).
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: No

 ** estimatedTaxes **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ChargeSummary-estimatedTaxes"></a>
Provides an aggregated view of estimated tax information for the agreement.
Type: [EstimatedTaxes](API_marketplace-agreements_EstimatedTaxes.md) object
Required: No

 ** expectedCharges **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ChargeSummary-expectedCharges"></a>
A list of expected charges for the agreement request.
Type: Array of [ExpectedCharge](API_marketplace-agreements_ExpectedCharge.md) objects
Required: No

 ** invoicingEntity **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ChargeSummary-invoicingEntity"></a>
The entity responsible for issuing the invoice.
Type: [InvoicingEntity](API_marketplace-agreements_InvoicingEntity.md) object
Required: No

 ** itemizedCharges **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ChargeSummary-itemizedCharges"></a>
An itemized list of charges for the agreement request.
Type: Array of [ItemizedCharge](API_marketplace-agreements_ItemizedCharge.md) objects
Required: No

 ** newAgreementValue **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ChargeSummary-newAgreementValue"></a>
The total value of the agreement, which includes any amendments.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** newAgreementValueAfterTax **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ChargeSummary-newAgreementValueAfterTax"></a>
Expected new agreement value after estimated taxes are applied.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

## See Also
<a name="API_marketplace-agreements_ChargeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ChargeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ChargeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ChargeSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
