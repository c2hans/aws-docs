---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-vdi/performance-testing-and-metrics.html
---

# Performance testing and metrics for large VDI migrations
<a name="performance-testing-and-metrics"></a>

Performance testing an application is an important task for any deployment, and the same concept applies to VDI deployments. To understand the performance requirements, you must plan and define metrics and acceptance criteria. These metrics can either be captured from the current VDI environment, or you can define new service-level agreements (SLAs) for your cloud environment.

Consider the following metrics:
+ Login time
+ Profile loading time
+ Network latency to on premises
+ Local disk performance, such as to support local files or an application cache
+ Network throughput, such as making sure that the maximum network capacity is defined by the chosen instance size

When conducting performance tests, we recommend that you conduct full-scale tests and replicate the size of an average production deployment. Performing performance tests on a small scale can lead to inaccurate results because the impact on shared resources, such as file servers for user profiles or malware signature updates, can be significantly lower.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
