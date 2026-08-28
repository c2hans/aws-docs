---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcops03-bp02.html
---

# DRHCOPS03-BP02 Understand factors that determine your data replication strategy
<a name="drhcops03-bp02"></a>

 Understand the factors that determine your data replication strategy, and implement replication within the boundaries of your data residency requirements to align with disaster recovery objectives, data integrity, and compliance mandates.

 **Desired outcome:** Your data replication strategy, including its technology, process, and policies, are developed and align to your disaster recovery objectives, data integrity and residency requirements, and compliance mandates.

 **Benefits of establishing this best practice:** Having a clear grasp of data replication strategies allows for effective evaluation, optimization, and alignment with disaster recovery objectives, data integrity and residency requirements, and compliance mandates.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-4"></a>
+  Implement data replication between Outposts, Local Zones, and AWS Regions within your cross-border requirements to provide data availability and minimize data loss in case of failures.
+  Evaluate replication technologies like AWS DataSync or third-party solutions based on your workload requirements and RPO targets.
+  Consider multi-site or multi-Region replication for mission-critical workloads to achieve lower RPOs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
