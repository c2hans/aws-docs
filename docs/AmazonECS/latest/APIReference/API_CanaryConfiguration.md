---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CanaryConfiguration.html
---

# CanaryConfiguration
<a name="API_CanaryConfiguration"></a>

Configuration for a canary deployment strategy that shifts a fixed percentage of traffic to the new service revision, waits for a specified bake time, then shifts the remaining traffic.

This is only valid when you run `CreateService` or `UpdateService` with `deploymentController` set to `ECS` and a `deploymentConfiguration` with a strategy set to `CANARY`.

## Contents
<a name="API_CanaryConfiguration_Contents"></a>

 ** canaryBakeTimeInMinutes **   <a name="ECS-Type-CanaryConfiguration-canaryBakeTimeInMinutes"></a>
The amount of time in minutes to wait during the canary phase before shifting the remaining production traffic to the new service revision. Valid values are 0 to 1440 minutes (24 hours). The default value is 10.
Type: Integer
Required: No

 ** canaryPercent **   <a name="ECS-Type-CanaryConfiguration-canaryPercent"></a>
The percentage of production traffic to shift to the new service revision during the canary phase. Valid values are multiples of 0.1 from 0.1 to 100.0. The default value is 5.0.
Type: Double
Required: No

## See Also
<a name="API_CanaryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/CanaryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/CanaryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/CanaryConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
