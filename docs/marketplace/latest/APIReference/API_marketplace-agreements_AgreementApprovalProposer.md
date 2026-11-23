---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AgreementApprovalProposer.html
---

# AgreementApprovalProposer

Details of the party proposing the agreement terms. This is commonly the seller for `PurchaseAgreement`.

## Contents
<a name="API_marketplace-agreements_AgreementApprovalProposer_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** accountId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalProposer-accountId"></a>
The AWS account ID of the proposer.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: Yes

 ** legalName **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalProposer-legalName"></a>
The legal name of the proposer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^\p{C}]+`
Required: Yes

## See Also
<a name="API_marketplace-agreements_AgreementApprovalProposer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/AgreementApprovalProposer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AgreementApprovalProposer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/AgreementApprovalProposer)
