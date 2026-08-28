---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS.html
---

# Amazon ECS
<a name="deploy-container-insights-ECS"></a>

You can use one or both of the following options to enable Container Insights on Amazon ECS clusters:
+ Use the AWS Management Console or the AWS CLI to start collecting cluster-level, task-level, and service-level metrics.
+ Deploy the CloudWatch agent as a daemon service to start collecting of instance-level metrics on clusters that are hosted on Amazon EC2 instances.

**Topics**
+ [Setting up Container Insights on Amazon ECS](deploy-container-insights-ECS-cluster.md)
+ [Setting up Container Insights on Amazon ECS using AWS Distro for OpenTelemetry](deploy-container-insights-ECS-adot.md)
+ [Deploying the CloudWatch agent to collect EC2 instance-level metrics on Amazon ECS](deploy-container-insights-ECS-instancelevel.md)
+ [Deploying the AWS Distro for OpenTelemetry to collect EC2 instance-level metrics on Amazon ECS clusters](deploy-container-insights-ECS-OTEL.md)
+ [Set up FireLens to send logs to CloudWatch Logs](deploy-container-insights-ECS-logs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
