---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_HealthCheckConfig.html
---

# HealthCheckConfig
<a name="API_HealthCheckConfig"></a>

Describes the health check configuration of a target group. Health check configurations aren't used for target groups of type `LAMBDA` or `ALB`.

## Contents
<a name="API_HealthCheckConfig_Contents"></a>

 ** enabled **   <a name="vpclattice-Type-HealthCheckConfig-enabled"></a>
Indicates whether health checking is enabled.
Type: Boolean
Required: No

 ** healthCheckIntervalSeconds **   <a name="vpclattice-Type-HealthCheckConfig-healthCheckIntervalSeconds"></a>
The approximate amount of time, in seconds, between health checks of an individual target. The range is 5–300 seconds. The default is 30 seconds.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 300.
Required: No

 ** healthCheckTimeoutSeconds **   <a name="vpclattice-Type-HealthCheckConfig-healthCheckTimeoutSeconds"></a>
The amount of time, in seconds, to wait before reporting a target as unhealthy. The range is 1–120 seconds. The default is 5 seconds.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 120.
Required: No

 ** healthyThresholdCount **   <a name="vpclattice-Type-HealthCheckConfig-healthyThresholdCount"></a>
The number of consecutive successful health checks required before considering an unhealthy target healthy. The range is 2–10. The default is 5.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10.
Required: No

 ** matcher **   <a name="vpclattice-Type-HealthCheckConfig-matcher"></a>
The codes to use when checking for a successful response from a target.
Type: [Matcher](API_Matcher.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** path **   <a name="vpclattice-Type-HealthCheckConfig-path"></a>
The destination for health checks on the targets. If the protocol version is `HTTP/1.1` or `HTTP/2`, specify a valid URI (for example, `/path?query`). The default path is `/`. Health checks are not supported if the protocol version is `gRPC`, however, you can choose `HTTP/1.1` or `HTTP/2` and specify a valid URI.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*(^/[a-zA-Z0-9@:%_+.~#?&/=-]*$|(^$)).*`
Required: No

 ** port **   <a name="vpclattice-Type-HealthCheckConfig-port"></a>
The port used when performing health checks on targets. The default setting is the port that a target receives traffic on.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

 ** protocol **   <a name="vpclattice-Type-HealthCheckConfig-protocol"></a>
The protocol used when performing health checks on targets. The possible protocols are `HTTP` and `HTTPS`. The default is `HTTP`.
Type: String
Valid Values: `HTTP | HTTPS | TCP`
Required: No

 ** protocolVersion **   <a name="vpclattice-Type-HealthCheckConfig-protocolVersion"></a>
The protocol version used when performing health checks on targets. The possible protocol versions are `HTTP1` and `HTTP2`.
Type: String
Valid Values: `HTTP1 | HTTP2`
Required: No

 ** unhealthyThresholdCount **   <a name="vpclattice-Type-HealthCheckConfig-unhealthyThresholdCount"></a>
The number of consecutive failed health checks required before considering a target unhealthy. The range is 2–10. The default is 2.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10.
Required: No

## See Also
<a name="API_HealthCheckConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/HealthCheckConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/HealthCheckConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/HealthCheckConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
