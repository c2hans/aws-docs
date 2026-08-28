---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/index-data-loading.html
---

# Data loading strategies
<a name="index-data-loading"></a>

## Initial data migration
<a name="loading-initial"></a>

The initial data migration represents the most critical phase of your Amazon OpenSearch Service migration. It requires careful orchestration to ensure data integrity while minimizing service disruption. The initial data migration consists of four phases.

**Phase 1: Pre-migration preparation**. This phase involves coordination with application teams to schedule maintenance windows and implement write operation controls. Tasks include:
+ Implementing application-level read-only modes to prevent new data modifications.
+ Ensuring that all pending transactions are completed before proceeding.
+ Documenting the timestamp when write operations are suspended.
+ Communicating status to all stakeholders throughout the process.

**Phase 2: Data transfer**. In this phase, you run your chosen extraction method while maintaining comprehensive monitoring. Tasks include:
+ Implementing progress tracking and logging for visibility into transfer status.
+ Configuring checkpointing mechanisms to enable recovery from interruptions.
+ Monitoring AWS service quotas and requesting increases if necessary.
+ Maintaining detailed audit logs for compliance and troubleshooting purposes.

**Phase 3: Data validation and verification**. This phase includes both quantitative and functional validation.

Quantitative validation:
+ Compare document counts between source Solr and destination Amazon OpenSearch Service.
+ Validate field mappings and data types across representative document samples.
+ Execute checksum or hash comparisons for critical data fields.
+ Verify index statistics and storage utilization metrics.

Functional validation:
+ Run representative search queries against both systems.
+ Compare search result relevance and ranking.
+ Validate faceting, aggregation, and filtering functionality.
+ Test application-specific search features and use cases.

**Phase 4: Application cutover**. This phase requires updating your application configurations to use Amazon OpenSearch Service:
+ Update connection strings and endpoint configurations.
+ Modify query syntax for Amazon OpenSearch Service compatibility.
+ Update authentication and authorization configurations for AWS Identity and Access Management (IAM).
+ Implement gradual traffic shifting where possible to minimize risk.

Before you cut over, make sure that comprehensive monitoring mechanisms are in place:
+ Configure Amazon CloudWatch dashboards for key performance indicators.
+ Set up CloudWatch alarms for critical metrics.
+ Implement AWS X-Ray tracing for application performance monitoring.
+ Configure AWS CloudTrail logging for audit and compliance requirements.

## Incremental data synchronization
<a name="loading-incremental"></a>

For scenarios where data modifications occurred during migration, implement change data capture (CDC) mechanisms by using AWS Database Migration Service (AWS DMS) or Amazon Kinesis Data Streams.
+ For relational database sources, use AWS DMS to capture and replicate ongoing changes:
  + Configure AWS DMS tasks for continuous replication.
  + Implement transformation rules for Amazon OpenSearch Service compatibility.
  + Monitor replication lag and performance metrics.
  + Handle data type conversions and schema differences.
+ For high-velocity data sources, use Amazon Kinesis Data Streams integration to implement real-time change streaming.

## Best practices and recommendations
<a name="loading-best-practices"></a>
+ For fast data ingestion, disable replica shards to increase the indexing rate. After data is ingested, you can enable the desired number of shards.
+ Implement least-privilege access principles for all migration components.
+ For data encryption:
  + Configure encryption for data in transit and at rest.
  + Enable Amazon OpenSearch Service domain encryption at rest by using AWS Key Management Service (AWS KMS).
  + Configure node-to-node encryption for inter-cluster communication.
  + Use SSL/TLS for all client connections to Amazon OpenSearch Service.
  + Encrypt data that's stored in Amazon S3 during the migration process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
