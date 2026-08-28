---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RollbackDetails.html
---

# RollbackDetails
<a name="API_RollbackDetails"></a>

Details about an instance refresh rollback.

## Contents
<a name="API_RollbackDetails_Contents"></a>

 ** InstancesToUpdateOnRollback **
Indicates the value of `InstancesToUpdate` at the time the rollback started.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PercentageCompleteOnRollback **
Indicates the value of `PercentageComplete` at the time the rollback started.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** ProgressDetailsOnRollback **
Reports progress on replacing instances in an Auto Scaling group that has a warm pool. This includes separate details for instances in the warm pool and instances in the Auto Scaling group (the live pool).
Type: [InstanceRefreshProgressDetails](API_InstanceRefreshProgressDetails.md) object
Required: No

 ** RollbackReason **
The reason for this instance refresh rollback (for example, whether a manual or automatic rollback was initiated).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** RollbackStartTime **
The date and time at which the rollback began.
Type: Timestamp
Required: No

## See Also
<a name="API_RollbackDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/RollbackDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/RollbackDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/RollbackDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
