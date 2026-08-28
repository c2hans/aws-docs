---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops02-bp04.html
---

# ADVOPS02-BP04 Instrument your advertising application code and infrastructure to emit detailed, structured logs and metrics
<a name="advops02-bp04"></a>

 Instrument your advertising application code and infrastructure to emit detailed, structured logs and metrics to achieve comprehensive visibility into advertising workloads. Organizations can monitor all components of their workloads, define KPIs, and set up alerts for critical metrics by using observability services like Amazon CloudWatch. This structured approach enables teams to detect, diagnose, and resolve issues quickly. This approach also optimizes performance and reliability of advertising campaigns.

## Implementation guidance
<a name="implementation-guidance-6"></a>

 To gain comprehensive visibility into your advertising workload and quickly detect, diagnose and resolve issues, use the following logging strategy:
+  Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and [AWS X-Ray](https://aws.amazon.com/xray/) to capture key performance metrics, error rates, latency data, and detailed logs from ad serving infrastructure.
+  Centralize all logs from the advertising stack, including third-party integrations and partner platforms, using a log aggregation solution like Amazon CloudWatch Logs.
+  Implement distributed tracing with AWS X-Ray to track user journeys and identify performance bottlenecks across advertising applications and services.
+  Integrate with ad tech platforms and partners to receive comprehensive event-level data like bid requests, ad impressions, and conversions to power observability and analytics.

## Resources
<a name="resources-6"></a>
+  [Observability using native Amazon CloudWatch and AWS X-Ray for serverless modern applications](https://aws.amazon.com/blogs/mt/observability-using-native-amazon-cloudwatch-and-aws-x-ray-for-serverless-modern-applications/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
