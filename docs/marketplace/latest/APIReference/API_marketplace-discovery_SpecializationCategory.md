---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SpecializationCategory.html
---

# SpecializationCategory

A category under a specialization that the listing earned.

## Contents
<a name="API_marketplace-discovery_SpecializationCategory_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** parentSpecializationId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SpecializationCategory-parentSpecializationId"></a>
The identifier of the parent specialization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9\-]+`
Required: Yes

 ** specializationCategoryId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SpecializationCategory-specializationCategoryId"></a>
The unique identifier of the category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9\-]+`
Required: Yes

 ** specializationCategoryName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SpecializationCategory-specializationCategoryName"></a>
The name of the category displayed to you.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_marketplace-discovery_SpecializationCategory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/SpecializationCategory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/SpecializationCategory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/SpecializationCategory)
