---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_BatchCreateBillingAdjustmentRequestEntry.html
---

# BatchCreateBillingAdjustmentRequestEntry
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentRequestEntry"></a>

An individual entry in a batch billing adjustment request, specifying the invoice and adjustment details.

## Contents
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentRequestEntry_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** adjustmentAmount **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BatchCreateBillingAdjustmentRequestEntry-adjustmentAmount"></a>
The adjustment amount as a string representation of a decimal number in the currency of the invoice.
Type: String
Pattern: `[0-9]*(\.[0-9]{0,8})?`
Required: Yes

 ** adjustmentReasonCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BatchCreateBillingAdjustmentRequestEntry-adjustmentReasonCode"></a>
The reason code for the billing adjustment.
Type: String
Valid Values: `INCORRECT_TERMS_ACCEPTED | INCORRECT_METERING | TEST_ENVIRONMENT_CHARGES | ALTERNATIVE_PROCUREMENT_CHANNEL | UNINTENDED_RENEWAL | BUYER_DISSATISFACTION | OTHER`
Required: Yes

 ** agreementId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BatchCreateBillingAdjustmentRequestEntry-agreementId"></a>
The unique identifier of the agreement associated with the invoice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

 ** clientToken **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BatchCreateBillingAdjustmentRequestEntry-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BatchCreateBillingAdjustmentRequestEntry-currencyCode"></a>
The 3-letter ISO 4217 currency code for the adjustment amount. Must match the currency code of the offer associated with the agreement (e.g., `USD`).
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: Yes

 ** originalInvoiceId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BatchCreateBillingAdjustmentRequestEntry-originalInvoiceId"></a>
The identifier of the original invoice to adjust.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** description **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BatchCreateBillingAdjustmentRequestEntry-description"></a>
An optional detailed description of the adjustment reason.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## See Also
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentRequestEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
