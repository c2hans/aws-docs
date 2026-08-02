---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_architecture_use_benchmarking.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF01-BP06 Use benchmarking to drive architectural decisions
<a name="perf_architecture_use_benchmarking"></a>

 Benchmark the performance of an existing workload to understand how it performs on the cloud and drive architectural decisions based on that data.

 **Common anti-patterns:**
+  You rely on common benchmarks that are not indicative of your workload’s characteristics.
+  You rely on customer feedback and perceptions as your only benchmark.

 **Benefits of establishing this best practice:** Benchmarking your current implementation allows you to measure performance improvements.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Use benchmarking with synthetic tests to assess how your workload’s components perform. Benchmarking is generally quicker to set up than load testing and is used to evaluate the technology for a particular component. Benchmarking is often used at the start of a new project, when you lack a full solution to load test.

 You can either build your own custom benchmark tests or use an industry standard test, such as [TPC-DS](http://www.tpc.org/tpcds/), to benchmark your workloads. Industry benchmarks are helpful when comparing environments. Custom benchmarks are useful for targeting specific types of operations that you expect to make in your architecture.

 When benchmarking, it is important to pre-warm your test environment to get valid results. Run the same benchmark multiple times to verify that you’ve captured any variance over time.

 Because benchmarks are generally faster to run than load tests, they can be used earlier in the deployment pipeline and provide faster feedback on performance deviations. When you evaluate a significant change in a component or service, a benchmark can be a quick way to see if you can justify the effort to make the change. Using benchmarking in conjunction with load testing is important because load testing informs you about how your workload performs in production.

### Implementation steps
<a name="implementation-steps"></a>
+  Define the metrics (like CPU utilization, latency, or throughput) to evaluate your workload performance.
+  Identify and set up a benchmarking tool that is suitable for your workload. You can use AWS services (like [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)) or a third-party tool that is compatible with your workload.
+  Perform your benchmark tests and monitor the metrics during the test.
+  Analyze and document the benchmarking results to identify any bottlenecks and issues.
+  Use the test results to make architectural decisions and adjust your workload. This may include changing services or adopting new features.
+  Retest your workload after the adjustment.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Architecture Center](https://aws.amazon.com/architecture/)
+  [AWS Partner Network](https://aws.amazon.com/partners/)
+  [AWS Solutions Library](https://aws.amazon.com/solutions/)
+  [AWS Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/)
+  [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)
+  [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)

 **Related videos:**
+  [This is my Architecture](https://aws.amazon.com/architecture/this-is-my-architecture/)
+  [Optimize applications through Amazon CloudWatch RUM](https://www.youtube.com/watch?v=NMaeujY9A9Y)
+  [Demo of Amazon CloudWatch Synthetics](https://www.youtube.com/watch?v=hF3NM9j-u7I)

 **Related examples:**
+  [AWS Samples](https://github.com/aws-samples)
+  [AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)
+  [Distributed Load Tests](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/)
+  [Measure page load time with Amazon CloudWatch Synthetics](https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance)
+  [Amazon CloudWatch RUM Web Client](https://github.com/aws-observability/aws-rum-web)
