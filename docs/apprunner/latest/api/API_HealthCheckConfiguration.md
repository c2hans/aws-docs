---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_HealthCheckConfiguration.html
---

# HealthCheckConfiguration
<a name="API_HealthCheckConfiguration"></a>

Describes the settings for the health check that AWS App Runner performs to monitor the health of a service.

## Contents
<a name="API_HealthCheckConfiguration_Contents"></a>

 ** HealthyThreshold **   <a name="apprunner-Type-HealthCheckConfiguration-HealthyThreshold"></a>
The number of consecutive checks that must succeed before App Runner decides that the service is healthy.
Default: `1`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** Interval **   <a name="apprunner-Type-HealthCheckConfiguration-Interval"></a>
The time interval, in seconds, between health checks.
Default: `5`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** Path **   <a name="apprunner-Type-HealthCheckConfiguration-Path"></a>
The URL that health check requests are sent to.
 `Path` is only applicable when you set `Protocol` to `HTTP`.
Default: `"/"`
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Protocol **   <a name="apprunner-Type-HealthCheckConfiguration-Protocol"></a>
The IP protocol that App Runner uses to perform health checks for your service.
If you set `Protocol` to `HTTP`, App Runner sends health check requests to the HTTP path specified by `Path`.
Default: `TCP`
Type: String
Valid Values: `TCP | HTTP`
Required: No

 ** Timeout **   <a name="apprunner-Type-HealthCheckConfiguration-Timeout"></a>
The time, in seconds, to wait for a health check response before deciding it failed.
Default: `2`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** UnhealthyThreshold **   <a name="apprunner-Type-HealthCheckConfiguration-UnhealthyThreshold"></a>
The number of consecutive checks that must fail before App Runner decides that the service is unhealthy.
Default: `5`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

## See Also
<a name="API_HealthCheckConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/HealthCheckConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/HealthCheckConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/HealthCheckConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
