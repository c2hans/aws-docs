---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-other-agent-features.html
---

# Deploying other CloudWatch agent features in your containers
<a name="ContainerInsights-other-agent-features"></a>

You can deploy additional monitoring features in your containers using the CloudWatch agent. These features include the following:
+ **Embedded Metric Format**— For more information, see [Embedding metrics within logs](CloudWatch_Embedded_Metric_Format.md).
+ **StatsD**— For more information, see [Retrieve custom metrics with StatsD](CloudWatch-Agent-custom-metrics-statsd.md).

Instructions and necessary files are located on GitHub at the following locations:
+ For Amazon ECS containers, see [ Example Amazon ECS task definitions based on deployment modes](https://github.com/aws-samples/amazon-cloudwatch-container-insights/tree/latest/ecs-task-definition-templates/deployment-mode).
+ For Amazon EKS and Kubernetes containers, see [ Example Kubernetes YAML files based on deployment modes](https://github.com/aws-samples/amazon-cloudwatch-container-insights/tree/latest/k8s-deployment-manifest-templates/deployment-mode).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
