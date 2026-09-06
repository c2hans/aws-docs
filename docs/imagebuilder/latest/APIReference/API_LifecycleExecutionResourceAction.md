---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecycleExecutionResourceAction.html
---

# LifecycleExecutionResourceAction
<a name="API_LifecycleExecutionResourceAction"></a>

The lifecycle policy action that was identified for the impacted resource.

## Contents
<a name="API_LifecycleExecutionResourceAction_Contents"></a>

 ** name **   <a name="imagebuilder-Type-LifecycleExecutionResourceAction-name"></a>
The name of the resource that was identified for a lifecycle policy action.
Type: String
Valid Values: `AVAILABLE | DELETE | DEPRECATE | DISABLE`
Required: No

 ** reason **   <a name="imagebuilder-Type-LifecycleExecutionResourceAction-reason"></a>
The reason why the lifecycle policy action is taken.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_LifecycleExecutionResourceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecycleExecutionResourceAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecycleExecutionResourceAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecycleExecutionResourceAction)
