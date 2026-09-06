---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_InstanceHealthSummary.html
---

# InstanceHealthSummary
<a name="API_InstanceHealthSummary"></a>

Describes information about the health of the instance.

## Contents
<a name="API_InstanceHealthSummary_Contents"></a>

 ** instanceHealth **   <a name="Lightsail-Type-InstanceHealthSummary-instanceHealth"></a>
Describes the overall instance health. Valid values are below.
Type: String
Valid Values: `initial | healthy | unhealthy | unused | draining | unavailable`
Required: No

 ** instanceHealthReason **   <a name="Lightsail-Type-InstanceHealthSummary-instanceHealthReason"></a>
More information about the instance health. If the `instanceHealth` is `healthy`, then an `instanceHealthReason` value is not provided.
If ** `instanceHealth` ** is `initial`, the ** `instanceHealthReason` ** value can be one of the following:
+  ** `Lb.RegistrationInProgress` ** - The target instance is in the process of being registered with the load balancer.
+  ** `Lb.InitialHealthChecking` ** - The Lightsail load balancer is still sending the target instance the minimum number of health checks required to determine its health status.
If ** `instanceHealth` ** is `unhealthy`, the ** `instanceHealthReason` ** value can be one of the following:
+  ** `Instance.ResponseCodeMismatch` ** - The health checks did not return an expected HTTP code.
+  ** `Instance.Timeout` ** - The health check requests timed out.
+  ** `Instance.FailedHealthChecks` ** - The health checks failed because the connection to the target instance timed out, the target instance response was malformed, or the target instance failed the health check for an unknown reason.
+  ** `Lb.InternalError` ** - The health checks failed due to an internal error.
If ** `instanceHealth` ** is `unused`, the ** `instanceHealthReason` ** value can be one of the following:
+  ** `Instance.NotRegistered` ** - The target instance is not registered with the target group.
+  ** `Instance.NotInUse` ** - The target group is not used by any load balancer, or the target instance is in an Availability Zone that is not enabled for its load balancer.
+  ** `Instance.IpUnusable` ** - The target IP address is reserved for use by a Lightsail load balancer.
+  ** `Instance.InvalidState` ** - The target is in the stopped or terminated state.
If ** `instanceHealth` ** is `draining`, the ** `instanceHealthReason` ** value can be one of the following:
+  ** `Instance.DeregistrationInProgress` ** - The target instance is in the process of being deregistered and the deregistration delay period has not expired.
Type: String
Valid Values: `Lb.RegistrationInProgress | Lb.InitialHealthChecking | Lb.InternalError | Instance.ResponseCodeMismatch | Instance.Timeout | Instance.FailedHealthChecks | Instance.NotRegistered | Instance.NotInUse | Instance.DeregistrationInProgress | Instance.InvalidState | Instance.IpUnusable`
Required: No

 ** instanceName **   <a name="Lightsail-Type-InstanceHealthSummary-instanceName"></a>
The name of the Lightsail instance for which you are requesting health check data.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

## See Also
<a name="API_InstanceHealthSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/InstanceHealthSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/InstanceHealthSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/InstanceHealthSummary)
