---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AgreementApprovalPurchaseOrder.html
---

# AgreementApprovalPurchaseOrder

A purchase order reference for a charge on the agreement request.

## Contents
<a name="API_marketplace-agreements_AgreementApprovalPurchaseOrder_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** chargeId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalPurchaseOrder-chargeId"></a>
The unique identifier of the charge to associate the purchase order with. Use `GetAgreementRequest` to retrieve the charges of the agreement request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ch-[a-zA-Z0-9]+`
Required: Yes

 ** purchaseOrderReference **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementApprovalPurchaseOrder-purchaseOrderReference"></a>
The purchase order reference to associate with the charge.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_marketplace-agreements_AgreementApprovalPurchaseOrder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/AgreementApprovalPurchaseOrder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AgreementApprovalPurchaseOrder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/AgreementApprovalPurchaseOrder)
