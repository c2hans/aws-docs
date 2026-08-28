---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecycleExecutionState.html
---

# LifecycleExecutionState
<a name="API_LifecycleExecutionState"></a>

The current state of the runtime instance of the lifecycle policy.

## Contents
<a name="API_LifecycleExecutionState_Contents"></a>

 ** reason **   <a name="imagebuilder-Type-LifecycleExecutionState-reason"></a>
The reason for the current status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** status **   <a name="imagebuilder-Type-LifecycleExecutionState-status"></a>
The runtime status of the lifecycle execution.
Type: String
Valid Values: `IN_PROGRESS | CANCELLED | CANCELLING | FAILED | SUCCESS | PENDING`
Required: No

## See Also
<a name="API_LifecycleExecutionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecycleExecutionState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecycleExecutionState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecycleExecutionState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
