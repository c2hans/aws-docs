---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-iceberg-describe.html
---

# Describe a Channel
<a name="msk-data-delivery-iceberg-describe"></a>

## Using the AWS Management Console
<a name="msk-data-delivery-iceberg-describe-console"></a>

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. In the navigation pane, choose **Clusters**.

1. Choose the name of your Amazon MSK Provisioned cluster with Express brokers.

1. Choose the **Channel** tab.

1. Choose the name of the Channel to describe.

The detail page shows source topic, destination, delivery settings, current state, and recent Amazon CloudWatch metrics.

## Using the AWS CLI
<a name="msk-data-delivery-iceberg-describe-cli"></a>

```
aws kafka describe-channel \
    --cluster-arn "arn:aws:kafka:us-east-1:123456789012:cluster/my-express-cluster/abc123" \
    --channel-arn "arn:aws:kafka:us-east-1:123456789012:channel/my-express-cluster/abc123/orders-channel"
```

The following is an example response for a streaming tables for Apache Iceberg destination.

```
{
    "ChannelArn": "arn:aws:kafka:us-east-1:123456789012:channel/my-express-cluster/abc123/orders-channel",
    "ChannelName": "orders-channel",
    "TopicConfigurationList": [
        {
            "TopicArn": "arn:aws:kafka:us-east-1:123456789012:topic/my-express-cluster/abc123/orders-topic",
            "RecordConverter": { "ValueConverter": "JSON" },
            "RecordSchema": { "GsrArn": "arn:aws:glue:us-east-1:123456789012:schema/my-registry/orders-schema" }
        }
    ],
    "IcebergDestinationConfiguration": {
        "ServiceExecutionRoleArn": "arn:aws:iam::123456789012:role/MSKChannelRole",
        "DataFreshnessInSeconds": 300,
        "Catalog": {
            "WarehouseLocation": "arn:aws:s3tables:us-east-1:123456789012:bucket/analytics-table-bucket"
        },
        "DeadLetterQueueS3": {
            "BucketArn": "arn:aws:s3:::my-dlq-bucket",
            "ErrorOutputPrefix": "dlq/"
        },
        "DestinationTableList": [
            {
                "DestinationDatabaseName": "analytics_db",
                "DestinationTableName": "orders_iceberg",
                "PartitionSpec": {
                    "PartitionStrategy": "TIME_HOUR",
                    "SourceList": [ { "SourceName": "timestamp" } ]
                }
            }
        ],
        "CompressionType": "ZSTD"
    },
    "Status": "ACTIVE",
    "DestinationType": "ICEBERG",
    "CreationTime": "2026-06-18T10:30:00.000Z"
}
```

**Note**
`Status` is one of `CREATING`, `ACTIVE`, `UPDATING`, `DELETING`, `FAILED`, `SUSPENDING`, `SUSPENDED`. When `Status` is `FAILED`, the response includes a `StateInfo` object with a `Code` and `Message` describing the cause. While an operation is in flight (`CREATING`, `UPDATING`, `DELETING`), the response also includes `ClusterOperationArn`.

**API reference** — see `DescribeChannel` in the *Amazon MSK API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
