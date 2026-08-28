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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
