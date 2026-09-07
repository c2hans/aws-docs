---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution.

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters deploys the following components in your AWS account.

 **Depicts Migration Assistant for Amazon OpenSearch Service architecture on AWS**

![migration assistant for amazon opensearch service architecture diagram](https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/images/migration-assistant-for-amazon-opensearch-service-architecture-diagram.png)

**Note**
AWS CloudFormation resources are created from AWS Cloud Development Kit (AWS CDK) constructs.

Migration Assistant 3.x deploys to Amazon Elastic Kubernetes Service (Amazon EKS). The solution has two layers:
+ A **control plane** that manages migration workflows. It includes the Migration Console pod, the Workflow CLI, and the Argo Workflows engine that sequences tasks, retries failures, and tracks state.
+ A **data plane** that performs the actual snapshot, metadata, backfill, capture, and replay work. It includes Reindex-from-Snapshot (RFS) workers, the Capture Proxy, the Traffic Replayer, and Strimzi-managed Apache Kafka for capture and replay.

The high-level process flow for the solution components deployed with the AWS CloudFormation template is as follows:

1.  **Client traffic is directed to the existing source cluster.** For zero-downtime migrations, a Kubernetes Service backed by an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) or [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) routes traffic through the capture proxy fleet, which forwards requests to the source while simultaneously recording them. For backfill-only migrations, this step is skipped.

1.  **The capture proxy replicates traffic to Apache Kafka.** The capture proxy relays traffic to the source cluster and simultaneously replicates the raw request/response streams to Apache Kafka, managed by Strimzi on Amazon EKS. This provides a durable record of all writes during the migration window.

1.  **Snapshot and backfill via Reindex-from-Snapshot.** With continuous traffic capture in place (or after pausing writes), the user submits a migration workflow from the Migration Console using the Workflow CLI. The workflow creates a point-in-time snapshot of the source cluster in [Amazon Simple Storage Service](https://aws.amazon.com/s3) (Amazon S3), migrates metadata (indexes, templates, aliases) to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection, and then launches RFS workers that read directly from the snapshot in Amazon S3 and bulk-index documents into the target.

1.  **Traffic Replayer catches up the target.** After the backfill completes, the Traffic Replayer reads captured traffic from Apache Kafka and replays it against the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection, transforming requests as needed (authentication, index names). The replayer catches the target up to real-time, closing the gap between the snapshot point-in-time and the current state.

1.  **Validate and compare.** The performance and behavior of traffic routed to the source and target clusters are analyzed by reviewing logs, metrics, and document counts in [Amazon CloudWatch](https://aws.amazon.com/cloudwatch), and by running comparison queries from the Migration Console.

1.  **Redirect traffic and decommission.** After confirming the target cluster’s functionality meets expectations, the user redirects clients to the new Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection by updating DNS records, load balancer configuration, or application connection strings. The user keeps the source cluster available as a fallback during a rollback window, then decommissions the source and removes Migration Assistant infrastructure.
