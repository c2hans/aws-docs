---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecycleExecutionResourceState.html
---

# LifecycleExecutionResourceState
<a name="API_LifecycleExecutionResourceState"></a>

Contains the state of an impacted resource that the runtime instance of the lifecycle policy identified for action.

## Contents
<a name="API_LifecycleExecutionResourceState_Contents"></a>

 ** reason **   <a name="imagebuilder-Type-LifecycleExecutionResourceState-reason"></a>
Messaging that clarifies the reason for the assigned status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** status **   <a name="imagebuilder-Type-LifecycleExecutionResourceState-status"></a>
The runtime status of the lifecycle action taken for the impacted resource.
Type: String
Valid Values: `FAILED | IN_PROGRESS | SKIPPED | SUCCESS`
Required: No

## See Also
<a name="API_LifecycleExecutionResourceState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecycleExecutionResourceState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecycleExecutionResourceState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecycleExecutionResourceState)
