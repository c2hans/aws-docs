---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_PaymentRequestSummary.html
---

# PaymentRequestSummary
<a name="API_marketplace-agreements_PaymentRequestSummary"></a>

Summary view of a payment request.

## Contents
<a name="API_marketplace-agreements_PaymentRequestSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** agreementId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentRequestSummary-agreementId"></a>
The unique identifier of the agreement associated with this payment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** chargeAmount **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentRequestSummary-chargeAmount"></a>
The amount charged or to be charged to the buyer.
Type: String
Pattern: `[0-9]*(\.[0-9]{0,8})?`
Required: No

 ** chargeId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentRequestSummary-chargeId"></a>
The unique identifier of the charge created after the payment request is approved. This field is only present for approved payment requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ch-[a-zA-Z0-9]+`
Required: No

 ** createdAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentRequestSummary-createdAt"></a>
The date and time when the payment request was created.
Type: Timestamp
Required: No

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentRequestSummary-currencyCode"></a>
The currency code for the charge amount.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: No

 ** name **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentRequestSummary-name"></a>
The descriptive name of the payment request.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 64.
Pattern: `.+`
Required: No

 ** paymentRequestId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentRequestSummary-paymentRequestId"></a>
The unique identifier of the payment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `pr-[a-zA-Z0-9]+`
Required: No

 ** status **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentRequestSummary-status"></a>
The current status of the payment request. Possible values include `VALIDATING`, `VALIDATION_FAILED`, `PENDING_APPROVAL`, `APPROVED`, `REJECTED`, and `CANCELLED`.
Type: String
Valid Values: `VALIDATING | VALIDATION_FAILED | PENDING_APPROVAL | APPROVED | REJECTED | CANCELLED`
Required: No

 ** updatedAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentRequestSummary-updatedAt"></a>
The date and time when the payment request was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_marketplace-agreements_PaymentRequestSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/PaymentRequestSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/PaymentRequestSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/PaymentRequestSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
