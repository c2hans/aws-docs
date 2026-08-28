---
source_url: https://docs.aws.amazon.com/sns/latest/dg/firehose-message-analysis-elasticsearch.html
---

# Analyzing Amazon SNS messages for OpenSearch Service destinations
<a name="firehose-message-analysis-elasticsearch"></a>

This topic explains how to analyze Amazon SNS messages sent through delivery streams to Amazon OpenSearch Service (OpenSearch Service) destinations.

**To analyze SNS messages sent through Firehose delivery streams to OpenSearch Service destinations**

1. Configure your OpenSearch Service resources. For instructions, see [Getting Started with Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/es-gsg.html) in the *Amazon OpenSearch Service Developer Guide*.

1. Configure your delivery stream. For instructions, see [Choose OpenSearch Service for Your Destination](https://docs.aws.amazon.com/firehose/latest/dev/create-destination.html#create-destination-elasticsearch) in the *Amazon Data Firehose Developer Guide*.

1. Run a query using OpenSearch Service queries and Kibana. For more information, see [Step 3: Search Documents in an OpenSearch Service Domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/es-gsg-search.html) and [Kibana](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/es-kibana.html) in the *Amazon OpenSearch Service Developer Guide*.

## Example query
<a name="example-es-query"></a>

The following example queries the `my-index` index for all SNS messages received in the specified date range:

```
POST https://search-my-domain.us-east-1.es.amazonaws.com/my-index/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "Timestamp": {
              "gte": "2020-12-08T00:00:00.000Z",
              "lte": "2020-12-09T00:00:00.000Z",
              "format": "strict_date_optional_time"
            }
          }
        }
      ]
    }
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
