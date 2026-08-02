---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_performing_architecture_cost.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF01-BP03 Factor cost requirements into decisions
<a name="perf_performing_architecture_cost"></a>

 Workloads often have cost requirements for operation. Use internal cost controls to select resource types and sizes based on predicted resource need.

 Determine which workload components could be replaced with fully managed services, such as managed databases, in-memory caches, and ETL services. Reducing your operational workload allows you to focus resources on business outcomes.

 For cost requirement best practices, refer to the *Cost-Effective Resources* section of the [Cost Optimization Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).

 **Common anti-patterns:**
+  You only use one family of instances.
+  You do not evaluate licensed solutions versus open-source solutions
+  You only use block storage.
+  You deploy common software on EC2 instances and Amazon EBS or ephemeral volumes that are available as a managed service.

 **Benefits of establishing this best practice:** Considering cost when making your selections will allow you to enable other investments.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Optimize workload components to reduce cost: Right size workload components and enable elasticity to reduce cost and maximize component efficiency. Determine which workload components can be replaced with managed services when appropriate, such as managed databases, in-memory caches, and reverse proxies.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Architecture Center](https://aws.amazon.com/architecture/)
+  [AWS Partner Network](https://aws.amazon.com/partners/)
+  [AWS Solutions Library](https://aws.amazon.com/solutions/)
+  [AWS Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/)
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)

 **Related videos:**
+  [Introducing The Amazon Builders’ Library (DOP328)](https://www.youtube.com/watch?v=sKRdemSirDM)
+  [This is my Architecture](https://aws.amazon.com/architecture/this-is-my-architecture/)
+  [Optimize performance and cost for your AWS compute (CMP323-R1) ](https://www.youtube.com/watch?v=zt6jYJLK8sg&ref=wellarchitected)

 **Related examples:**
+  [AWS Samples](https://github.com/aws-samples)
+  [AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)
+  [Rightsizing with Compute Optimizer and Memory utilization enabled](https://www.wellarchitectedlabs.com/cost/200_labs/200_aws_resource_optimization/5_ec2_computer_opt/)
+  [AWS Compute Optimizer Demo code](https://github.com/awslabs/ec2-spot-labs/tree/master/aws-compute-optimizer)
