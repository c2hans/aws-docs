---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_architecture_factor_cost_into_architectural_decisions.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF01-BP03 Factor cost into architectural decisions
<a name="perf_architecture_factor_cost_into_architectural_decisions"></a>

 Factor cost into your architectural decisions to improve resource utilization and performance efficiency of your cloud workload. When you are aware of the cost implications of your cloud workload, you are more likely to leverage efficient resources and reduce wasteful practices.

 **Common anti-patterns:**
+  You only use one family of instances.
+  You do not evaluate licensed solutions against open-source solutions.
+  You do not define storage lifecycle policies.
+  You do not review new services and features of the AWS Cloud.
+  You only use block storage.

 **Benefits of establishing this best practice:** Factoring cost into your decision making allows you to use more efficient resources and explore other investments.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Optimizing workloads for cost can improve resource utilization and avoid waste in a cloud workload. Factoring cost into architectural decisions usually includes right-sizing workload components and enabling elasticity, which results in improved cloud workload performance efficiency.

### Implementation steps
<a name="implementation-steps"></a>
+  Establish cost objectives like budget limits for your cloud workload.
+  Identify the key components (like instances and storage) that drive cost of your workload. You can use [AWS Pricing Calculator](https://calculator.aws/#/) and [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to identify key cost drivers in your workload.
+  Use [Well-Architected cost optimization best practices](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) to optimize these key components for cost.
+  Continually monitor and analyze cost to identify cost optimization opportunities in your workload.
  +  Use [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) to get alerts for unacceptable costs.
  +  Use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) or [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) to get cost optimization recommendations.
  +  Use [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) to get automated cost anomaly detection and root cause analysis.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [A Detailed Overview of the Cost Intelligence Dashboard](https://aws.amazon.com/blogs/aws-cloud-financial-management/a-detailed-overview-of-the-cost-intelligence-dashboard/)
+  [AWS Architecture Center](https://aws.amazon.com/architecture/)
+  [AWS Partner Network](https://aws.amazon.com/partners/)
+  [AWS Solutions Library](https://aws.amazon.com/solutions/)
+  [AWS Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/)

 **Related videos:**
+  [This is my Architecture](https://aws.amazon.com/architecture/this-is-my-architecture/)
+  [Optimize performance and cost for your AWS compute](https://www.youtube.com/watch?v=zt6jYJLK8sg&ref=wellarchitected)

 **Related examples:**
+  [AWS Samples](https://github.com/aws-samples)
+  [AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)
+  [Rightsizing with Compute Optimizer and Memory utilization enabled](https://www.wellarchitectedlabs.com/cost/200_labs/200_aws_resource_optimization/5_ec2_computer_opt/)
+  [AWS Compute Optimizer Demo code](https://github.com/awslabs/ec2-spot-labs/tree/master/aws-compute-optimizer)
