---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecyclePolicyResourceSelection.html
---

# LifecyclePolicyResourceSelection
<a name="API_LifecyclePolicyResourceSelection"></a>

Resource selection criteria for the lifecycle policy.

## Contents
<a name="API_LifecyclePolicyResourceSelection_Contents"></a>

 ** recipes **   <a name="imagebuilder-Type-LifecyclePolicyResourceSelection-recipes"></a>
A list of recipes that are used as selection criteria for the output images that the lifecycle policy applies to.
Type: Array of [LifecyclePolicyResourceSelectionRecipe](API_LifecyclePolicyResourceSelectionRecipe.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** tagMap **   <a name="imagebuilder-Type-LifecyclePolicyResourceSelection-tagMap"></a>
A list of tags that are used as selection criteria for the Image Builder image resources that the lifecycle policy applies to.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_LifecyclePolicyResourceSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecyclePolicyResourceSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecyclePolicyResourceSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecyclePolicyResourceSelection)
