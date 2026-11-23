---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_BuyerAgreementApprovalRejectionInput.html
---

# BuyerAgreementApprovalRejectionInput

The rejection decision for an agreement approval.

## Contents
<a name="API_marketplace-agreements_BuyerAgreementApprovalRejectionInput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** agreementApprovalId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApprovalRejectionInput-agreementApprovalId"></a>
The unique identifier of the agreement approval to reject.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `apr-[A-Za-z0-9]+`
Required: Yes

 ** note **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApprovalRejectionInput-note"></a>
The reason for the rejection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** approverOutcomeIdToOverride **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApprovalRejectionInput-approverOutcomeIdToOverride"></a>
The `approverOutcomeId` of the approver to decide on behalf of. You must be the management account or a delegated administrator of your AWS organization to set this field. Use `GetAgreementApproval` to retrieve the `approverOutcomeId` of each approver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `aprout-[A-Za-z0-9-]+`
Required: No

## See Also
<a name="API_marketplace-agreements_BuyerAgreementApprovalRejectionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/BuyerAgreementApprovalRejectionInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/BuyerAgreementApprovalRejectionInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/BuyerAgreementApprovalRejectionInput)
