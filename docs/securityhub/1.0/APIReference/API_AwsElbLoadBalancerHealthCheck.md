---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElbLoadBalancerHealthCheck.html
---

# AwsElbLoadBalancerHealthCheck
<a name="API_AwsElbLoadBalancerHealthCheck"></a>

Contains information about the health checks that are conducted on the load balancer.

## Contents
<a name="API_AwsElbLoadBalancerHealthCheck_Contents"></a>

 ** HealthyThreshold **   <a name="securityhub-Type-AwsElbLoadBalancerHealthCheck-HealthyThreshold"></a>
The number of consecutive health check successes required before the instance is moved to the Healthy state.
Type: Integer
Required: No

 ** Interval **   <a name="securityhub-Type-AwsElbLoadBalancerHealthCheck-Interval"></a>
The approximate interval, in seconds, between health checks of an individual instance.
Type: Integer
Required: No

 ** Target **   <a name="securityhub-Type-AwsElbLoadBalancerHealthCheck-Target"></a>
The instance that is being checked. The target specifies the protocol and port. The available protocols are TCP, SSL, HTTP, and HTTPS. The range of valid ports is 1 through 65535.
For the HTTP and HTTPS protocols, the target also specifies the ping path.
For the TCP protocol, the target is specified as `TCP: <port> `.
For the SSL protocol, the target is specified as `SSL.<port> `.
For the HTTP and HTTPS protocols, the target is specified as ` <protocol>:<port>/<path to ping> `.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Timeout **   <a name="securityhub-Type-AwsElbLoadBalancerHealthCheck-Timeout"></a>
The amount of time, in seconds, during which no response means a failed health check.
Type: Integer
Required: No

 ** UnhealthyThreshold **   <a name="securityhub-Type-AwsElbLoadBalancerHealthCheck-UnhealthyThreshold"></a>
The number of consecutive health check failures that must occur before the instance is moved to the Unhealthy state.
Type: Integer
Required: No

## See Also
<a name="API_AwsElbLoadBalancerHealthCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElbLoadBalancerHealthCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElbLoadBalancerHealthCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElbLoadBalancerHealthCheck)
