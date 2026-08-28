---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_BillingAdjustmentSummary.html
---

# BillingAdjustmentSummary
<a name="API_marketplace-agreements_BillingAdjustmentSummary"></a>

Summary view of a billing adjustment request.

## Contents
<a name="API_marketplace-agreements_BillingAdjustmentSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** adjustmentAmount **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BillingAdjustmentSummary-adjustmentAmount"></a>
The adjustment amount as a string representation of a decimal number.
Type: String
Pattern: `[0-9]*(\.[0-9]{0,8})?`
Required: Yes

 ** agreementId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BillingAdjustmentSummary-agreementId"></a>
The unique identifier of the agreement associated with this billing adjustment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

 ** agreementType **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BillingAdjustmentSummary-agreementType"></a>
The type of agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z]+`
Required: Yes

 ** billingAdjustmentRequestId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BillingAdjustmentSummary-billingAdjustmentRequestId"></a>
The unique identifier of the billing adjustment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ba-[a-zA-Z0-9]+`
Required: Yes

 ** catalog **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BillingAdjustmentSummary-catalog"></a>
The catalog in which the agreement was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9.-]+`
Required: Yes

 ** createdAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BillingAdjustmentSummary-createdAt"></a>
The date and time when the billing adjustment request was created.
Type: Timestamp
Required: Yes

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BillingAdjustmentSummary-currencyCode"></a>
The currency code for the adjustment amount.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: Yes

 ** originalInvoiceId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BillingAdjustmentSummary-originalInvoiceId"></a>
The identifier of the original invoice being adjusted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** status **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BillingAdjustmentSummary-status"></a>
The current status of the billing adjustment request.
Type: String
Valid Values: `PENDING | VALIDATION_FAILED | COMPLETED`
Required: Yes

 ** updatedAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BillingAdjustmentSummary-updatedAt"></a>
The date and time when the billing adjustment request was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_marketplace-agreements_BillingAdjustmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/BillingAdjustmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/BillingAdjustmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/BillingAdjustmentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
