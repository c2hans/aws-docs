---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecyclePolicyDetailExclusionRules.html
---

# LifecyclePolicyDetailExclusionRules
<a name="API_LifecyclePolicyDetailExclusionRules"></a>

Specifies resources that lifecycle policy actions should not apply to.

## Contents
<a name="API_LifecyclePolicyDetailExclusionRules_Contents"></a>

 ** amis **   <a name="imagebuilder-Type-LifecyclePolicyDetailExclusionRules-amis"></a>
Lists configuration values that apply to AMIs that Image Builder should exclude from the lifecycle action.
Type: [LifecyclePolicyDetailExclusionRulesAmis](API_LifecyclePolicyDetailExclusionRulesAmis.md) object
Required: No

 ** tagMap **   <a name="imagebuilder-Type-LifecyclePolicyDetailExclusionRules-tagMap"></a>
Contains a list of tags that Image Builder uses to skip lifecycle actions for Image Builder image resources that have them.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_LifecyclePolicyDetailExclusionRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecyclePolicyDetailExclusionRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecyclePolicyDetailExclusionRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecyclePolicyDetailExclusionRules)
