---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/how-this-solution-works.html
---

# How this solution works
<a name="how-this-solution-works"></a>

The Migration Assistant for Amazon OpenSearch Service solution simplifies zero-downtime migrations to Amazon OpenSearch Service and Amazon OpenSearch Serverless NextGen by capturing, replicating, and replaying traffic between source and target clusters. Migration Assistant 3.0 deploys to Amazon Elastic Kubernetes Service (Amazon EKS) and runs migrations as Kubernetes-managed workloads orchestrated by Argo Workflows.

For zero-downtime migrations, client traffic initially flows to the existing source cluster through a Kubernetes Service that routes through the capture proxy fleet. The capture proxy forwards traffic to the source while simultaneously replicating it to Apache Kafka (managed by Strimzi on Amazon EKS) for later replay.

After traffic capture is active, users initiate a Reindex-from-Snapshot (RFS) backfill through the Workflow CLI on the Migration Console pod. RFS creates a point-in-time snapshot of the source cluster in Amazon S3, migrates metadata to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection, and bulk-indexes documents from the snapshot into the target. After backfill completes, users employ the Traffic Replayer to synchronize live traffic on the target. Logs and metrics in Amazon CloudWatch are analyzed to compare the performance and behavior of the source and target, helping ensure that the new setup is functioning as expected. After the comparison is confirmed, client traffic is redirected to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection, allowing for the safe retirement of the old infrastructure.

This solution supports several scenarios, including metadata migration, backfilling historical data, and replicating live traffic. With tools such as the Capture Proxy, Traffic Replayer, Metadata Migration Tool, and Reindex-from-Snapshot (RFS), users can efficiently manage the migration process, helping to ensure that the target environment mirrors the source without disruptions to live services.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
