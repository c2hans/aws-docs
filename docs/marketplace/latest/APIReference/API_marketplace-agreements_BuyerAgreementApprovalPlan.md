---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_BuyerAgreementApprovalPlan.html
---

# BuyerAgreementApprovalPlan

An approval plan that the buyer's organization requires, with its approval levels and the approvers at each level.

## Contents
<a name="API_marketplace-agreements_BuyerAgreementApprovalPlan_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** levels **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApprovalPlan-levels"></a>
The approval levels of the plan, in the order they are evaluated. Approvers at a level can act only after the previous level is approved.
Type: Array of [BuyerAgreementApprovalPlanLevel](API_marketplace-agreements_BuyerAgreementApprovalPlanLevel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Required: Yes

 ** planReference **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApprovalPlan-planReference"></a>
The identifier of the approval plan. Pass it in `StartAgreementApprovals` to start an agreement approval for this plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `aplan-[A-Za-z0-9]+`
Required: Yes

 ** name **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApprovalPlan-name"></a>
The name of the approval plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(.)+`
Required: No

## See Also
<a name="API_marketplace-agreements_BuyerAgreementApprovalPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/BuyerAgreementApprovalPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/BuyerAgreementApprovalPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/BuyerAgreementApprovalPlan)
