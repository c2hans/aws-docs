---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AgreementApprovalSummary.html
---

# AgreementApprovalSummary

Summary view of an agreement approval.

## Contents
<a name="API_marketplace-agreements_AgreementApprovalSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** agreementApprovalId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalSummary-agreementApprovalId"></a>
The unique identifier of the agreement approval.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `apr-[A-Za-z0-9]+`
Required: Yes

 ** agreementRequestId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalSummary-agreementRequestId"></a>
The unique identifier of the agreement request that the agreement approval is for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ar-[A-Za-z0-9]+`
Required: Yes

 ** approvalNeededBy **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalSummary-approvalNeededBy"></a>
The date and time by which the agreement approval must be completed.
Type: Timestamp
Required: Yes

 ** approvalType **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalSummary-approvalType"></a>
The type of the agreement approval. The only value is `BUYER_AGREEMENT_APPROVAL`, an approval that the buyer's organization requires before the agreement request can be accepted.
Type: String
Valid Values: `BUYER_AGREEMENT_APPROVAL`
Required: Yes

 ** createdAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalSummary-createdAt"></a>
The date and time when the agreement approval was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalSummary-name"></a>
The descriptive name of the agreement approval.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(.)+`
Required: Yes

 ** status **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalSummary-status"></a>
The current status of the agreement approval. Possible values include `PENDING_APPROVAL`, `APPROVED`, `REJECTED`, `EXPIRED`, and `CANCELLED`.
Type: String
Valid Values: `PENDING_APPROVAL | APPROVED | REJECTED | EXPIRED | CANCELLED`
Required: Yes

 ** updatedAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalSummary-updatedAt"></a>
The date and time when the agreement approval was last updated.
Type: Timestamp
Required: Yes

 ** expiresAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalSummary-expiresAt"></a>
The date and time when the agreement approval expires if it isn't approved or rejected.
Type: Timestamp
Required: No

 ** startedAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalSummary-startedAt"></a>
The date and time when approvers could start acting on the agreement approval.
Type: Timestamp
Required: No

## See Also
<a name="API_marketplace-agreements_AgreementApprovalSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/AgreementApprovalSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AgreementApprovalSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/AgreementApprovalSummary)
