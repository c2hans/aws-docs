---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/solr-how-differs.html
---

# How Solr migration differs
<a name="solr-how-differs"></a>

Apache Solr stores its index definition in a `schema.xml` file (or a managed schema) and lays out its Lucene segments differently from Elasticsearch and OpenSearch. Because there is no Solr-native snapshot format that the solution can read the way it reads an Elasticsearch or OpenSearch snapshot, the Solr migration path relies on a dedicated reader component.

The **SolrReader** reads the Lucene segment files from your Solr backup in Amazon S3, reconstructs documents from Lucene stored fields in those segments, and translates the Solr `schema.xml` field types into OpenSearch mappings. The translated documents and mappings are then bulk-indexed into the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection by the same Reindex-from-Snapshot (RFS) backfill workers used for other sources. As a result, the operational flow (configure, submit, monitor, validate) is the same as any other backfill migration — only the source preparation and the version string differ.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
