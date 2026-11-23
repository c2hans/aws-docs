---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AgreementApprovalProposalSummary.html
---

# AgreementApprovalProposalSummary

A summary of the proposal received from the proposer.

## Contents
<a name="API_marketplace-agreements_AgreementApprovalProposalSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** offerId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalProposalSummary-offerId"></a>
The unique identifier of the offer in AWS Marketplace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\S{1,64}`
Required: Yes

 ** visibilityScope **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalProposalSummary-visibilityScope"></a>
The visibility of the offer. Valid values are `PUBLIC` and `PRIVATE`.
Type: String
Valid Values: `PUBLIC | PRIVATE`
Required: Yes

 ** offerSetId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalProposalSummary-offerSetId"></a>
A unique identifier for the offer set containing this offer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `\S{1,50}`
Required: No

 ** resources **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalProposalSummary-resources"></a>
The list of resources involved in the agreement.
Type: Array of [AgreementApprovalResource](API_marketplace-agreements_AgreementApprovalResource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## See Also
<a name="API_marketplace-agreements_AgreementApprovalProposalSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/AgreementApprovalProposalSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AgreementApprovalProposalSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/AgreementApprovalProposalSummary)
