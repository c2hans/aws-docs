---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/data-flow.html
---

# Data flow
<a name="data-flow"></a>

The data flow focus area includes the following three areas:
+ Data ingestion
+ Data retention
+ Data migration approach

## Data ingestion
<a name="data-ingestion"></a>

Data ingestion focuses on how to get data into your Amazon OpenSearch Service domain. A thorough understanding of the data sources and formats is paramount when choosing the right ingestion framework for OpenSearch.

There are many different ways to create or modernize your ingestion design. There are many open-source tools for building a self-managed ingestion pipeline. OpenSearch Service supports integration with [Fluentd](https://www.fluentd.org/), [Logstash](https://github.com/opensearch-project/logstash-output-opensearch), or [OpenSearch Data Prepper](https://opensearch.org/docs/latest/data-prepper/index/). These tools are popular with most log analytics solutions developers. You can deploy these tools on an Amazon EC2 instance, on Amazon Elastic Kubernetes Service (Amazon EKS), or on premises. Both Logstash and Fluentd support Amazon OpenSearch Service domains as an output destination. However, this will require you to maintain, patch, test, and keep the Fluentd or Logstash software versions up to date.

To reduce your operational overhead, you can use one of the AWS managed services that support integration with Amazon OpenSearch Service. For example, [Amazon OpenSearch Ingestion](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion.html) is a fully managed, serverless data collector that delivers real-time log, metric, and trace data to Amazon OpenSearch Service domains. With OpenSearch Ingestion, you no longer need to use third-party solutions like Logstash or [Jaeger](https://www.jaegertracing.io/) to ingest data into your OpenSearch Service domains. You configure your data producers to send data to OpenSearch Ingestion. Then, it automatically delivers the data to the domain or collection that you specify. You can also configure OpenSearch Ingestion to transform your data before delivering it.

Another option is [Amazon Kinesis Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html), which is a fully managed service that helps build a serverless ingestion pipeline. Kinesis Data Firehose provides a secure way to ingest, transform, and [deliver streaming data to Amazon OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations.html). It can automatically scale to match the throughput of your data, and it requires no ongoing administration. Kinesis Data Firehose can also transform incoming records by using AWS Lambda, compress, and batch the data before loading it into your OpenSearch Service domain.

With a managed service, you can retire your existing data ingestion pipeline, or you can augment your current setup to reduce operational overhead.

Migration planning is a good time to assess whether your current ingestion pipeline meets the needs of current and future use cases. If you are migrating from a self-managed Elasticsearch or OpenSearch cluster, your ingestion pipeline should support swapping the endpoints from the current cluster to the Amazon OpenSearch Service domain with minimal client library updates.

## Data retention
<a name="data-retention"></a>

When planning for data ingestion and storage, be sure to plan and agree on data retention. For log analytics use cases, it's critical that you have right policies created within your domain to retire the historic data. When you are moving from an existing on-premises and cloud VM based architecture, you could be using a particular type of instance for all your data nodes. Data nodes have same CPU, memory, and storage profile. Most customers would configure high throughput storage to cater to their high-speed indexing requirement. This singular storage profile architecture is called *hot node only* architecture, or hot-only. Hot-only architecture couples storage with compute, which implies that you need to add compute nodes if your storage requirement increases.

To decouple storage from compute, Amazon OpenSearch Service offers the UltraWarm storage tier. UltraWarm provides a cost-effective way to store read-only data on Amazon OpenSearch Service by providing nodes that can accommodate a larger volume of data than traditional data nodes.

During planning, decide the data retention and processing requirement. To reduce the cost of your existing solution, take advantage of the UltraWarm tier. Identify the retention requirement for your data. Then create *Index state management policies* to move data from hot to warm or to delete the data automatically from the domain when not needed. This also helps to ensure that your domain does not run out of storage.

## Data migration approaches
<a name="data-migration-approaches"></a>

During the planning stage, it's critical that you decide on a particular data migration approach. Your data migration approach dictates how you move the data that is in your current data store to the target store without any gaps. The procedural details for these approaches are covered in the [Stage 4 – Data migration](stage-4-data-migration.md) section, which is when you implement your approach.

This section covers different ways and patterns that you can use to migrate an Elasticsearch or OpenSearch cluster to Amazon OpenSearch Service. When choosing a pattern, consider the following list of factors (not exhaustive):
+ Whether you want to copy data from an existing self-managed cluster or you are rebuilding from original the data source (log files, product catalog database)
+ Version compatibility of the source Elasticsearch or OpenSearch cluster and target Amazon OpenSearch Service domain
+ Applications and services dependent on the Elasticsearch or OpenSearch cluster
+ The available window for the migration
+ The volume of indexed data in your existing environment

### Build from a snapshot
<a name="build-from-a-snapshot.4b85c57f-d207-5fd5-a667-27d75fcda4b3"></a>

Snapshots are the most popular way to migrate from a self-managed Elasticsearch cluster to Amazon OpenSearch Service. Snapshots provide a way to back up your OpenSearch or Elasticsearch data by using a durable storage service such as Amazon S3. With this approach, you take snapshot of your current Elasticsearch or OpenSearch environment and restore it in the target Amazon OpenSearch Service environment. After restoring the snapshot, you can point your application to the new environment. This is a faster solution in the following situations:
+ Your source and target are compatible.
+ The existing cluster contains a large volume of indexed data, which can be time consuming to reindex.
+ Your source data is not available for reindexing.

For additional considerations, see* Snapshot considerations* in the [Stage 4 – Data migration](stage-4-data-migration.md) section.

### Build from the source
<a name="build-from-the-source.5c511657-b2dd-5394-b37f-5306116be68f"></a>

This approach implies that you are not going to move data from your current Elasticsearch or OpenSearch cluster. Instead, you reload the data directly from your log or product catalog source to the target Amazon OpenSearch Service domain. This is generally done with minor changes to existing data ingestion pipelines. In the log analytics use case, building from the source might also require reloading the historical logs from your sources to the new OpenSearch Service environment. For search use cases, it might require that you reload your full product catalog and content to the new Amazon OpenSearch Service domain. This approach works well in the following scenarios:
+ Your source and target environment versions are not compatible for snapshot restore.
+ You want to change your data model in the target environment as part of the migration.
+ You want to jump to the most recent version of Amazon OpenSearch Service to avoid rolling upgrades, and you want to address the breaking changes in one go. This can be a good idea if you are self-managing a relatively older version (5.x or earlier) of Elasticsearch.
+ You may want to change your indexing strategy. For example, instead of rolling over every day, you might roll over every month in the new environment.

For information about options for building from the source, see *2. Building from the source* in the [Stage 4 – Data migration](stage-4-data-migration.md) section.

### Reindex remotely from an existing Elasticsearch or OpenSearch environment
<a name="reindex-remotely-from-an-existing-elasticsearch-or-opensearch-environment.0e442402-f8e4-55b4-a995-0bd89220ad17"></a>

This approach uses the [remote reindex API](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/remote-reindex.html) from Amazon OpenSearch Service. Using remote reindex, you can copy data directly from your existing on-premises or cloud-based Elasticsearch or OpenSearch cluster to your Amazon OpenSearch Service domain. You can build automation that can keep the data synchronized between the two environment locations until you cut over to the target environment.

### Use open-source data migration tools
<a name="use-open-source-data-migration-tools.c2a24d30-bcc7-5413-8c5b-6e965d0bac2c"></a>

There are multiple open source tools available to migrate data from your existing Elasticsearch environment to your target Amazon OpenSearch environment. One such example is the Logstash utility. You can use the Logstash utility to extract data from an Elasticsearch or OpenSearch cluster and copy it to the Amazon OpenSearch Service domain.

We recommend that you evaluate all your options and opt for the one that you are most comfortable with. To ensure that your selected approach is fool-proof, test all your tools and automation during your PoC stage. For details and step-by-step guidance on how to implement these approaches, see the [Stage 4 – Data migration](stage-4-data-migration.md) section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
