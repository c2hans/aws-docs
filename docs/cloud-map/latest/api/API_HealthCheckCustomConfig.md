---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html
---

# HealthCheckCustomConfig
<a name="API_HealthCheckCustomConfig"></a>

A complex type that contains information about an optional custom health check. A custom health check, which requires that you use a third-party health checker to evaluate the health of your resources, is useful in the following circumstances:
+ You can't use a health check that's defined by `HealthCheckConfig` because the resource isn't available over the internet. For example, you can use a custom health check when the instance is in an Amazon VPC. (To check the health of resources in a VPC, the health checker must also be in the VPC.)
+ You want to use a third-party health checker regardless of where your resources are located.

**Important**
If you specify a health check configuration, you can specify either `HealthCheckCustomConfig` or `HealthCheckConfig` but not both.

To change the status of a custom health check, submit an `UpdateInstanceCustomHealthStatus` request. AWS Cloud Map doesn't monitor the status of the resource, it just keeps a record of the status specified in the most recent `UpdateInstanceCustomHealthStatus` request.

Here's how custom health checks work:

1. You create a service.

1. You register an instance.

1. You configure a third-party health checker to monitor the resource that's associated with the new instance.
**Note**
 AWS Cloud Map doesn't check the health of the resource directly.

1. The third-party health-checker determines that the resource is unhealthy and notifies your application.

1. Your application submits an `UpdateInstanceCustomHealthStatus` request.

1.  AWS Cloud Map waits for 30 seconds.

1. If another `UpdateInstanceCustomHealthStatus` request doesn't arrive during that time to change the status back to healthy, AWS Cloud Map stops routing traffic to the resource.

## Contents
<a name="API_HealthCheckCustomConfig_Contents"></a>

 ** FailureThreshold **   <a name="cloudmap-Type-HealthCheckCustomConfig-FailureThreshold"></a>
 *This member has been deprecated.*
This parameter is no longer supported and is always set to 1. AWS Cloud Map waits for approximately 30 seconds after receiving an `UpdateInstanceCustomHealthStatus` request before changing the status of the service instance.
The number of 30-second intervals that you want AWS Cloud Map to wait after receiving an `UpdateInstanceCustomHealthStatus` request before it changes the health status of a service instance.
Sending a second or subsequent `UpdateInstanceCustomHealthStatus` request with the same value before 30 seconds has passed doesn't accelerate the change. AWS Cloud Map still waits `30` seconds after the first request to make the change.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

## See Also
<a name="API_HealthCheckCustomConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/HealthCheckCustomConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/HealthCheckCustomConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/HealthCheckCustomConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
