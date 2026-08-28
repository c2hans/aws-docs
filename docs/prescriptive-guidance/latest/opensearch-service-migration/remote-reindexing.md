---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/remote-reindexing.html
---

# 3. Remote reindexing
<a name="remote-reindexing"></a>

In this case, the indexes of the source self-managed Elasticsearch or OpenSearch cluster are migrated into the Amazon OpenSearch Service domain using the [reindex document API operation](https://opensearch.org/docs/latest/opensearch/reindex-data). You can use the reindex document API operation to create an index from an existing Elasticsearch or OpenSearch index. The existing index can be in the same cluster where you run the reindex operation, or it can be in a remote cluster. Amazon OpenSearch Service supports using the reindex document API operation with remote clusters. You can reindex from an index in a self-managed Elasticsearch to an index in Amazon OpenSearch Service.

Remote reindex supports Elasticsearch 1.5 and later for the remote Elasticsearch cluster and Amazon OpenSearch Service 6.7 and later for the local domain. For more information, see the blog post [Migrate data into Amazon ES using remote reindex](https://aws.amazon.com/blogs/big-data/migrate-data-into-amazon-es-using-remote-reindex/). The blog post refers to Amazon Elasticsearch, but the guidance applies to Amazon OpenSearch Service domains equally.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
