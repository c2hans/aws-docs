---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/datasources-opensearch-serverless.html
---

# Amazon OpenSearch Service Serverless
<a name="datasources-opensearch-serverless"></a>

**Note**
OpenSearch Service Serverless support is only available with Grafana workspaces that are running Grafana version 9.4 and later.

You can use the OpenSearch Service data source to access Amazon OpenSearch Service Serverless data with Amazon Managed Grafana. Access to the data is controlled by data access policies. The following example shows a policy that allows users to query a specific collection and index. Be sure to replace {{`collection_name`}}, {{`index_name`}}, and {{`principal_arn`}} with the correct values for your use case.

```
[
  {
    "Rules": [
      {
        "Resource": ["collection/{{{collection_name}}}"],
        "Permission": ["aoss:DescribeCollectionItems"],
        "ResourceType": "collection"
      },
      {
        "Resource": ["index/{{{collection_name}}}/{{{index_name}}}"],
        "Permission": ["aoss:DescribeIndex", "aoss:ReadDocument"],
        "ResourceType": "index"
      }
    ],
    "Principal": ["{{principal_arn}}"],
    "Description": "read-access"
  }
]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
