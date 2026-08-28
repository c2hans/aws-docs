---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_LinearConfiguration.html
---

# LinearConfiguration
<a name="API_LinearConfiguration"></a>

Configuration for linear deployment strategy that shifts production traffic in equal percentage increments with configurable wait times between each step until 100% of traffic is shifted to the new service revision. This is only valid when you run `CreateService` or `UpdateService` with `deploymentController` set to `ECS` and a `deploymentConfiguration` with a strategy set to `LINEAR`.

## Contents
<a name="API_LinearConfiguration_Contents"></a>

 ** stepBakeTimeInMinutes **   <a name="ECS-Type-LinearConfiguration-stepBakeTimeInMinutes"></a>
The amount of time in minutes to wait between each traffic shifting step during a linear deployment. Valid values are 0 to 1440 minutes (24 hours). The default value is 6. This bake time is not applied after reaching 100 percent traffic.
Type: Integer
Required: No

 ** stepPercent **   <a name="ECS-Type-LinearConfiguration-stepPercent"></a>
The percentage of production traffic to shift in each step during a linear deployment. Valid values are multiples of 0.1 from 3.0 to 100.0. The default value is 10.0.
Type: Double
Required: No

## See Also
<a name="API_LinearConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/LinearConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/LinearConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/LinearConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
