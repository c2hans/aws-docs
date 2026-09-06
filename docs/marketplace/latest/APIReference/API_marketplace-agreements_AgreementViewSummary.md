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

 ** endTimeBehaviorReasonCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementViewSummary-endTimeBehaviorReasonCode"></a>
The reason why the agreement doesn't renew at its end date. The field is `null` when the agreement renews.
More than one reason can apply to the same agreement. When that happens, the operation returns only one reason code, and `PROPOSER_RENEW_OPTED_OUT` takes precedence over all others.
The `EnableAutoRenew` field reflects only the acceptor's preference, and doesn't reflect the other reasons an agreement might not renew.
Reason codes include:
+  `PROPOSER_RENEW_OPTED_OUT` – The proposer opted out of renewing the agreement.
+  `ACCEPTOR_RENEW_OPTED_OUT` – The acceptor opted out of renewing the agreement.
+  `NO_RENEWAL_TERM` – The accepted terms of the agreement don't include a renewal term, which is required for an agreement to renew.
+  `RENEWAL_LIMIT_EXHAUSTED` – The agreement reached the maximum number of renewals allowed by its renewal term.
Type: String
Valid Values: `PROPOSER_RENEW_OPTED_OUT | ACCEPTOR_RENEW_OPTED_OUT | NO_RENEWAL_TERM | RENEWAL_LIMIT_EXHAUSTED`
Required: No

 ** endTimeBehaviorType **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementViewSummary-endTimeBehaviorType"></a>
The behavior of the agreement when it reaches its end date. The field is `null` for agreements that have no end date, because those agreements never reach an end time.
Types include:
+  `RENEW` – A new agreement is created from the accepted terms of this agreement.
+  `REPLACE` – A new agreement is created from a different offer than the one this agreement was created from. This happens, for example, when a private offer reaches its end date and the acceptor transitions to the public offer for the product.
+  `EXPIRE` – The agreement ends and isn't renewed or replaced.
Type: String
Valid Values: `RENEW | REPLACE | EXPIRE`
Required: No

 ** entitlements **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementViewSummary-entitlements"></a>
A list of entitlements associated with the agreement.
Type: Array of [Entitlement](API_marketplace-agreements_Entitlement.md) objects
Required: No

 ** initialAgreementId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementViewSummary-initialAgreementId"></a>
The unique identifier of the very first agreement in a chain of related agreements, such as renewals or replacements. It stays the same across all agreements in that chain, which lets you trace an agreement back to the original. You can also use it as the `InitialAgreementId` filter value to return every agreement in the same chain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** lastUpdateTime **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementViewSummary-lastUpdateTime"></a>
The date and time when the agreement was last updated. An agreement is updated when any of its attributes or accepted terms change. Amendments, renewals, and a party changing whether the agreement renews are all examples.
Use the `BeforeLastUpdateTime` and `AfterLastUpdateTime` filters to search on this value, and `LastUpdateTime` as the `SortBy` value to sort by it. Sorting by `LastUpdateTime` is supported only when `PartyType` is `Proposer`.
Type: Timestamp
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
