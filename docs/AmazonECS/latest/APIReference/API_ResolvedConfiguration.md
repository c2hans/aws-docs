---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ResolvedConfiguration.html
---

# ResolvedConfiguration
<a name="API_ResolvedConfiguration"></a>

The resolved configuration for a service revision, which contains the actual resources your service revision uses, such as which target groups serve traffic.

## Contents
<a name="API_ResolvedConfiguration_Contents"></a>

 ** loadBalancers **   <a name="ECS-Type-ResolvedConfiguration-loadBalancers"></a>
The resolved load balancer configuration for the service revision. This includes information about which target groups serve traffic and which listener rules direct traffic to them.
Type: Array of [ServiceRevisionLoadBalancer](API_ServiceRevisionLoadBalancer.md) objects
Required: No

## See Also
<a name="API_ResolvedConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ResolvedConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ResolvedConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ResolvedConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
