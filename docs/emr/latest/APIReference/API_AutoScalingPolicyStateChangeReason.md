---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_AutoScalingPolicyStateChangeReason.html
---

# AutoScalingPolicyStateChangeReason
<a name="API_AutoScalingPolicyStateChangeReason"></a>

The reason for an [AutoScalingPolicyStatus](API_AutoScalingPolicyStatus.md) change.

## Contents
<a name="API_AutoScalingPolicyStateChangeReason_Contents"></a>

 ** Code **   <a name="EMR-Type-AutoScalingPolicyStateChangeReason-Code"></a>
The code indicating the reason for the change in status.`USER_REQUEST` indicates that the scaling policy status was changed by a user. `PROVISION_FAILURE` indicates that the status change was because the policy failed to provision. `CLEANUP_FAILURE` indicates an error.
Type: String
Valid Values: `USER_REQUEST | PROVISION_FAILURE | CLEANUP_FAILURE`
Required: No

 ** Message **   <a name="EMR-Type-AutoScalingPolicyStateChangeReason-Message"></a>
A friendly, more verbose message that accompanies an automatic scaling policy state change.
Type: String
Required: No

## See Also
<a name="API_AutoScalingPolicyStateChangeReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/AutoScalingPolicyStateChangeReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/AutoScalingPolicyStateChangeReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/AutoScalingPolicyStateChangeReason)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
