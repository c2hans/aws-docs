---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ContentAlternatives.html
---

# ContentAlternatives

The proposed values for a listing field. Exactly one member is set, depending on the field. The list in that member is empty if the status of the recommendation is `INSUFFICIENT_CONTEXT`.

## Contents
<a name="API_ContentAlternatives_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AdditionalResources **   <a name="AWSMarketplaceService-Type-ContentAlternatives-AdditionalResources"></a>
The proposed values for `AdditionalResources`. You can have up to 3 alternatives.
Type: Array of [AdditionalResourcesAlternative](API_AdditionalResourcesAlternative.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

 ** CaseStudies **   <a name="AWSMarketplaceService-Type-ContentAlternatives-CaseStudies"></a>
The proposed values for `CaseStudies`. You can have up to 3 alternatives.
Type: Array of [CaseStudiesAlternative](API_CaseStudiesAlternative.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

 ** Text **   <a name="AWSMarketplaceService-Type-ContentAlternatives-Text"></a>
The proposed values for a text field, such as `ProductTitle` or `LongDescription`. You can have up to 3 alternatives.
Type: Array of [TextAlternative](API_TextAlternative.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

 ** TextList **   <a name="AWSMarketplaceService-Type-ContentAlternatives-TextList"></a>
The proposed values for `Highlights`, `SearchKeywords`, or `Categories`. You can have up to 3 alternatives.
Type: Array of [TextListAlternative](API_TextListAlternative.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

 ** UseCases **   <a name="AWSMarketplaceService-Type-ContentAlternatives-UseCases"></a>
The proposed values for `UseCases`. You can have up to 3 alternatives.
Type: Array of [UseCasesAlternative](API_UseCasesAlternative.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

## See Also
<a name="API_ContentAlternatives_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ContentAlternatives)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ContentAlternatives)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ContentAlternatives)
