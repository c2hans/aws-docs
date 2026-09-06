---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_tradeoffs_performance_measure.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF08-BP04 Measure the impact of performance improvements
<a name="perf_tradeoffs_performance_measure"></a>

 As changes are made to improve performance, evaluate the collected metrics and data. Use this information to determine impact that the performance improvement had on the workload, the workload’s components, and your customers. This measurement helps you understand the improvements that result from the tradeoff, and helps you determine if any negative side-effects were introduced.

 A well-architected system uses a combination of performance related strategies. Determine which strategy will have the largest positive impact on a given hotspot or bottleneck. For example, sharding data across multiple relational database systems could improve overall throughput while retaining support for transactions and, within each shard, caching can help to reduce the load.

 **Common anti-patterns:**
+  You deploy and manage technologies manually that are available as managed services.
+  You focus on just one component, such as networking, when multiple components could be used to increase performance of the workload.
+  You rely on customer feedback and perceptions as your only benchmark.

 **Benefits of establishing this best practice:** For implementing performance strategies, you must select multiple services and features that, taken together, will allow you to meet your workload requirements for performance.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 A well-architected system uses a combination of performance-related strategies. Determine which strategy will have the largest positive impact on a given hotspot or bottleneck. For example, sharding data across multiple relational database systems could improve overall throughput while retaining support for transactions and, within each shard, caching can help to reduce the load.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon Builders’ Library](https://aws.amazon.com/builders-library)
+  [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)
+  [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
+  [Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/welcome.html)

 **Related videos:**
+  [Introducing The Amazon Builders’ Library (DOP328)](https://www.youtube.com/watch?v=sKRdemSirDM)
+  [Optimize applications through Amazon CloudWatch RUM](https://www.youtube.com/watch?v=NMaeujY9A9Y)
+  [Demo of Amazon CloudWatch Synthetics](https://www.youtube.com/watch?v=hF3NM9j-u7I)

 **Related examples:**
+  [Measure page load time with Amazon CloudWatch Synthetics](https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance)
+  [Amazon CloudWatch RUM Web Client](https://github.com/aws-observability/aws-rum-web)
+  [Distributed Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/)
