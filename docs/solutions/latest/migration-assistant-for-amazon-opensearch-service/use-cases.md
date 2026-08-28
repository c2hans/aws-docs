---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/use-cases.html
---

# Use cases
<a name="use-cases"></a>

 **Migrating existing data**

Migration Assistant for Amazon OpenSearch Service offers various options for migrating existing data, including detailed guidance on running a reindex-from-snapshot applicable across all supported migration routes, such as from Elasticsearch 5.6, 6.8, 7.10.2, or 7.17 to OpenSearch 2.19 or OpenSearch 3.x, and from OpenSearch 1.x through 3.x sources to supported Amazon OpenSearch Service or Amazon OpenSearch Serverless NextGen targets.

 **Near real-time migration of HTTP traffic between clusters**

The solution offers you the option to capture data destined for a source cluster and store this data for reuse. A user can replay this data to an Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection in near real-time to migrate as soon as possible, or replay at a later time.

 **Replay traffic to multiple targets**

The solution allows you to capture traffic for replay through multiple instances or in sequential runs, facilitating the validation of diverse cluster workloads and configurations.

 **Precise simulation of your cluster workloads**

The solution allows users to capture and replay traffic either simultaneously with multiple instances, or in separate sequential runs. This feature aids in validating different cluster workloads and configurations. By default, the Traffic Replayer preserves the original concurrency and request rate to accurately simulate production loads, ensuring a fair like-for-like comparison.

 **Migrating from Apache Solr**

Migration Assistant supports migrating from Apache Solr 6.x–9.x to OpenSearch 3.x on Amazon OpenSearch Service or Amazon OpenSearch Serverless NextGen. This includes document backfill from Solr backups with automatic schema translation from Solr field types to OpenSearch mappings. For SolrCloud sources with JSON-format writes, Migration Assistant can also capture live traffic, transform Solr requests into OpenSearch-compatible requests, and replay them to the target. Standalone Solr sources are backfill-only.

 **Migrating to Amazon OpenSearch Serverless NextGen**

Migration Assistant migrates to Amazon OpenSearch Serverless NextGen collections from every supported source. The solution auto-detects the collection type and adjusts behavior for supported NextGen targets: `SEARCH` collections preserve source document IDs, while `TIMESERIES` and `VECTORSEARCH` collections use server-generated IDs. When migrating to a `VECTORSEARCH` collection, `knn_vector` field mappings are automatically converted to Faiss HNSW for Serverless NextGen compatibility, and `model_id` references are removed.

 **Validate target cluster results**

The solution facilitates user comparisons of source and target traffic in terms of accuracy and performance. It captures metrics and logs for analysis, providing users with the necessary confidence to migrate their production traffic to a new target.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
