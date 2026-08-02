---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AgreementViewSummary.html
---

# AgreementViewSummary
<a name="API_marketplace-agreements_AgreementViewSummary"></a>

A summary of the agreement, including top-level attributes (for example, the agreement ID, proposer, and acceptor).

## Contents
<a name="API_marketplace-agreements_AgreementViewSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** acceptanceTime **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementViewSummary-acceptanceTime"></a>
The date and time that the agreement was accepted.
Type: Timestamp
Required: No

 ** acceptor **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementViewSummary-acceptor"></a>
Details of the party accepting the agreement terms. This is commonly the buyer for `PurchaseAgreement.`
Type: [Acceptor](API_marketplace-agreements_Acceptor.md) object
Required: No

 ** agreementId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementViewSummary-agreementId"></a>
The unique identifier of the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** agreementType **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementViewSummary-agreementType"></a>
The type of agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z]+`
Required: No

 ** endTime **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementViewSummary-endTime"></a>
The date and time when the agreement ends. The field is `null` for pay-as-you-go agreements, which don’t have end dates.
Type: Timestamp
Required: No

 ** entitlements **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementViewSummary-entitlements"></a>
A list of entitlements associated with the agreement.
Type: Array of [Entitlement](API_marketplace-agreements_Entitlement.md) objects
Required: No

 ** proposalSummary **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementViewSummary-proposalSummary"></a>
A summary of the proposal
Type: [ProposalSummary](API_marketplace-agreements_ProposalSummary.md) object
Required: No

 ** proposer **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementViewSummary-proposer"></a>
Details of the party proposing the agreement terms, most commonly the seller for `PurchaseAgreement`.
Type: [Proposer](API_marketplace-agreements_Proposer.md) object
Required: No

 ** startTime **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementViewSummary-startTime"></a>
The date and time when the agreement starts.
Type: Timestamp
Required: No

 ** status **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementViewSummary-status"></a>
The current status of the agreement.
Type: String
Valid Values: `ACTIVE | ARCHIVED | CANCELLED | EXPIRED | RENEWED | REPLACED | ROLLED_BACK | SUPERSEDED | TERMINATED`
Required: No

## See Also
<a name="API_marketplace-agreements_AgreementViewSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/AgreementViewSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AgreementViewSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/AgreementViewSummary)
