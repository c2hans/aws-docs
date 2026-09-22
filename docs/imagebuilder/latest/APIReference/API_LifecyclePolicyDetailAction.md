---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecyclePolicyDetailAction.html
---

# LifecyclePolicyDetailAction
<a name="API_LifecyclePolicyDetailAction"></a>

Contains the action configuration for a lifecycle policy rule: the action to take, and which underlying resources the action extends to.

## Contents
<a name="API_LifecyclePolicyDetailAction_Contents"></a>

 ** type **   <a name="imagebuilder-Type-LifecyclePolicyDetailAction-type"></a>
Specifies the lifecycle action to take. `DELETE` deletes the image resource and, with `includeResources`, also removes distributed AMIs, snapshots, or container images. `DEPRECATE` and `DISABLE` set the corresponding status on the image resource and, if `includeResources.amis` is set, on its distributed AMIs.
Type: String
Valid Values: `DELETE | DEPRECATE | DISABLE`
Required: Yes

 ** includeResources **   <a name="imagebuilder-Type-LifecyclePolicyDetailAction-includeResources"></a>
Specifies which underlying resources the action extends to beyond the Image Builder image resource itself: distributed AMIs, their snapshots, or distributed container images. `DELETE` rules can include all three, `DEPRECATE` and `DISABLE` rules can include AMIs only, and you can only include snapshots together with AMIs.
Type: [LifecyclePolicyDetailActionIncludeResources](API_LifecyclePolicyDetailActionIncludeResources.md) object
Required: No

## See Also
<a name="API_LifecyclePolicyDetailAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecyclePolicyDetailAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecyclePolicyDetailAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecyclePolicyDetailAction)
