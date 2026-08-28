---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_State.html
---

# State
<a name="API_State"></a>

An object that described the state of Amazon Inspector scans for an account.

## Contents
<a name="API_State_Contents"></a>

 ** errorCode **   <a name="inspector2-Type-State-errorCode"></a>
The error code explaining why the account failed to enable Amazon Inspector.
Type: String
Valid Values: `ALREADY_ENABLED | ENABLE_IN_PROGRESS | DISABLE_IN_PROGRESS | SUSPEND_IN_PROGRESS | RESOURCE_NOT_FOUND | ACCESS_DENIED | INTERNAL_ERROR | SSM_UNAVAILABLE | SSM_THROTTLED | EVENTBRIDGE_UNAVAILABLE | EVENTBRIDGE_THROTTLED | RESOURCE_SCAN_NOT_DISABLED | DISASSOCIATE_ALL_MEMBERS | ACCOUNT_IS_ISOLATED | EC2_SSM_RESOURCE_DATA_SYNC_LIMIT_EXCEEDED | EC2_SSM_ASSOCIATION_VERSION_LIMIT_EXCEEDED | BLOCKED_BY_ORGANIZATION_POLICY`
Required: Yes

 ** errorMessage **   <a name="inspector2-Type-State-errorMessage"></a>
The error message received when the account failed to enable Amazon Inspector.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** status **   <a name="inspector2-Type-State-status"></a>
The status of Amazon Inspector for the account.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | SUSPENDING | SUSPENDED`
Required: Yes

## See Also
<a name="API_State_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/State)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/State)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/State)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
