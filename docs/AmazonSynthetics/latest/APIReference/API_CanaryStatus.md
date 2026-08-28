---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryStatus.html
---

# CanaryStatus
<a name="API_CanaryStatus"></a>

A structure that contains the current state of the canary.

## Contents
<a name="API_CanaryStatus_Contents"></a>

 ** State **   <a name="synthetics-Type-CanaryStatus-State"></a>
The current state of the canary.
Type: String
Valid Values: `CREATING | READY | STARTING | RUNNING | UPDATING | STOPPING | STOPPED | ERROR | DELETING`
Required: No

 ** StateReason **   <a name="synthetics-Type-CanaryStatus-StateReason"></a>
If the canary creation or update failed, this field provides details on the failure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** StateReasonCode **   <a name="synthetics-Type-CanaryStatus-StateReasonCode"></a>
If the canary creation or update failed, this field displays the reason code.
Type: String
Valid Values: `INVALID_PERMISSIONS | CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_FAILED | UPDATE_PENDING | UPDATE_IN_PROGRESS | UPDATE_COMPLETE | ROLLBACK_COMPLETE | ROLLBACK_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED | SYNC_DELETE_IN_PROGRESS`
Required: No

## See Also
<a name="API_CanaryStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/CanaryStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/CanaryStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/CanaryStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
