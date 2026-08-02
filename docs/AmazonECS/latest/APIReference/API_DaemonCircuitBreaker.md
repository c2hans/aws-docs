---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonCircuitBreaker.html
---

# DaemonCircuitBreaker
<a name="API_DaemonCircuitBreaker"></a>

Information about the circuit breaker used to determine when a daemon deployment has failed.

## Contents
<a name="API_DaemonCircuitBreaker_Contents"></a>

 ** failureCount **   <a name="ECS-Type-DaemonCircuitBreaker-failureCount"></a>
The number of times the circuit breaker detected a daemon deployment failure.
Type: Integer
Required: No

 ** status **   <a name="ECS-Type-DaemonCircuitBreaker-status"></a>
The circuit breaker status. Amazon ECS is not using the circuit breaker for daemon deployment failures when the status is `DISABLED`.
Type: String
Valid Values: `TRIGGERED | MONITORING | MONITORING_COMPLETE | DISABLED`
Required: No

 ** threshold **   <a name="ECS-Type-DaemonCircuitBreaker-threshold"></a>
The threshold which determines that the daemon deployment failed.
Type: Integer
Required: No

## See Also
<a name="API_DaemonCircuitBreaker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonCircuitBreaker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonCircuitBreaker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonCircuitBreaker)
