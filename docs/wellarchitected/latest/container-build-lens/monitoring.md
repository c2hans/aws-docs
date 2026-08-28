---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/monitoring.html
---

# Monitoring
<a name="monitoring"></a>

| CONTAINER\_BUILD\_PERF\_05: How do you make sure you get consistent performance results over time? |
| --- |
|   |

 **Implement an automated performance testing strategy**

 System performance can degrade over time. It’s important to have an automated testing and monitoring system in place to identify degradation of performance. Every time you build target images based on new parent images, you should measure the performance impact of the changes in the parent image. This also includes the overall build process, because we have to make sure that a testing and monitoring system covers the CI/CD chain. Performance metrics and image sizes have to be collected using services like Amazon CloudWatch and teams must be alarmed if [anomalies](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) have been detected.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
