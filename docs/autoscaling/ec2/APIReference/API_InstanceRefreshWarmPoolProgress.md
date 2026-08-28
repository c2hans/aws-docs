---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRefreshWarmPoolProgress.html
---

# InstanceRefreshWarmPoolProgress
<a name="API_InstanceRefreshWarmPoolProgress"></a>

Reports progress on replacing instances that are in the warm pool.

## Contents
<a name="API_InstanceRefreshWarmPoolProgress_Contents"></a>

 ** InstancesToUpdate **
The number of instances remaining to update.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PercentageComplete **
The percentage of instances in the warm pool that have been replaced. For each instance replacement, Amazon EC2 Auto Scaling tracks the instance's health status and warm-up time. When the instance's health status changes to healthy and the specified warm-up time passes, the instance is considered updated and is added to the percentage complete.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_InstanceRefreshWarmPoolProgress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/InstanceRefreshWarmPoolProgress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/InstanceRefreshWarmPoolProgress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/InstanceRefreshWarmPoolProgress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
