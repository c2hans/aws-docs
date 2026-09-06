---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

This section describes the components and AWS services that make up this solution and the architecture details on how these components work together. These components are meant to accomplish one of the following scenarios:
+  **Metadata migration** - Migrating cluster metadata, such as index settings, aliases, and templates.
+  **Backfill migration** - Migrating existing or historical data from a source to an Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.
+  **Live traffic migration** - Replicating live ongoing traffic from source to an Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.
+  **Comparative tooling** - Comparing the performance and behaviors of an existing cluster with a prospective new one.

In this guide, we focus on the first three scenarios, guiding you through a backfill from a source cluster while concurrently handling live production traffic, which will be captured and replayed to a target on Amazon OpenSearch Service or Amazon OpenSearch Serverless NextGen.

**Important**
Migration strategies aren’t universally applicable. This guide provides instructions based on engineering best practices.

## AWS services in this solution
<a name="aws-services-in-this-solution"></a>

| AWS service | Description |
| --- | --- |
|  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)  |  **Core.** Infrastructure as Code (IaC) templates used to deploy the Amazon EKS cluster, networking, IAM roles, and supporting resources for Migration Assistant. |
|  [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/)  |  **Core.** Provides the managed Kubernetes control plane for running Migration Assistant workloads, including the Migration Console, Workflow Engine, RFS workers, capture proxy pods, and Traffic Replayer pods. |
|  [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)  |  **Core.** A managed search, logging, and analytics service that customers can upgrade to, migrate to, and use to compare the results of a source and target cluster. Migration Assistant supports both Amazon OpenSearch Service domains and Amazon OpenSearch Serverless NextGen collections (`SEARCH`, `TIMESERIES`, and `VECTORSEARCH`) as migration targets. |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  **Core.** Stores snapshots, migration artifacts, and IaC content. The default migrations bucket is mounted read-only on the Migration Console at `/s3/artifacts` for direct artifact access. |
|  [Amazon Elastic Container Registry (Amazon ECR)](https://aws.amazon.com/ecr/)  |  **Core.** Stores container images for Migration Assistant components. Images are mirrored to private Amazon ECR for isolated subnet deployments. |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  |  **Core.** Provides log aggregation, metrics, and dashboards for Migration Assistant pods running on Amazon EKS. CloudWatch dashboards are pre-wired by the deployment. |
|  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)  |  **Supporting.** Securely stores sensitive data, such as basic-auth credentials for source clusters, that is required for Migration Assistant. |
|  [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)  |  **Supporting.** Provides the IAM role used by the Migration Console and Argo workflow executor pods through [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) to authenticate to Amazon OpenSearch Service, Amazon OpenSearch Serverless NextGen, and other AWS services without long-lived credentials. |
|  [Amazon EC2](https://aws.amazon.com/pm/ec2/)  |  **Supporting.** Provides networking and security infrastructure for Migration Assistant including security groups, virtual private clouds, and the bootstrap host used to deploy the solution. |
|  [Amazon Elastic File System](https://aws.amazon.com/efs/)  |  **Supporting.** Persistent storage for retaining captured request and response data and tuples used during traffic replay validation. |
|  [Amazon Elastic Container Service](https://aws.amazon.com/ecs/)  |  **Optional (legacy).** The legacy ECS-based deployment of Migration Assistant remains available in support-only mode for existing deployments. New deployments should use the Amazon EKS deployment. |

## Control plane components
<a name="control-plane"></a>

The control plane manages migration workflows. It runs on Amazon EKS and includes the following components.

### Migration Console
<a name="migration-management-console"></a>

The Migration Console is a Kubernetes pod (`migration-console-0`) on Amazon EKS that provides the operator interface for the Migration Assistant for Amazon OpenSearch Service solution. It hosts the Workflow CLI and the `console` command-line tools used to inspect or manually drive individual migration components during validation and troubleshooting. The Migration Console pod runs under the `migration-console-access-role` Kubernetes service account, which is associated with an IAM role through [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) so the console can authenticate to Amazon OpenSearch Service, Amazon OpenSearch Serverless NextGen, and other AWS services without long-lived credentials. The default Amazon S3 migrations bucket is mounted read-only on the console at `/s3/artifacts` for direct artifact access.

### Workflow CLI
<a name="workflow-cli"></a>

The Workflow CLI is the customer-facing interface for configuring, submitting, approving, and monitoring migrations. You define the migration in workflow configuration once and run `workflow submit` to start it; `workflow manage` provides an interactive monitoring TUI; `workflow approve` releases gated checkpoints. The Workflow CLI is the day-to-day operator interface for the solution.

### Workflow Engine (Argo Workflows)
<a name="workflow-engine"></a>

The workflow engine sequences migration tasks, retries failures, tracks state, and pauses at approval gates. It runs as Argo Workflows on Amazon EKS. The Argo workflow executor pods run under the `argo-workflow-executor` Kubernetes service account, which is associated with an IAM role through [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) so workflow steps can authenticate to Amazon OpenSearch Service, Amazon OpenSearch Serverless NextGen, and other AWS services as the workflow runs.

## Data plane components
<a name="data-plane"></a>

The data plane performs the actual snapshot, metadata, backfill, capture, and replay work. It includes the following components.

### Source cluster
<a name="source-cluster"></a>

The source cluster is based on Elasticsearch, OpenSearch, or Apache Solr, operating on Amazon EC2 instances or alternative computing infrastructure. For zero-downtime migrations, a Capture Proxy is configured to interface with the source cluster, positioning the proxy in front of, or alongside, the cluster’s coordinating nodes.

### Metadata Migration Tool
<a name="metadata-migration-tool"></a>

The Metadata Migration Tool migrates cluster metadata, including index mappings, index configuration settings, templates, component templates, and aliases. It is integrated into the Workflow CLI as the metadata migration phase. Built-in transformations are included for common compatibility issues, including legacy multi-type mapping union, `string` to `text` and `keyword`, `flattened` to `flat_object`, `dense_vector` to `knn_vector`, k-NN vector compatibility for newer OpenSearch and Serverless targets, and analysis-component cleanup for analyzer, tokenizer, char-filter, and token-filter names that changed across versions.

### Capture Proxy
<a name="capture-proxy"></a>

The Capture Proxy is designed for HTTP RESTful traffic. It functions by relaying traffic to a source cluster and concurrently dividing the traffic, replicating it into a durable Apache Kafka stream for subsequent playback. The Capture Proxy runs as pods on Amazon EKS and is fronted by a Kubernetes Service. On Amazon EKS, the Service is backed by AWS load-balancer infrastructure (Application Load Balancer or Network Load Balancer), and the bootstrap path handles the platform wiring for you.

### Traffic Replayer
<a name="traffic-replayer"></a>

The Traffic Replayer is a network traffic utility that replicates real-world workloads by retrieving recorded request traffic and dispatching it to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. It associates the original requests and their responses with those directed to the target, which helps to compare correlated data.

### Reindex-from-Snapshot (RFS)
<a name="reindex-from-snapshot-container"></a>

Reindex-from-Snapshot (RFS) is the high-performance backfill engine. RFS reads the raw Lucene segment files directly from a snapshot in Amazon S3, applies any configured transformations, and bulk-indexes documents into the target on Amazon OpenSearch Service or Amazon OpenSearch Serverless NextGen. RFS runs as Amazon EKS pods, with one worker per shard for massive parallelism. Because RFS reads from snapshot storage rather than the source cluster API, scaling backfill workers does not add live load on the source cluster.

### Strimzi (Apache Kafka operator)
<a name="strimzi-kafka"></a>

Strimzi manages Apache Kafka on Amazon EKS for capture and replay workflows. The Capture Proxy writes captured request/response streams to Apache Kafka topics, and the Traffic Replayer consumes from those topics to replay traffic against the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

### Target
<a name="target-cluster"></a>

The target is the destination Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection for migration or comparison in an A/B test. This target must exist prior to deploying this solution.
