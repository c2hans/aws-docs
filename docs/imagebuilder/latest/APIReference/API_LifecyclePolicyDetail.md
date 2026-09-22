---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecyclePolicyDetail.html
---

# LifecyclePolicyDetail
<a name="API_LifecyclePolicyDetail"></a>

Defines one lifecycle policy rule: the action to take, the filter that determines which resources the rule applies to, and optional exclusion rules.

## Contents
<a name="API_LifecyclePolicyDetail_Contents"></a>

 ** action **   <a name="imagebuilder-Type-LifecyclePolicyDetail-action"></a>
Configuration details for the policy action.
Type: [LifecyclePolicyDetailAction](API_LifecyclePolicyDetailAction.md) object
Required: Yes

 ** filter **   <a name="imagebuilder-Type-LifecyclePolicyDetail-filter"></a>
Specifies the resources that the lifecycle policy applies to.
Type: [LifecyclePolicyDetailFilter](API_LifecyclePolicyDetailFilter.md) object
Required: Yes

 ** exclusionRules **   <a name="imagebuilder-Type-LifecyclePolicyDetail-exclusionRules"></a>
Additional rules to specify resources that should be exempt from policy actions.
Type: [LifecyclePolicyDetailExclusionRules](API_LifecyclePolicyDetailExclusionRules.md) object
Required: No

## See Also
<a name="API_LifecyclePolicyDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecyclePolicyDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecyclePolicyDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecyclePolicyDetail)
