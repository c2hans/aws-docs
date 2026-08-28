---
source_url: https://docs.aws.amazon.com/security-lake/latest/userguide/opensearch-integration.html
---

# Integration with Amazon OpenSearch Service
<a name="opensearch-integration"></a>

**Integration type:** Subscriber

[Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) is a managed service that makes it easy to deploy, operate, and scale OpenSearch Service clusters in the AWS Cloud. Using OpenSearch Service Ingestion to ingest data into your OpenSearch Service cluster, you can derive insights quicker for time sensitive security investigations. You can respond swiftly to security incidents, helping you protect your business critical data and systems.

## OpenSearch Service dashboard
<a name="opensearch-integration-dashboard"></a>

After you integrate OpenSearch Service with Security Lake, you can configure Security Lake to send security data from different sources to OpenSearch Service through serverless OpenSearch Service Ingestion. For more information on how to configure OpenSearch Service ingestion to process security data, see [Generate security insights from Amazon Security Lake data using Amazon OpenSearch Service Ingestion](https://aws.amazon.com/blogs/big-data/generate-security-insights-from-amazon-security-lake-data-using-amazon-opensearch-ingestion/).

After OpenSearch Service Ingestion starts writing your data into your OpenSearch Service domain. To visualize the data using the pre-built dashboards, navigate to dashboards and choose any one of the installed dashboards.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
