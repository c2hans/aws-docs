---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/targeted-business-outcomes.html
---

# Objectives
<a name="targeted-business-outcomes"></a>

Implementing the strategies in this guide helps organizations achieve measurable improvements across cost, reliability, and operations:
+ **Reduced infrastructure costs: **Reduce compute spend by up to 30-60% through intelligent node provisioning, Spot and Graviton adoption, right-sizing pod requests, and eliminating extended support charges.
+ **Improved resource utilization: **Drive cluster utilization from the typical 20–30% up to 60–70% by eliminating idle capacity, consolidating underutilized nodes, and enforcing resource quotas.
+ **Maintained application reliability: **Balance cost savings with availability guarantees using Pod Disruption Budgets (PDBs), topology spread constraints, graceful termination policies, and multi-AZ (Availability Zone) Spot diversification.
+ **Operational efficiency: **Reduce manual intervention through automated scaling, Karpenter-driven deprovisioning, off-hours scheduling, and workload placement policies that make cost-optimal decisions without human input.
+ **Observability cost control: **Prevent monitoring spend from scaling linearly with cluster growth by reducing metric cardinality, filtering at source, and disabling unnecessary insights in non-production environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
