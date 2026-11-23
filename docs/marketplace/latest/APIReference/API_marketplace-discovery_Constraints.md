---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_Constraints.html
---

# Constraints

Constraints that control how you can configure a rate card.

## Contents
<a name="API_marketplace-discovery_Constraints_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** multipleDimensionSelection **   <a name="AWSMarketplaceService-Type-marketplace-discovery_Constraints-multipleDimensionSelection"></a>
Specifies whether you can select multiple dimensions. This field has one of the following values:
Allowed
You can select more than one dimension.
Disallowed
You can select only one dimension.
Type: String
Valid Values: `Allowed | Disallowed`
Required: Yes

 ** quantityConfiguration **   <a name="AWSMarketplaceService-Type-marketplace-discovery_Constraints-quantityConfiguration"></a>
Specifies whether you can configure quantities. This field has one of the following values:
Allowed
You can set the quantity of each dimension.
Disallowed
You cannot change the quantity.
Type: String
Valid Values: `Allowed | Disallowed`
Required: Yes

## See Also
<a name="API_marketplace-discovery_Constraints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/Constraints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/Constraints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/Constraints)
