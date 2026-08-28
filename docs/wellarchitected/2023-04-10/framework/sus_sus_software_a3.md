---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sus_sus_software_a3.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS03-BP02 Remove or refactor workload components with low or no use
<a name="sus_sus_software_a3"></a>

Remove components that are unused and no longer required, and refactor components with little utilization to minimize waste in your workload.

 **Common anti-patterns:**
+  You do not regularly check the utilization level of individual components of your workload.
+  You do not check and analyze recommendations from AWS rightsizing tools such as [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/).

 **Benefits of establishing this best practice:** Removing unused components minimizes waste and improves the overall efficiency of your cloud workload.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Review your workload to identify idle or unused components. This is an iterative improvement process which can be initiated by changes in demand or the release of a new cloud service. For example, a significant drop in [AWS Lambda](https://docs.aws.amazon.com/lambda/) function run time can be an indicator of a need to lower the memory size. Also, as AWS releases new services and features, the optimal services and architecture for your workload may change.

 Continually monitor workload activity and look for opportunities to improve the utilization level of individual components. By removing idle components and performing rightsizing activities, you meet your business requirements with the fewest cloud resources.

 **Implementation steps**
+  Monitor and capture the utilization metrics for critical components of your workload (like CPU utilization, memory utilization, or network throughput in [Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)).
+  For stable workloads, check AWS rightsizing tools such as [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) at regular intervals to identify idle, unused, or underutilized components.
+  For ephemeral workloads, evaluate utilization metrics to identify idle, unused, or underutilized components.
+  Retire components and associated assets (like Amazon ECR images) that are no longer needed.
+  Refactor or consolidate underutilized components with other resources to improve utilization efficiency. For example, you can provision multiple small databases on a single [Amazon RDS](https://aws.amazon.com/rds/) database instance instead of running databases on individual under-utilized instances.
+  Understand the [resources provisioned by your workload to complete a unit of work](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/evaluate-specific-improvements.html).

## Resources
<a name="resources"></a>

 **Related documents:**
+ [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)
+  [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+  [Automated Cleanup of Unused Images in Amazon ECR](https://aws.amazon.com/blogs/compute/automated-cleanup-of-unused-images-in-amazon-ecr/)

 **Related examples:**
+ [ Well-Architected Lab - Rightsizing with AWS Compute Optimizer](https://wellarchitectedlabs.com/cost/200_labs/200_aws_resource_optimization/)
+ [ Well-Architected Lab - Optimize Hardware Patterns and Observe Sustainability KPIs ](https://wellarchitectedlabs.com/sustainability/200_labs/200_optimize_hardware_patterns_observe_sustainability_kpis/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
