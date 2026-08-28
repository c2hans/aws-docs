---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_AutoScalingPolicyDescription.html
---

# AutoScalingPolicyDescription
<a name="API_AutoScalingPolicyDescription"></a>

An automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates Amazon EC2 instances in response to the value of a CloudWatch metric. See [PutAutoScalingPolicy](API_PutAutoScalingPolicy.md).

## Contents
<a name="API_AutoScalingPolicyDescription_Contents"></a>

 ** Constraints **   <a name="EMR-Type-AutoScalingPolicyDescription-Constraints"></a>
The upper and lower Amazon EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.
Type: [ScalingConstraints](API_ScalingConstraints.md) object
Required: No

 ** Rules **   <a name="EMR-Type-AutoScalingPolicyDescription-Rules"></a>
The scale-in and scale-out rules that comprise the automatic scaling policy.
Type: Array of [ScalingRule](API_ScalingRule.md) objects
Required: No

 ** Status **   <a name="EMR-Type-AutoScalingPolicyDescription-Status"></a>
The status of an automatic scaling policy.
Type: [AutoScalingPolicyStatus](API_AutoScalingPolicyStatus.md) object
Required: No

## See Also
<a name="API_AutoScalingPolicyDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/AutoScalingPolicyDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/AutoScalingPolicyDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/AutoScalingPolicyDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
