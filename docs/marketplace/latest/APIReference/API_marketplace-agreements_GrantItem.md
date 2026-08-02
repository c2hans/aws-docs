---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_GrantItem.html
---

# GrantItem
<a name="API_marketplace-agreements_GrantItem"></a>

Entitlements granted to the acceptor of fixed upfront as part of agreement execution.

## Contents
<a name="API_marketplace-agreements_GrantItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** dimensionKey **   <a name="AWSMarketplaceService-Type-marketplace-agreements_GrantItem-dimensionKey"></a>
Unique dimension key defined in the product document. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** maxQuantity **   <a name="AWSMarketplaceService-Type-marketplace-agreements_GrantItem-maxQuantity"></a>
Maximum amount of capacity that the buyer can be entitled to the given dimension of the product. If `MaxQuantity` is not provided, the buyer will be able to use an unlimited amount of the given dimension.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_marketplace-agreements_GrantItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/GrantItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GrantItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/GrantItem)
