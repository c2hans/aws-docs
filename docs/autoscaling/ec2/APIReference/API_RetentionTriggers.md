---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RetentionTriggers.html
---

# RetentionTriggers
<a name="API_RetentionTriggers"></a>

 Defines the specific triggers that cause instances to be retained in a Retained state rather than terminated. Each trigger corresponds to a different failure scenario during the instance lifecycle. This allows fine-grained control over when to preserve instances for manual intervention.

## Contents
<a name="API_RetentionTriggers_Contents"></a>

 ** TerminateHookAbandon **
 Specifies the action when a termination lifecycle hook is abandoned due to failure, timeout, or explicit abandonment (calling CompleteLifecycleAction).
 Set to `retain` to move instances to a retained state. Set to `terminate` for default termination behavior.
 Retained instances don't count toward desired capacity and remain until you call `TerminateInstanceInAutoScalingGroup`.
Type: String
Valid Values: `retain | terminate`
Required: No

## See Also
<a name="API_RetentionTriggers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/RetentionTriggers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/RetentionTriggers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/RetentionTriggers)
