---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerInstanceHealthStatus.html
---

# ContainerInstanceHealthStatus
<a name="API_ContainerInstanceHealthStatus"></a>

An object representing the health status of the container instance.

## Contents
<a name="API_ContainerInstanceHealthStatus_Contents"></a>

 ** details **   <a name="ECS-Type-ContainerInstanceHealthStatus-details"></a>
An array of objects representing the details of the container instance health status.
Type: Array of [InstanceHealthCheckResult](API_InstanceHealthCheckResult.md) objects
Required: No

 ** overallStatus **   <a name="ECS-Type-ContainerInstanceHealthStatus-overallStatus"></a>
The overall health status of the container instance. This is an aggregate status of all container instance health checks.
Type: String
Valid Values: `OK | IMPAIRED | INSUFFICIENT_DATA | INITIALIZING`
Required: No

## See Also
<a name="API_ContainerInstanceHealthStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ContainerInstanceHealthStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ContainerInstanceHealthStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ContainerInstanceHealthStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
