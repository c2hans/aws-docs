---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceLifecyclePolicy.html
---

# InstanceLifecyclePolicy
<a name="API_InstanceLifecyclePolicy"></a>

 The instance lifecycle policy for the Auto Scaling group. This policy controls instance behavior when an instance transitions through its lifecycle states. Configure retention triggers to specify when instances should move to a `Retained` state instead of automatic termination.

For more information, see [ Control instance retention with instance lifecycle policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-lifecycle-policy.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Contents
<a name="API_InstanceLifecyclePolicy_Contents"></a>

 ** RetentionTriggers **
 Specifies the conditions that trigger instance retention behavior. These triggers determine when instances should move to a `Retained` state instead of automatic termination. This allows you to maintain control over instance management when lifecycles transition and operations fail.
Type: [RetentionTriggers](API_RetentionTriggers.md) object
Required: No

## See Also
<a name="API_InstanceLifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/InstanceLifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/InstanceLifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/InstanceLifecyclePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
