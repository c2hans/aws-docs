---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_BuyerAgreementApproval.html
---

# BuyerAgreementApproval

The details of an approval that the buyer's organization requires before the agreement request can be accepted, including the approval levels and the decision of each approver.

## Contents
<a name="API_marketplace-agreements_BuyerAgreementApproval_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** agreementApprovalId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApproval-agreementApprovalId"></a>
The unique identifier of the agreement approval.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `apr-[A-Za-z0-9]+`
Required: Yes

 ** agreementRequestId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApproval-agreementRequestId"></a>
The unique identifier of the agreement request that the agreement approval is for. Use `GetAgreementRequest` to retrieve the agreement request details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ar-[A-Za-z0-9]+`
Required: Yes

 ** approvalNeededBy **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApproval-approvalNeededBy"></a>
The date and time by which the agreement approval must be completed.
Type: Timestamp
Required: Yes

 ** approvalType **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApproval-approvalType"></a>
The type of the agreement approval, which is `BUYER_AGREEMENT_APPROVAL`.
Type: String
Valid Values: `BUYER_AGREEMENT_APPROVAL`
Required: Yes

 ** createdAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApproval-createdAt"></a>
The date and time when the agreement approval was created.
Type: Timestamp
Required: Yes

 ** levels **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApproval-levels"></a>
The approval levels, in the order they are evaluated. Approvers at a level can act only after the previous level is approved. Each level lists its approvers and the decision of each one.
Type: Array of [BuyerAgreementApprovalLevel](API_marketplace-agreements_BuyerAgreementApprovalLevel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Required: Yes

 ** name **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApproval-name"></a>
The descriptive name of the agreement approval.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(.)+`
Required: Yes

 ** planInput **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApproval-planInput"></a>
The approval plan and the note that the requester provided in `StartAgreementApprovals`.
Type: [BuyerAgreementApprovalPlanInput](API_marketplace-agreements_BuyerAgreementApprovalPlanInput.md) object
Required: Yes

 ** proposalSummary **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApproval-proposalSummary"></a>
A summary of the proposal received from the proposer.
Type: [AgreementApprovalProposalSummary](API_marketplace-agreements_AgreementApprovalProposalSummary.md) object
Required: Yes

 ** proposer **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApproval-proposer"></a>
The details of the party proposing the agreement terms. This is commonly the seller for `PurchaseAgreement`.
Type: [AgreementApprovalProposer](API_marketplace-agreements_AgreementApprovalProposer.md) object
Required: Yes

 ** requester **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApproval-requester"></a>
The account that started the agreement approval.
Type: [AgreementApprovalRequester](API_marketplace-agreements_AgreementApprovalRequester.md) object
Required: Yes

 ** status **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApproval-status"></a>
The current status of the agreement approval. Possible values include `PENDING_APPROVAL`, `APPROVED`, `REJECTED`, `EXPIRED`, and `CANCELLED`.
Type: String
Valid Values: `PENDING_APPROVAL | APPROVED | REJECTED | EXPIRED | CANCELLED`
Required: Yes

 ** updatedAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApproval-updatedAt"></a>
The date and time when the agreement approval was last updated.
Type: Timestamp
Required: Yes

 ** expiresAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApproval-expiresAt"></a>
The date and time when the agreement approval expires if it isn't approved or rejected.
Type: Timestamp
Required: No

 ** startedAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApproval-startedAt"></a>
The date and time when approvers could start acting on the agreement approval.
Type: Timestamp
Required: No

## See Also
<a name="API_marketplace-agreements_BuyerAgreementApproval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/BuyerAgreementApproval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/BuyerAgreementApproval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/BuyerAgreementApproval)
