---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Sample-Workloads-ECS.html
---

# (Optional) Set up sample containerized Amazon ECS workloads for Prometheus metric testing
<a name="ContainerInsights-Prometheus-Sample-Workloads-ECS"></a>

To test the Prometheus metric support in CloudWatch Container Insights, you can set up one or more of the following containerized workloads. The CloudWatch agent with Prometheus support automatically collects metrics from each of these workloads. To see the metrics that are collected by default, see [Prometheus metrics collected by the CloudWatch agent](ContainerInsights-Prometheus-metrics.md).

**Topics**
+ [Sample App Mesh workload for Amazon ECS clusters](ContainerInsights-Prometheus-Sample-Workloads-ECS-appmesh.md)
+ [Sample Java/JMX workload for Amazon ECS clusters](ContainerInsights-Prometheus-Sample-Workloads-ECS-javajmx.md)
+ [Sample NGINX workload for Amazon ECS clusters](ContainerInsights-Prometheus-Setup-nginx-ecs.md)
+ [Sample NGINX Plus workload for Amazon ECS clusters](ContainerInsights-Prometheus-Setup-nginx-plus-ecs.md)
+ [Tutorial for adding a new Prometheus scrape target: Memcached on Amazon ECS](ContainerInsights-Prometheus-Setup-memcached-ecs.md)
+ [Tutorial for scraping Redis OSS Prometheus metrics on Amazon ECS Fargate](ContainerInsights-Prometheus-Setup-redis-ecs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
