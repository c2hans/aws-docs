---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_HealthCheckPolicy.html
---

# HealthCheckPolicy
<a name="API_HealthCheckPolicy"></a>

An object that represents the health check policy for a virtual node's listener.

## Contents
<a name="API_HealthCheckPolicy_Contents"></a>

 ** healthyThreshold **   <a name="appmesh-Type-HealthCheckPolicy-healthyThreshold"></a>
The number of consecutive successful health checks that must occur before declaring listener healthy.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10.
Required: Yes

 ** intervalMillis **   <a name="appmesh-Type-HealthCheckPolicy-intervalMillis"></a>
The time period in milliseconds between each health check execution.
Type: Long
Valid Range: Minimum value of 5000. Maximum value of 300000.
Required: Yes

 ** protocol **   <a name="appmesh-Type-HealthCheckPolicy-protocol"></a>
The protocol for the health check request. If you specify `grpc`, then your service must conform to the [GRPC Health Checking Protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md).
Type: String
Valid Values: `http | tcp | http2 | grpc`
Required: Yes

 ** timeoutMillis **   <a name="appmesh-Type-HealthCheckPolicy-timeoutMillis"></a>
The amount of time to wait when receiving a response from the health check, in milliseconds.
Type: Long
Valid Range: Minimum value of 2000. Maximum value of 60000.
Required: Yes

 ** unhealthyThreshold **   <a name="appmesh-Type-HealthCheckPolicy-unhealthyThreshold"></a>
The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10.
Required: Yes

 ** path **   <a name="appmesh-Type-HealthCheckPolicy-path"></a>
The destination path for the health check request. This value is only used if the specified protocol is HTTP or HTTP/2. For any other protocol, this value is ignored.
Type: String
Required: No

 ** port **   <a name="appmesh-Type-HealthCheckPolicy-port"></a>
The destination port for the health check request. This port must match the port defined in the [PortMapping](API_PortMapping.md) for the listener.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

## See Also
<a name="API_HealthCheckPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HealthCheckPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HealthCheckPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HealthCheckPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
