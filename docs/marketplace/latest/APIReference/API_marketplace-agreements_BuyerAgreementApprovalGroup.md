---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_BuyerAgreementApprovalGroup.html
---

# BuyerAgreementApprovalGroup

A group of approvers, the number of approvals the group requires, and the decision of each approver.

## Contents
<a name="API_marketplace-agreements_BuyerAgreementApprovalGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** approvalCriteria **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApprovalGroup-approvalCriteria"></a>
The number of approvers in the group who must approve.
Type: [BuyerAgreementApprovalCriteria](API_marketplace-agreements_BuyerAgreementApprovalCriteria.md) object
Required: Yes

 ** approvers **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BuyerAgreementApprovalGroup-approvers"></a>
The approvers in the group and the decision of each one.
Type: Array of [ApproverOutcome](API_marketplace-agreements_ApproverOutcome.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_marketplace-agreements_BuyerAgreementApprovalGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/BuyerAgreementApprovalGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/BuyerAgreementApprovalGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/BuyerAgreementApprovalGroup)
