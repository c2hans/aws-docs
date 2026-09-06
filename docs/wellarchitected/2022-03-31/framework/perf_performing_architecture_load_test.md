---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_performing_architecture_load_test.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF01-BP07 Load test your workload
<a name="perf_performing_architecture_load_test"></a>

 Deploy your latest workload architecture on the cloud using different resource types and sizes. Monitor the deployment to capture performance metrics that identify bottlenecks or excess capacity. Use this performance information to design or improve your architecture and resource selection.

 Load testing uses your *actual* workload so that you can see how your solution performs in a production environment. Load tests must be run using synthetic or sanitized versions of production data (remove sensitive or identifying information). Use replayed or pre-programmed user journeys through your workload at scale that exercise your entire architecture. Automatically carry out load tests as part of your delivery pipeline, and compare the results against pre-defined KPIs and thresholds. This ensures that you continue to achieve required performance.

 **Common anti-patterns:**
+  You load test individual parts of your workload but not your entire workload.
+  You load test on infrastructure that is not the same as your production environment.
+  You only conduct load testing to your expected load and not beyond, to help foresee where you may have future problems.
+  Performing load testing without informing AWS Support, and having your test defeated as it looks like a denial of service event.

 **Benefits of establishing this best practice:** Measuring your performance under a load test will show you where you will be impacted as load increases. This can provide you with the capability of anticipating needed changes before they impact your workload.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

 Validate your approach with load testing: Load test a proof-of-concept to find out if you meet your performance requirements. You can use AWS services to run production-scale environments to test your architecture. Because you only pay for the test environment when it is needed, you can carry out full-scale testing at a fraction of the cost of using an on-premises environment.

 Monitor metrics: Amazon CloudWatch can collect metrics across the resources in your architecture. You can also collect and publish custom metrics to surface business or derived metrics. Use CloudWatch or third-party solutions to set alarms that indicate when thresholds are breached.

 Test at scale: Load testing uses your actual workload so you can see how your solution performs in a production environment. You can use AWS services to run production-scale environments to test your architecture. Because you only pay for the test environment when it is needed, you can run full-scale testing at a lower cost than using an on-premises environment. Take advantage of the AWS Cloud to test your workload to discover where it fails to scale, or if it scales in a non-linear way. For example, use Spot Instances to generate loads at low cost and discover bottlenecks before they are experienced in production.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+  [Building AWS CloudFormation Templates using CloudFormer](https://aws.amazon.com/blogs/devops/building-aws-cloudformation-templates-using-cloudformer/)
+  [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)
+  [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
+  [Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/welcome.html)

 **Related videos:**
+  [Introducing The Amazon Builders’ Library (DOP328)](https://www.youtube.com/watch?v=sKRdemSirDM)
+  [Optimize applications through Amazon CloudWatch RUM](https://www.youtube.com/watch?v=NMaeujY9A9Y)
+  [Demo of Amazon CloudWatch Synthetics](https://www.youtube.com/watch?v=hF3NM9j-u7I)

 **Related examples:**
+  [Distributed Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/)
