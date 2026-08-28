---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceRevisionLoadBalancer.html
---

# ServiceRevisionLoadBalancer
<a name="API_ServiceRevisionLoadBalancer"></a>

The resolved load balancer configuration for a service revision. This includes information about which target groups serve traffic and which listener rules direct traffic to them.

## Contents
<a name="API_ServiceRevisionLoadBalancer_Contents"></a>

 ** productionListenerRule **   <a name="ECS-Type-ServiceRevisionLoadBalancer-productionListenerRule"></a>
The Amazon Resource Name (ARN) of the production listener rule or listener that directs traffic to the target group associated with the service revision.
Type: String
Required: No

 ** targetGroupArn **   <a name="ECS-Type-ServiceRevisionLoadBalancer-targetGroupArn"></a>
The Amazon Resource Name (ARN) of the target group associated with the service revision.
Type: String
Required: No

## See Also
<a name="API_ServiceRevisionLoadBalancer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceRevisionLoadBalancer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceRevisionLoadBalancer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceRevisionLoadBalancer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
