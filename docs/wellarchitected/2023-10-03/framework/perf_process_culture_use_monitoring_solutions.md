---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_process_culture_use_monitoring_solutions.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP02 Use monitoring solutions to understand the areas where performance is most critical
<a name="perf_process_culture_use_monitoring_solutions"></a>

 Understand and identify areas where increasing the performance of your workload will have a positive impact on efficiency or customer experience. For example, a website that has a large amount of customer interaction can benefit from using edge services to move content delivery closer to customers.

 **Common anti-patterns:**
+  You assume that standard compute metrics such as CPU utilization or memory pressure are enough to catch performance issues.
+  You only use the default metrics recorded by your selected monitoring software.
+  You only review metrics when there is an issue.

 **Benefits of establishing this best practice:** Understanding critical areas of performance helps workload owners monitor KPIs and prioritize high-impact improvements.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Set up end-to-end tracing to identify traffic patterns, latency, and critical performance areas. Monitor your data access patterns for slow queries or poorly fragmented and partitioned data. Identify the constrained areas of the workload using load testing or monitoring.

 Increase performance efficiency by understanding your architecture, traffic patterns, and data access patterns, and identify your latency and processing times. Identify the potential bottlenecks that might affect the customer experience as the workload grows. After investigating these areas, look at which solution you could deploy to remove those performance concerns.

### Implementation steps
<a name="implementation-steps"></a>

1.  Set up end-to-end monitoring to capture all workload components and metrics. Here are examples of monitoring solutions on AWS.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_process_culture_use_monitoring_solutions.html)

1.  Perform tests to generate metrics, identify traffic patterns, bottlenecks, and critical performance areas. Here are some examples of how to perform testing:
   +  Set up [CloudWatch Synthetic Canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) to mimic browser-based user activities programmatically using Linux cron jobs or rate expressions to generate consistent metrics over time.
   +  Use the [AWS Distributed Load Testing](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) solution to generate peak traffic or test the workload at the expected growth rate.

1.  Evaluate the metrics and telemetry to identify your critical performance areas. Review these areas with your team to discuss monitoring and solutions to avoid bottlenecks.

1.  Experiment with performance improvements and measure those changes with data. As an example, you can use [CloudWatch Evidently](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently.html) to test new improvements and performance impacts to your workload.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon Builders’ Library](https://aws.amazon.com/builders-library)
+  [X-Ray Documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
+  [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)
+  [Amazon DevOps Guru](https://aws.amazon.com/devops-guru/)

 **Related videos:**
+  [The Amazon Builders’ Library: 25 years of Amazon operational excellence](https://www.youtube.com/watch?v=DSRhgBd_gtw)
+  [Visual Monitoring of Applications with Amazon CloudWatch Synthetics](https://www.youtube.com/watch?v=_PCs-ucZz7E)

 **Related examples:**
+  [Measure page load time with Amazon CloudWatch Synthetics](https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance)
+  [Amazon CloudWatch RUM Web Client](https://github.com/aws-observability/aws-rum-web)
+  [X-Ray SDK for Node.js](https://github.com/aws/aws-xray-sdk-node)
+  [X-Ray SDK for Python](https://github.com/aws/aws-xray-sdk-python)
+  [X-Ray SDK for Java](https://github.com/aws/aws-xray-sdk-java)
+  [X-Ray SDK for .Net](https://github.com/aws/aws-xray-sdk-dotnet)
+  [X-Ray SDK for Ruby](https://github.com/aws/aws-xray-sdk-ruby)
+  [X-Ray Daemon](https://github.com/aws/aws-xray-daemon)
+  [Distributed Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
