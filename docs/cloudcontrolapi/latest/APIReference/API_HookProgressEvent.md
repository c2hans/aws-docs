---
source_url: https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_HookProgressEvent.html
---

# HookProgressEvent
<a name="API_HookProgressEvent"></a>

Represents the current status of a Hook operation request for the target resource.

For more information about Hooks, see the [AWS CloudFormation Hooks User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html).

## Contents
<a name="API_HookProgressEvent_Contents"></a>

 ** FailureMode **   <a name="ccapi-Type-HookProgressEvent-FailureMode"></a>
The failure mode of the invocation. The following are the potential statuses:
+  `FAIL`: This will fail the Hook invocation and the request associated with it.
+  `WARN`: This will fail the Hook invocation, but not the request associated with it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-A-Za-z_]+`
Required: No

 ** HookEventTime **   <a name="ccapi-Type-HookProgressEvent-HookEventTime"></a>
The time that the Hook invocation request initiated.
Type: Timestamp
Required: No

 ** HookStatus **   <a name="ccapi-Type-HookProgressEvent-HookStatus"></a>
The status of the Hook invocation. The following are potential statuses:
+  `HOOK_PENDING`: The Hook was added to the invocation plan, but not yet invoked.
+  `HOOK_IN_PROGRESS`: The Hook was invoked, but hasn't completed.
+  `HOOK_COMPLETE_SUCCEEDED`: The Hook invocation is complete with a successful result.
+  `HOOK_COMPLETE_FAILED`: The Hook invocation is complete with a failed result.
+  `HOOK_FAILED`: The Hook invocation didn't complete successfully.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-A-Za-z_]+`
Required: No

 ** HookStatusMessage **   <a name="ccapi-Type-HookProgressEvent-HookStatusMessage"></a>
The message explaining the current Hook status.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`
Required: No

 ** HookTypeArn **   <a name="ccapi-Type-HookProgressEvent-HookTypeArn"></a>
The ARN of the Hook being invoked.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:.+:.*:.*:.+`
Required: No

 ** HookTypeName **   <a name="ccapi-Type-HookProgressEvent-HookTypeName"></a>
The type name of the Hook being invoked.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 196.
Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}`
Required: No

 ** HookTypeVersionId **   <a name="ccapi-Type-HookProgressEvent-HookTypeVersionId"></a>
The type version of the Hook being invoked.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-]+`
Required: No

 ** InvocationPoint **   <a name="ccapi-Type-HookProgressEvent-InvocationPoint"></a>
The point in which the Hook is being invoked.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-A-Za-z_]+`
Required: No

## See Also
<a name="API_HookProgressEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudcontrol-2021-09-30/HookProgressEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudcontrol-2021-09-30/HookProgressEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudcontrol-2021-09-30/HookProgressEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Control API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudcontrolapi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
