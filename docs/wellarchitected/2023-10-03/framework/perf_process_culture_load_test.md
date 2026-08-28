---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_process_culture_load_test.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP04 Load test your workload
<a name="perf_process_culture_load_test"></a>

 Load test your workload to verify it can handle production load and identify any performance bottleneck.

 **Common anti-patterns:**
+  You load test individual parts of your workload but not your entire workload.
+  You load test on infrastructure that is not the same as your production environment.
+  You only conduct load testing to your expected load and not beyond, to help foresee where you may have future problems.
+  You perform load testing without consulting the [Amazon EC2 Testing Policy](https://aws.amazon.com/ec2/testing/) and submitting a Simulated Event Submissions Form. This results in your test failing to run, as it looks like a denial-of-service event.

 **Benefits of establishing this best practice:** Measuring your performance under a load test will show you where you will be impacted as load increases. This can provide you with the capability of anticipating needed changes before they impact your workload.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

 Load testing in the cloud is a process to measure the performance of cloud workload under realistic conditions with expected user load. This process involves provisioning a production-like cloud environment, using load testing tools to generate load, and analyzing metrics to assess the ability of your workload handling a realistic load. Load tests must be run using synthetic or sanitized versions of production data (remove sensitive or identifying information). Automatically carry out load tests as part of your delivery pipeline, and compare the results against pre-defined KPIs and thresholds. This process helps you continue to achieve required performance.

### Implementation steps
<a name="implementation-steps"></a>
+  Set up the test environment based on your production environment. You can use AWS services to run production-scale environments to test your architecture.
+  Choose and configure the load testing tool that suits your workload.
+  Define the load testing scenarios and parameters (like test duration and number of users).
+  Perform test scenarios at scale. Take advantage of the AWS Cloud to test your workload to discover where it fails to scale, or if it scales in a non-linear way. For example, use Spot Instances to generate loads at low cost and discover bottlenecks before they are experienced in production.
+  Monitor and record performance metrics (like throughput and response time). Amazon CloudWatch can collect metrics across the resources in your architecture. You can also collect and publish custom metrics to surface business or derived metrics.
+  Analyze the results to identify performance bottlenecks and areas for improvements.
+  Document and report on load testing process and results.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+  [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)
+  [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
+  [Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/welcome.html)

 **Related videos:**
+  [Solving with AWS Solutions: Distributed Load Testing](https://www.youtube.com/watch?v=Y-2rk0sSyOM)
+  [Optimize applications through Amazon CloudWatch RUM](https://www.youtube.com/watch?v=NMaeujY9A9Y)
+  [Demo of Amazon CloudWatch Synthetics](https://www.youtube.com/watch?v=hF3NM9j-u7I)

 **Related examples:**
+  [Distributed Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
