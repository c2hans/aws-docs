---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-iceberg-update.html
---

# Update a Channel
<a name="msk-data-delivery-iceberg-update"></a>

You can modify only the data freshness interval (`DataFreshnessInSeconds`, 300–900).

**Important**
You cannot update the source topic, input format, schema, destination configuration, or service execution role of an existing Channel. To change these settings, delete the Channel and create a new one.

## Using the AWS Management Console
<a name="msk-data-delivery-iceberg-update-console"></a>

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. In the navigation pane, choose **Clusters**.

1. Choose the name of your Amazon MSK Provisioned cluster with Express brokers.

1. Choose the **Channel** tab.

1. Select the Channel to update and choose **Edit data freshness**.

1. Modify **Data freshness** (5–15 minutes), then choose **Save changes**.

## Using the AWS CLI
<a name="msk-data-delivery-iceberg-update-cli"></a>

Use the update field that matches the Channel's destination type — `--iceberg-destination-update` for an Iceberg destination.

```
aws kafka update-channel \
    --cluster-arn "arn:aws:kafka:us-east-1:123456789012:cluster/my-express-cluster/abc123" \
    --channel-arn "arn:aws:kafka:us-east-1:123456789012:channel/my-express-cluster/abc123/orders-channel" \
    --iceberg-destination-update '{
        "DataFreshnessInSeconds": 600
    }'
```

Response:

```
{
    "ChannelArn": "arn:aws:kafka:us-east-1:123456789012:channel/my-express-cluster/abc123/orders-channel",
    "ClusterOperationArn": "arn:aws:kafka:us-east-1:123456789012:cluster-operation/my-express-cluster/abc123/..."
}
```

**Note**
A `200` response indicates the update was accepted; the Channel transitions to `UPDATING` and returns to `ACTIVE` when complete. Track progress with the `ClusterOperationArn`.

**API reference** — see `UpdateChannel` in the *Amazon MSK API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
