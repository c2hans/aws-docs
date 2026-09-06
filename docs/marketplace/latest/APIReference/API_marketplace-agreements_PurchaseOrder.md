---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_PurchaseOrder.html
---

# PurchaseOrder
<a name="API_marketplace-agreements_PurchaseOrder"></a>

Contains information about a purchase order association to a charge within an agreement.

## Contents
<a name="API_marketplace-agreements_PurchaseOrder_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** chargeId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PurchaseOrder-chargeId"></a>
The unique identifier of the charge to associate the purchase order with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

 ** agreementId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PurchaseOrder-agreementId"></a>
The unique identifier of the agreement associated with this charge.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** chargeRevision **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PurchaseOrder-chargeRevision"></a>
The revision of the charge.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** purchaseOrderReference **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PurchaseOrder-purchaseOrderReference"></a>
The purchase order reference to associate with the charge.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_marketplace-agreements_PurchaseOrder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/PurchaseOrder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/PurchaseOrder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/PurchaseOrder)
