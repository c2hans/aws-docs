---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AgreementCancellationRequestSummary.html
---

# AgreementCancellationRequestSummary
<a name="API_marketplace-agreements_AgreementCancellationRequestSummary"></a>

Summary view of an agreement cancellation request.

## Contents
<a name="API_marketplace-agreements_AgreementCancellationRequestSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** agreementCancellationRequestId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementCancellationRequestSummary-agreementCancellationRequestId"></a>
The unique identifier of the cancellation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `acr-[a-zA-Z0-9]+`
Required: No

 ** agreementId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementCancellationRequestSummary-agreementId"></a>
The unique identifier of the agreement associated with this cancellation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** agreementType **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementCancellationRequestSummary-agreementType"></a>
The type of agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z]+`
Required: No

 ** catalog **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementCancellationRequestSummary-catalog"></a>
The catalog in which the agreement was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9.-]+`
Required: No

 ** createdAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementCancellationRequestSummary-createdAt"></a>
The date and time when the cancellation request was created.
Type: Timestamp
Required: No

 ** reasonCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementCancellationRequestSummary-reasonCode"></a>
The reason code provided for the cancellation.
Type: String
Valid Values: `INCORRECT_TERMS_ACCEPTED | REPLACING_AGREEMENT | TEST_AGREEMENT | ALTERNATIVE_PROCUREMENT_CHANNEL | PRODUCT_DISCONTINUED | UNINTENDED_RENEWAL | BUYER_DISSATISFACTION | OTHER`
Required: No

 ** status **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementCancellationRequestSummary-status"></a>
The current status of the cancellation request. Possible values include `PENDING_APPROVAL`, `APPROVED`, `REJECTED`, `CANCELLED`, and `VALIDATION_FAILED`.
Type: String
Valid Values: `PENDING_APPROVAL | APPROVED | REJECTED | CANCELLED | VALIDATION_FAILED`
Required: No

 ** updatedAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementCancellationRequestSummary-updatedAt"></a>
The date and time when the cancellation request was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_marketplace-agreements_AgreementCancellationRequestSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/AgreementCancellationRequestSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AgreementCancellationRequestSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/AgreementCancellationRequestSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
