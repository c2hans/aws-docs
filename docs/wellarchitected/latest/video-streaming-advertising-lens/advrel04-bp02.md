---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel04-bp02.html
---

# ADVREL04-BP02 Deploy new code or resources in staggered phases, separated by sufficient time, to verify that the changes are successful
<a name="advrel04-bp02"></a>

 Implement gradual, phased deployments to minimize risks and service impacts when updating systems.

## Implementation guidance
<a name="implementation-guidance-27"></a>

 When deploying new code or resources, it is possible for unintended results to occur. Various deployment strategies can be used to reduce frequency and service impact.

 By making changes through a blue/green deployment methodology, you can significantly reduce the impact of any potential issues and avoid downtime.

 When a blue/green deployment isn't possible, a rolling deployment methodology should be used to reduce the number of resources being modified simultaneously. With a rolling deployment, changes are made in small batches, with a pre-determined amount of buffer time between batches. If an issue occurs with the deployment, the unchanged resources can continue handling traffic, avoiding downtime.

## Key AWS services
<a name="key-aws-services-13"></a>
+  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+  [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/)

## Resources
<a name="resources-22"></a>
+  [Blue/Green Deployments on AWS](https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/welcome.html)
+  [Rolling deployments](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/rolling-deployments.html)
+  [Deployment methods](Users/jblatch/Downloads/•%20https:/docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/deployment-methods.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
