---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_AutoScalingPolicy.html
---

# AutoScalingPolicy
<a name="API_AutoScalingPolicy"></a>

An automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. An automatic scaling policy defines how an instance group dynamically adds and terminates Amazon EC2 instances in response to the value of a CloudWatch metric. See [PutAutoScalingPolicy](API_PutAutoScalingPolicy.md).

## Contents
<a name="API_AutoScalingPolicy_Contents"></a>

 ** Constraints **   <a name="EMR-Type-AutoScalingPolicy-Constraints"></a>
The upper and lower Amazon EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.
Type: [ScalingConstraints](API_ScalingConstraints.md) object
Required: Yes

 ** Rules **   <a name="EMR-Type-AutoScalingPolicy-Rules"></a>
The scale-in and scale-out rules that comprise the automatic scaling policy.
Type: Array of [ScalingRule](API_ScalingRule.md) objects
Required: Yes

## See Also
<a name="API_AutoScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/AutoScalingPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/AutoScalingPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/AutoScalingPolicy)
