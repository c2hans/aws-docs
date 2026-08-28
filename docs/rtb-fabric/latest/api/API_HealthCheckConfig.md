---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_HealthCheckConfig.html
---

# HealthCheckConfig
<a name="API_HealthCheckConfig"></a>

The health check configuration for a managed endpoint. Defines how the service probes instances in the Auto Scaling group to determine their health status.

## Contents
<a name="API_HealthCheckConfig_Contents"></a>

 ** path **   <a name="rtbfabric-Type-HealthCheckConfig-path"></a>
The destination path for the health check request. Must start with `/`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `/.*`
Required: Yes

 ** port **   <a name="rtbfabric-Type-HealthCheckConfig-port"></a>
The port to use for health check probes. Valid range is 80 to 65535.
Type: Integer
Valid Range: Minimum value of 80. Maximum value of 65535.
Required: Yes

 ** healthyThresholdCount **   <a name="rtbfabric-Type-HealthCheckConfig-healthyThresholdCount"></a>
The number of consecutive successful health checks required before an instance is considered healthy. Valid range is 2 to 10.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10.
Required: No

 ** intervalSeconds **   <a name="rtbfabric-Type-HealthCheckConfig-intervalSeconds"></a>
The interval between health check probes, in seconds. Valid range is 5 to 60.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 60.
Required: No

 ** protocol **   <a name="rtbfabric-Type-HealthCheckConfig-protocol"></a>
The protocol to use for health check probes.
Type: String
Valid Values: `HTTP | HTTPS`
Required: No

 ** statusCodeMatcher **   <a name="rtbfabric-Type-HealthCheckConfig-statusCodeMatcher"></a>
The expected HTTP status code or status code pattern from healthy instances. Supports a single code (for example, `200`), a range (for example, `200-299`), or a comma-separated list (for example, `200,204`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** timeoutMs **   <a name="rtbfabric-Type-HealthCheckConfig-timeoutMs"></a>
The timeout for each health check probe, in milliseconds. Valid range is 100 to 5000.
Type: Integer
Valid Range: Minimum value of 100. Maximum value of 5000.
Required: No

 ** unhealthyThresholdCount **   <a name="rtbfabric-Type-HealthCheckConfig-unhealthyThresholdCount"></a>
The number of consecutive failed health checks required before an instance is considered unhealthy. Valid range is 2 to 10.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10.
Required: No

## See Also
<a name="API_HealthCheckConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/HealthCheckConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/HealthCheckConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/HealthCheckConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RTB Fabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rtb-fabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
