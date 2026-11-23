---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_BuyerAgreementApprovalPlanInput.html
---

# BuyerAgreementApprovalPlanInput

The approval plan to start an agreement approval for, and an optional note for the approvers.

## Contents
<a name="API_marketplace-agreements_BuyerAgreementApprovalPlanInput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** planReference **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApprovalPlanInput-planReference"></a>
The identifier of the approval plan. Use `GetAgreementRequestApprovalPlans` to retrieve the approval plans of the agreement request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `aplan-[A-Za-z0-9]+`
Required: Yes

 ** requesterNote **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApprovalPlanInput-requesterNote"></a>
An optional note for the approvers, such as the business reason for the purchase (1-1000 characters).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

## See Also
<a name="API_marketplace-agreements_BuyerAgreementApprovalPlanInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/BuyerAgreementApprovalPlanInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/BuyerAgreementApprovalPlanInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/BuyerAgreementApprovalPlanInput)
