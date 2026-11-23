---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AgreementRequestSummary.html
---

# AgreementRequestSummary

Summary view of an agreement request.

## Contents
<a name="API_marketplace-agreements_AgreementRequestSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** agreementId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementRequestSummary-agreementId"></a>
The unique identifier of the agreement that the agreement request is for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** agreementRequestId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementRequestSummary-agreementRequestId"></a>
The unique identifier of the agreement request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ar-[A-Za-z0-9]+`
Required: No

 ** agreementType **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementRequestSummary-agreementType"></a>
The type of agreement (for example, `PurchaseAgreement`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z]+`
Required: No

 ** proposalSummary **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementRequestSummary-proposalSummary"></a>
A summary of the proposal received from the proposer.
Type: [ProposalSummary](API_marketplace-agreements_ProposalSummary.md) object
Required: No

 ** status **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementRequestSummary-status"></a>
The current status of the agreement request. Possible values include `DRAFT`, `PENDING_APPROVAL`, `APPROVED`, `ACCEPTED`, `REJECTED`, and `CANCELLED`.
Type: String
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | ACCEPTED | REJECTED | CANCELLED`
Required: No

## See Also
<a name="API_marketplace-agreements_AgreementRequestSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/AgreementRequestSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AgreementRequestSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/AgreementRequestSummary)
