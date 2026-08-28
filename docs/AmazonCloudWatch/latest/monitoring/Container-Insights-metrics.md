---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics.html
---

# Metrics collected by Container Insights
<a name="Container-Insights-metrics"></a>

Container Insights collects one set of metrics for Amazon ECS and AWS Fargate on Amazon ECS, and a different set for Amazon EKS, AWS Fargate on Amazon EKS, RedHat OpenShift on AWS (ROSA), and Kubernetes.

Metrics are not visible until the container tasks have been running for some time.

**Topics**
+ [Amazon ECS Container Insights with enhanced observability metrics](Container-Insights-enhanced-observability-metrics-ECS.md)
+ [Amazon ECS Container Insights metrics](Container-Insights-metrics-ECS.md)
+ [Amazon EKS and Kubernetes Container Insights with enhanced observability metrics](Container-Insights-metrics-enhanced-EKS.md)
+ [Amazon EKS and Kubernetes Container Insights metrics](Container-Insights-metrics-EKS.md)
+ [Container Insights performance log reference](Container-Insights-reference.md)
+ [Container Insights Prometheus metrics monitoring](ContainerInsights-Prometheus.md)
+ [Integration with Application Insights](container-insights-appinsights.md)
+ [Viewing Amazon ECS lifecycle events within Container Insights](container-insights-ECS-lifecycle-events.md)
+ [Troubleshooting Container Insights](ContainerInsights-troubleshooting.md)
+ [Building your own CloudWatch agent Docker image](ContainerInsights-build-docker-image.md)
+ [Deploying other CloudWatch agent features in your containers](ContainerInsights-other-agent-features.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
