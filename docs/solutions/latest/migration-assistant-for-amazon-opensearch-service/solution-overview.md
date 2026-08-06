---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/solution-overview.html
---

# Build an environment to upgrade, migrate, and compare OpenSearch clusters
<a name="solution-overview"></a>

**Tip**
For a guided, conversational experience that handles configuration generation, schema extraction, and troubleshooting automatically, use Migration Assistant AI agent mode. See [AI-assisted migration](agent-assisted-migration.md).

OpenSearch is widely adopted for log analytics and search. However, self-managing OpenSearch can be operationally demanding. Amazon OpenSearch Service and Amazon OpenSearch Serverless NextGen offer more manageable alternatives, but transitioning to these services or updating to the latest OpenSearch version has historically been complex. It can also be difficult to predict the outcome of a migration before production traffic moves. The Migration Assistant for Amazon OpenSearch Service solution addresses these challenges by making migration workflow-driven, repeatable, and easier to validate before cutover.

The Migration Assistant for Amazon OpenSearch Service solution is a workflow-driven toolkit designed to ease the transition to Amazon OpenSearch Service and Amazon OpenSearch Serverless NextGen, facilitate upgrades to the latest OpenSearch versions, and refine cluster configurations based on observed traffic patterns. Migration Assistant 3.0 deploys to Amazon Elastic Kubernetes Service (Amazon EKS) and runs migrations as Kubernetes-managed workloads. Whether you’re looking to set up a proof-of-concept in AWS, transition production workloads with confidence, or enhance your current OpenSearch clusters, this guide provides step-by-step instructions, best practices, and insights to help you migrate to Amazon OpenSearch Service or Amazon OpenSearch Serverless NextGen.

 **Supported migration paths**

The following matrix shows which source versions can be directly migrated to which Amazon OpenSearch Service or Amazon OpenSearch Serverless NextGen target versions:

| Source version | OpenSearch 1.x | OpenSearch 2.x | OpenSearch 3.x | Amazon OpenSearch Serverless NextGen |
| --- | --- | --- | --- | --- |
| Elasticsearch 1.x–2.x | ✓\* | ✓\* | ✓\* | ✓\* |
| Elasticsearch 5.x–7.x | ✓ | ✓ | ✓ | ✓\*\* |
| Elasticsearch 8.x |  | ✓ | ✓ | ✓\*\* |
| OpenSearch 1.x–2.x |  | ✓ | ✓ | ✓\*\* |
| OpenSearch 3.x |  |  | ✓ | ✓\*\* |
| Apache Solr 6.x–9.x |  |  | ✓**\***  | ✓**\***  |

**Note**
\* Elasticsearch 1.x–2.x migrations are backfill only. Live traffic capture and replay is not supported for those source versions.

**Note**
\*\* Live traffic capture and replay is supported with Amazon OpenSearch Serverless NextGen targets when the source supports it. Document IDs are preserved on `SEARCH` collections. `TIMESERIES` and `VECTORSEARCH` collections use server-generated IDs, so replay cannot reconcile updates or deletes by source `_id` on those collection types.

**Note**
 **\*** Backfill and live traffic capture and replay are supported for Apache Solr sources running in SolrCloud mode. Capture and replay requires JSON-format write requests. See [Capture and replay live traffic from Solr](solr-capture-replay.md).

<a name="get-started"></a> **Get started**

Migration Assistant includes two operating modes: an AI-assisted agent and a manual Workflow CLI. Choose the path that matches how much guidance and automation you want during assessment, deployment, workflow configuration, and migration.

| Path | Use when | Start here |
| --- | --- | --- |
| AI-assisted migration | You want a guided, conversational experience that can help assess your source cluster, deploy Migration Assistant, generate workflow configuration, run the migration, and troubleshoot issues. |  [AI-assisted migration](agent-assisted-migration.md)  |
| Manual Workflow CLI | You want direct control over deployment, workflow JSON, CLI commands, approval gates, validation, and operational troubleshooting. |  [Prepare for migration](prepare-for-migration.md)  |

If this is your first migration, start with [AI-assisted migration](agent-assisted-migration.md). The agent can guide you through assessment, deployment, configuration, and execution. If you prefer to operate each step yourself, start with [Prepare for migration](prepare-for-migration.md) and then use the manual workflow path in [Run workflows](use-the-solution.md).

 **Benefits of using this solution:**
+ Migrate cluster metadata, including index settings, type mappings, index templates, and aliases.
+ Migrate existing data from legacy Elasticsearch, OpenSearch, and Apache Solr clusters to Amazon OpenSearch Service domains and Amazon OpenSearch Serverless NextGen collections.
+ Use AI-assisted migration to guide source assessment, deployment, workflow generation, migration execution, and troubleshooting.
+ Intercept and redirect live traffic from supported self-managed Elasticsearch, OpenSearch, and SolrCloud sources to Amazon OpenSearch Service domains and Amazon OpenSearch Serverless NextGen collections with minimal latency.
+ Replicate production traffic on target clusters to validate and ensure accuracy.
+ Simulate real-world traffic by capturing and replaying request patterns to fine-tune system performance.
+ Deploy across the most common AWS Regions for global reach and scalability.
+ Provides a recommended path for migration while continuing to maintain service availability.
+ Run migrations as repeatable, workflow-driven Amazon EKS workloads with built-in approval gates, retry logic, and resumable backfill.

This implementation guide provides an overview of the Migration Assistant for Amazon OpenSearch Service solution, its reference architecture and components, considerations for planning the deployment, and configuration steps for deploying the solution to the Amazon Web Services (AWS) Cloud. It also references the solution’s open-source documentation, which includes developer documentation and tips to enhance and contribute to the solution.

The intended audience for using this solution’s features and capabilities in their environment includes solution architects, business decision makers, DevOps engineers, data scientists, and cloud professionals.

To follow the migration story end to end, read this guide in this order:

1.  [Solution overview](#solution-overview) - confirm the supported migration path and core concepts.

1.  [Prepare for migration](prepare-for-migration.md) - understand the architecture, plan the deployment, and deploy Migration Assistant.

1.  [Run a migration](run-a-migration.md) - configure workflows, follow a playbook, migrate data, replay traffic, monitor progress, troubleshoot issues, cut over, and remove the solution after the rollback window.

1.  [Reference](reference.md) - review source, release, legal, and data-collection reference material.

For specific planning and reference questions, use the following table:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this solution.<br />Costs depend on migration duration, data volume, target type, and whether you run capture and replay. For current sample estimates, see [Cost](cost.md). |  [Cost](cost.md)  |
| Understand the security considerations for this solution. |  [Security](security-1.md)  |
| Know how to plan for quotas for this solution. |  [Quotas](quotas.md)  |
| Know which AWS Regions support this solution. |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
| View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution. |  +   [Launch with a new VPC](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/migration-assistant-for-amazon-opensearch-service/latest/migration-assistant-for-amazon-opensearch-service-create-vpc-eks.template)  <br />+   [Launch into an existing VPC](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/migration-assistant-for-amazon-opensearch-service/latest/migration-assistant-for-amazon-opensearch-service-import-vpc-eks.template&redirectId)    |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. |  [Migration Assistant documentation](https://docs.aws.amazon.com/solutions/migration-assistant-for-amazon-opensearch-service/)  |
