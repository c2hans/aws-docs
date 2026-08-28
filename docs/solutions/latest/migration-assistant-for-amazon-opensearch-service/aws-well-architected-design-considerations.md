---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

This solution uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework benefit this solution.

## Operational excellence
<a name="operational-excellence"></a>

This section describes how we architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).
+ The solution enables users to transition from legacy, self-managed Elasticsearch, OpenSearch, and Apache Solr clusters to Amazon OpenSearch Service and Amazon OpenSearch Serverless NextGen, managed services that significantly reduce the operational burden associated with maintaining outdated systems.
+ Migrations are described once in workflow configuration and executed as Amazon EKS workloads with built-in approval gates, retry logic, and resumable backfill, which makes migrations repeatable and reduces operator guesswork.

## Security
<a name="security"></a>

This section describes how we architected this solution using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).
+ The solution facilitates user migration to Amazon OpenSearch Service and Amazon OpenSearch Serverless NextGen, which are regularly updated to uphold a strong security posture.
+ The Amazon EKS deployment uses [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) so the Migration Console pod and the Argo workflow executor pods authenticate to Amazon OpenSearch Service, Amazon OpenSearch Serverless NextGen, and other AWS services without long-lived credentials.

## Reliability
<a name="reliability"></a>

This section describes how we architected this solution using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).
+ The solution introduces a lightweight proxy layer between the client and the source cluster to capture data reliably using Apache Kafka. This ensures that requests can be replayed on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection, with the flexibility to modify or resend any failed requests.
+ RFS tracks per-shard progress automatically; backfill resumes from the last checkpoint after a failure without restarting completed shards or duplicating documents.

## Performance efficiency
<a name="performance-efficiency"></a>

This section describes how we architected this solution using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).
+ The tools within the solution have been optimized for efficiently capturing and replaying traffic, mitigating the need for horizontal scaling.
+ RFS reads Lucene segment files directly from Amazon S3 snapshots, allowing massive parallelism (one worker per shard) without adding live load on the source cluster.

## Cost optimization
<a name="cost-optimization"></a>

This section describes how we architected this solution using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).
+ The solution provisions CloudFormation stacks designed to operate specifically during migration processes, which can be safely decommissioned post-migration.
+ Migration workloads run as short-lived pods on Amazon EKS, ensuring cost-effectiveness as charges are incurred only for the duration that the pods are active.
+ For those interested in a preliminary local trial, the solution can be evaluated on a local Kubernetes cluster before AWS implementation.

## Sustainability
<a name="sustainability"></a>

This section describes how we architected this solution using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).
+ The solution allows customers to migrate their workloads to Amazon OpenSearch Service and Amazon OpenSearch Serverless NextGen on more environmentally friendly hardware, for example AWS Graviton instance types.
+ Short-lived migration workers on Amazon EKS only consume compute, memory, and storage during active migration phases, reducing idle resource utilization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
