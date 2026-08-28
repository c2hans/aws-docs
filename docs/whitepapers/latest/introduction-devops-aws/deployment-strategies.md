---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/deployment-strategies.html
---

# Deployment strategies
<a name="deployment-strategies"></a>

Deployment strategies define how you want to deliver your software. Organizations follow different deployment strategies based on their business model. Some choose to deliver software that is fully tested, and others might want their users to provide feedback and let their users evaluate under development features (such as Beta releases). The following section discusses various deployment strategies.

## In-place deployments
<a name="in-place-deployments"></a>

In this strategy, the previous version of the application on each compute resource is stopped, the latest application is installed, and the new version of the application is started and validated. This allows application deployments to proceed with minimal disturbance to underlying infrastructure. With an in-place deployment, you can deploy your application without creating new infrastructure; however, the availability of your application can be affected during these deployments. This approach also minimizes infrastructure costs and management overhead associated with creating new resources. You can use a load balancer so that each instance is deregistered during its deployment and then restored to service after the deployment is complete. In-place deployments can be all-at-once, assuming a service outage, or done as a rolling update. AWS CodeDeploy and [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)offer deployment configurations for one-at-a-time, half-at-a-time, and all-at-once.

## Blue/green deployment
<a name="blue-green-deployments"></a>

[Blue/green deployment](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/bluegreen-deployments.html), sometimes referred to as red/black deployment, is a technique for releasing applications by shifting traffic between two identical environments running differing versions of the application. Blue/green deployment helps you minimize downtime during application updates, mitigating risks surrounding downtime and rollback functionality.

Blue/green deployments enable you to launch a new version (green) of your application alongside the old version (blue), and monitor and test the new version before you reroute traffic to it, rolling back on issue detection.

## Canary deployment
<a name="canary-deployments"></a>

The purpose of a [canary deployment](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.canary-deployment.en.html) is to reduce the risk of deploying a new version that impacts the workload. The method will incrementally deploy the new version, making it visible to new users in a slow fashion. As you gain confidence in the deployment, you will deploy it to replace the current version in its entirety.

## Linear deployment
<a name="linear-deployments"></a>

Linear deployment means traffic is shifted in equal increments with an equal number of minutes between each increment. You can choose from predefined linear options that specify the percentage of traffic shifted in each increment and the number of minutes between each increment.

## All-at-once deployment
<a name="all-at-once-deployments"></a>

 All-at-once deployment means all traffic is shifted from the original environment to the replacement environment all at once.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
