---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-list.html
---

# List Channels
<a name="msk-data-delivery-list"></a>

## Using the AWS Management Console
<a name="msk-data-delivery-list-console"></a>

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. In the navigation pane, choose **Clusters**.

1. Choose the name of your Amazon MSK Provisioned cluster with Express brokers.

1. Choose the **Channel** tab.

All Channels for the cluster are listed with name, state, destination type, and creation time.

## Using the AWS CLI
<a name="msk-data-delivery-list-cli"></a>

```
aws kafka list-channels \
    --cluster-arn "arn:aws:kafka:us-east-1:123456789012:cluster/my-express-cluster/abc123"
```

**Note**
Use `--topic-name-filter "orders-topic"` to return only Channels whose source topic name matches the value. Use `--max-results` and `--next-token` to page through results.

Response:

```
{
    "Channels": [
        {
            "ChannelArn": "arn:aws:kafka:us-east-1:123456789012:channel/my-express-cluster/abc123/orders-channel",
            "ChannelName": "orders-channel",
            "Status": "ACTIVE",
            "DestinationType": "ICEBERG",
            "CreationTime": "2026-06-18T10:30:00.000Z"
        },
        {
            "ChannelArn": "arn:aws:kafka:us-east-1:123456789012:channel/my-express-cluster/abc123/clickstream-channel",
            "ChannelName": "clickstream-channel",
            "Status": "ACTIVE",
            "DestinationType": "S3",
            "CreationTime": "2026-06-19T08:15:00.000Z"
        }
    ],
    "NextToken": null
}
```

**API reference** — see `ListChannels` in the *Amazon MSK API Reference*.
