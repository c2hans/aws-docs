---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TargetHealth.html
---

# TargetHealth
<a name="API_TargetHealth"></a>

Information about the current health of a target.

## Contents
<a name="API_TargetHealth_Contents"></a>

 ** Description **
A description of the target health that provides additional details. If the state is `healthy`, a description is not provided.
Type: String
Required: No

 ** Reason **
The reason code.
If the target state is `healthy`, a reason code is not provided.
If the target state is `initial`, the reason code can be one of the following values:
+  `Elb.RegistrationInProgress` - The target is in the process of being registered with the load balancer.
+  `Elb.InitialHealthChecking` - The load balancer is still sending the target the minimum number of health checks required to determine its health status.
If the target state is `unhealthy`, the reason code can be one of the following values:
+  `Target.ResponseCodeMismatch` - The health checks did not return an expected HTTP code.
+  `Target.Timeout` - The health check requests timed out.
+  `Target.FailedHealthChecks` - The load balancer received an error while establishing a connection to the target or the target response was malformed.
+  `Elb.InternalError` - The health checks failed due to an internal error.
If the target state is `unused`, the reason code can be one of the following values:
+  `Target.NotRegistered` - The target is not registered with the target group.
+  `Target.NotInUse` - The target group is not used by any load balancer or the target is in an Availability Zone that is not enabled for its load balancer.
+  `Target.InvalidState` - The target is in the stopped or terminated state.
+  `Target.IpUnusable` - The target IP address is reserved for use by a load balancer.
If the target state is `draining`, the reason code can be the following value:
+  `Target.DeregistrationInProgress` - The target is in the process of being deregistered and the deregistration delay period has not expired.
If the target state is `unavailable`, the reason code can be the following value:
+  `Target.HealthCheckDisabled` - Health checks are disabled for the target group.
+  `Elb.InternalError` - Target health is unavailable due to an internal error.
Type: String
Valid Values: `Elb.RegistrationInProgress | Elb.InitialHealthChecking | Target.ResponseCodeMismatch | Target.Timeout | Target.FailedHealthChecks | Target.NotRegistered | Target.NotInUse | Target.DeregistrationInProgress | Target.InvalidState | Target.IpUnusable | Target.HealthCheckDisabled | Elb.InternalError`
Required: No

 ** State **
The state of the target.
Type: String
Valid Values: `initial | healthy | unhealthy | unhealthy.draining | unused | draining | unavailable`
Required: No

## See Also
<a name="API_TargetHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/TargetHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/TargetHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/TargetHealth)
